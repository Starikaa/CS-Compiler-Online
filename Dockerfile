FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y openjdk-21-jdk build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 9000

CMD ["python", "run.py"]