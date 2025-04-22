# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Make apt retry transient failures, then update & install all build dependencies in one go
RUN echo 'Acquire::Retries "5";' > /etc/apt/apt.conf.d/80-retries \
 && apt-get update \
 && apt-get install -y --no-install-recommends \
       apt-utils \
       gcc \
       python3-dev \
       libffi-dev \
       libpq-dev \
       pkg-config \
       libcairo2-dev \
       cmake \
       libpangocairo-1.0-0 \
       libpng-dev \
       libssl-dev \
       libjpeg62-turbo-dev \
 && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy application code
COPY . /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Expose the application port
EXPOSE 8000

# Default command
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
