# Use the official Python 3.12 slim image as the base image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file from the host to the container
COPY requirements.txt .

# Install all Python dependencies listed in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy all application files from the host to the container
COPY . .

# Inform Docker that the application listens on port 5000
EXPOSE 5000

# Run the Flask application when the container starts
CMD ["python", "app.py"]
