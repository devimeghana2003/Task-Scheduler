# Use the official Python base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files
COPY app.py .
COPY templates templates

# Expose the port your Flask application is running on
EXPOSE 5000

# Run the Flask application
CMD ["python", "app.py"]
