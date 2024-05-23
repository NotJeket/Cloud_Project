# Use a base image. Here, we're using the official Python image as an example.
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script into the container
COPY hello_docker.py /app/

# Define the command to run the Python script when the container starts
CMD ["python", "hello_docker.py"]
