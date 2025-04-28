# Vulnerable base image
FROM python:3.8-alpine

WORKDIR /app

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy application code
COPY . .

# Expose Flask's default port
EXPOSE 5001

# CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
CMD ["python", "app/main.py"]
