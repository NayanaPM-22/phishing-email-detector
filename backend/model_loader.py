# model_loader.py - Loads and runs the BERT model
import torch
from transformers import DistilBertForSequenceClassification, DistilBertTokenizer
import os

# Path to model
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'bert_model')

# Setup device
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Load model and tokenizer
print(f'Loading model from {MODEL_PATH}...')
tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
model = DistilBertForSequenceClassification.from_pretrained(MODEL_PATH)
model = model.to(device)
model.eval()
print(f'✅ Model loaded on {device}')

def predict(text: str):
    # Tokenize
    encoding = tokenizer(
        str(text),
        max_length=512,
        padding='max_length',
        truncation=True,
        return_tensors='pt'
    )

    input_ids = encoding['input_ids'].to(device)
    attention_mask = encoding['attention_mask'].to(device)

    # Predict
    with torch.no_grad():
        outputs = model(input_ids=input_ids, attention_mask=attention_mask)
        probs = torch.softmax(outputs.logits, dim=1)
        phishing_prob = probs[0][1].item()
        legit_prob = probs[0][0].item()

    label = 'Phishing' if phishing_prob > 0.5 else 'Legitimate'

    return {
        'label': label,
        'phishing_probability': round(phishing_prob * 100, 2),
        'legitimate_probability': round(legit_prob * 100, 2),
        'confidence': round(max(phishing_prob, legit_prob) * 100, 2)
    }