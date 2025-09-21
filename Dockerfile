FROM python:3.10-slim
WORKDIR /app
COPY app/ /app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["streamlit", "run", "frontend.py", "--server.port=8501", "--server.address=0.0.0.0"]
