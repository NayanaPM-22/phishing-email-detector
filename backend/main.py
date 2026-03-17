# main.py - FastAPI backend
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from model_loader import predict
import re

app = FastAPI(title='Phishing Email Detector API')

# Allow frontend to call API
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
)

# Input schema
class EmailInput(BaseModel):
    email_text: str

# URL extractor
def extract_urls(text):
    pattern = r'http[s]?://(?:[a-zA-Z0-9$\-_@.&+!*\\(\\),]|(?:%[0-9a-fA-F]{2}))+'
    return re.findall(pattern, text)

# URL risk scorer
def score_urls(text):
    urls = extract_urls(text)
    if not urls:
        return 0.0
    risk = 0
    for url in urls[:5]:
        if url.startswith('http://'):   risk += 1
        if len(url) > 75:               risk += 1
        if re.match(r'http[s]?://\d+\.\d+\.\d+\.\d+', url): risk += 2
        if any(kw in url.lower() for kw in 
               ['login','verify','secure','account','confirm','signin']): risk += 1
    return min(risk / 8, 1.0)

# Urgency keywords
URGENCY_WORDS = ['urgent', 'verify', 'click', 'suspended', 'account',
                 'password', 'confirm', 'update', 'limited', 'expire',
                 'warning', 'immediately', 'alert', 'security', 'bank']

@app.get('/health')
def health():
    return {'status': 'ok', 'message': 'Phishing Detector API is running'}

@app.post('/predict')
def predict_email(input: EmailInput):
    text = input.email_text

    # Get BERT prediction
    result = predict(text)

    # Extra features
    urls = extract_urls(text)
    url_risk = score_urls(text)
    urgency = sum(w in text.lower() for w in URGENCY_WORDS)

    return {
        'label': result['label'],
        'confidence': result['confidence'],
        'phishing_probability': result['phishing_probability'],
        'legitimate_probability': result['legitimate_probability'],
        'url_count': len(urls),
        'url_risk_score': round(url_risk, 3),
        'urgency_word_count': urgency,
        'urls_found': urls[:5]
    }