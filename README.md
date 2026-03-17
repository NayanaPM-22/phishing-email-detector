# 🛡️ Phishing Email Detector

> Fine-tuned DistilBERT model achieving **99.25% F1 Score** on 79,537 real emails

---

## 📌 Overview

A full-stack machine learning application that detects phishing emails using:

- **DistilBERT** — Fine-tuned transformer model for text classification
- **URL Risk Scoring** — Lookalike domain detection, suspicious keyword analysis
- **Explainable AI** — LIME and SHAP explanations for every prediction
- **FastAPI** — REST API backend
- **Interactive Web UI** — Beautiful 2-page frontend

---

## 🏆 Model Performance

| Metric    | Score      |
| --------- | ---------- |
| Accuracy  | 99.20%     |
| Precision | 99.05%     |
| Recall    | 99.46%     |
| F1 Score  | **99.25%** |

---

## 🗂️ Dataset

- **Sources:** CEAS_08, Enron, Nazario, Nigerian Fraud, SpamAssassin
- **Total emails:** 79,537
- **Distribution:** 53% Phishing / 47% Legitimate
- **Train/Test split:** 80/20

---

## 🏗️ Project Architecture

```
Email Input
    │
    ├── Text Preprocessing (NLTK)
    │       └── Cleaning, Stopword removal, Lemmatization
    │
    ├── URL Risk Scoring
    │       └── Lookalike domain detection, Suspicious keywords
    │
    ├── DistilBERT Feature Extraction
    │       └── 512 token embeddings
    │
    ├── Classification
    │       └── Binary: Phishing / Legitimate
    │
    └── Explainability
            ├── LIME — Word importance
            └── SHAP — Feature contributions
```

---

## 🚀 How to Run

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend

Open `frontend/index.html` in browser

### API Endpoints

| Endpoint   | Method | Description   |
| ---------- | ------ | ------------- |
| `/health`  | GET    | Health check  |
| `/predict` | POST   | Predict email |

---

## 🔧 Tech Stack

| Category        | Technology                           |
| --------------- | ------------------------------------ |
| ML/NLP          | DistilBERT, HuggingFace Transformers |
| Explainability  | LIME, SHAP                           |
| Backend         | FastAPI, Uvicorn                     |
| Frontend        | HTML, CSS, JavaScript                |
| Data Processing | Pandas, NLTK, Scikit-learn           |
| Deployment      | Docker                               |

---

## 📊 Key Features

- ✅ Real-time phishing detection
- ✅ URL risk analysis with lookalike domain detection
- ✅ Explainable AI — understand WHY an email is flagged
- ✅ REST API for easy integration
- ✅ Beautiful interactive web interface
- ✅ Docker support

---

## 👥 Team

- Lekhanashree M (231AI016)
- Nayana Yogeshwari PM (231AI023)
- Tanmai K (231AI039)

**IT471 - Cyber Security Project**
