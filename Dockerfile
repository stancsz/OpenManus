# Use an official Python 3.12 slim image.
FROM python:3.12-slim

# Prevent Python from buffering stdout and stderr.
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container.
WORKDIR /app

# Install curl (if needed for other purposes) and clean up apt cache.
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Upgrade pip to the latest version.
RUN pip install --upgrade pip

# Copy the requirements file into the container.
COPY requirements.txt .

# Install the dependencies using pip.
RUN pip install -r requirements.txt

# Copy the rest of the application code.
COPY . .

# Expose port 5000 (Flask's default port).
EXPOSE 5000

# Set the Flask app environment variable.
ENV FLASK_APP=app.py

# Run the Flask application.
CMD ["python", "app.py"]
