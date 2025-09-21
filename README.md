# Expense Tracker System

This project is a modern expense tracking system, built as part of the "Engineering of Advanced Software Solutions" (EASS) course.  
It includes a backend API (FastAPI), a frontend interface (Streamlit), persistent storage (TinyDB), and unit/integration testing.

---

## 📁 Project Structure

```
expense-tracker/
│
├── app/
│   ├── main.py              # FastAPI backend with expense/user/category logic
│   ├── models.py            # Pydantic models
│   ├── db.py                # TinyDB storage logic
│   ├── frontend.py          # Streamlit frontend
│   ├── requirements.txt     # All dependencies
│   ├── integration_test.py  # End-to-end test
│
├── tests/
│   ├── conftest.py          # Fixtures
│   ├── test_main.py         # Unit tests for API
│   ├── unit_tests.py        # Streamlit and logic tests
│
├── Dockerfile               # Backend Docker setup
├── docker-compose.yml       # Full system (backend + frontend)
├── README.md                # Project documentation
```

---

## 🚀 Features

- ✅ Add/delete expenses with category, user, and description  
- ✅ REST API with FastAPI and pydantic models  
- ✅ Lightweight database using TinyDB (JSON file)  
- ✅ Streamlit frontend: user & category support  
- ✅ Unit + integration tests (pytest)  
- ✅ Docker & Docker Compose ready  

---

## 🧩 Requirements

- Python 3.10+  
- pip  
- Git  
- Docker & Docker Compose (optional for deployment)  

---

## 🛠️ Running the Project

### Option 1: Local run (no Docker)

Install dependencies:
```bash
pip install -r app/requirements.txt
```

Run backend:
```bash
cd app
uvicorn main:app --reload
```

Run frontend (in new tab):
```bash
streamlit run frontend.py
```

> API: [http://localhost:8000/docs](http://localhost:8000/docs)  
> UI: [http://localhost:8501](http://localhost:8501)

---

### Option 2: Run with Docker

Start everything:
```bash
docker-compose up --build
```

> Backend: [http://localhost:8000/docs](http://localhost:8000/docs)  
> Frontend: [http://localhost:8501](http://localhost:8501)

---

## 🧪 Run Tests

```bash
pytest
```

Covers:
- ✅ Unit tests (validation, API)  
- ✅ Integration test (full expense cycle)

---

## 🔗 Repository

GitHub: [https://github.com/AmitKei/Expense-Tracker](https://github.com/AmitKei/Expense-Tracker)