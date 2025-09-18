FROM python:3.11-slim
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc libssl-dev libldap2-dev libsasl2-dev python3-dev \
 && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY student_age.py .
VOLUME ["/data"]
EXPOSE 5000
CMD ["python", "student_age.py"]