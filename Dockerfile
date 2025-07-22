# Use the official Python image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Expose port 8080 (Flask default for Cloud Run)
EXPOSE 8080

# Run the app
CMD ["python", "app.py"]
