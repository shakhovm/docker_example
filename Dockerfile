# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install required Python packages
RUN pip install -r requirements.txt

# Make port 8050 available to the outside world
EXPOSE 8050

# Run the application
CMD ["python", "main.py"]
