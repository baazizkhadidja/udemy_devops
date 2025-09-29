FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY student_age.py .
VOLUME ["/data"]
EXPOSE 5000
CMD ["python", "student_age.py"]