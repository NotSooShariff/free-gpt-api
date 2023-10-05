# Use the official Debian repository
FROM debian:bookworm-slim

# Use a base image with Python
# FROM python:3.7-slim

# Install necessary packages, including pip
RUN apt-get update && apt-get install -y chromium-driver python3-pip
RUN apt-get install -y python3.11-venv

# Set chromedriver binary path
ENV CHROME_DRIVER_PATH /usr/bin/chromedriver

# Set workspace
WORKDIR /app

# Copy local files
COPY . .

# Create and activate a virtual environment
RUN python3 -m venv venv
ENV VIRTUAL_ENV=/app/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install Python dependencies using pip within the virtual environment
RUN pip install -r requirements.txt
RUN pip install --upgrade Flask Flask-Cors Flask-RESTful

# Set environment variables
ENV APP_HOME /app
ENV PORT 5000

# Start the application
CMD exec gunicorn --bind :${PORT} --workers 1 --threads 8 app:app