FROM python:3.11-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt .
# The GPU runtime image should supply CUDA-compatible PyTorch separately.
RUN pip install --no-cache-dir -r requirements.txt
COPY henai ./henai
COPY app.py .
RUN mkdir -p /app/outputs
EXPOSE 7860
CMD ["python", "app.py"]
