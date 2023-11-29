FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt \
    && pip install torch --no-cache-dir --index-url https://download.pytorch.org/whl/cpu \
    && rm -rf /root/.cache \
    && rm -rf /var/lib/apt/lists/*

CMD ["gunicorn","--bind","0.0.0.0:5000","app:app"]