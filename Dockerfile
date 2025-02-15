# Use a stable and compatible Python image
FROM python:3.12.6-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y gcc

# Copy only requirements first (optimizing caching)
COPY requirements.txt .

# Installing dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app files
COPY . .

# Ensure entrypoint scripts have execute permissions
RUN chmod +x /app

# Expose API port
EXPOSE 8000

# Run FastAPI server
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
