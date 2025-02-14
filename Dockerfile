# Use official Python image
FROM python:3.12.6-slim

# Seting the working directory in the container
WORKDIR /app

# Copying all the files from the current directory to the container
COPY . /app

# Installing the dependencies
RUN pip install --no-cache-dir fastapi uvicorn joblib scikit-learn pandas

# Expose API port
EXPOSE 8000

# Run FastAPI server
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
