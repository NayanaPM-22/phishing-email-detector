# Dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

### **Step 2 — Create requirements.txt**
Create a new file inside `backend/` called `requirements.txt`:
```
fastapi
uvicorn
transformers
torch
python-multipart
pydantic