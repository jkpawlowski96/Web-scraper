#FROM ubuntu:latest  

# Use an official Python runtime as a parent image
FROM python:3.6

RUN export PYTHONPATH=$PYTHONPATH:/app
RUN python -m pip install pymongo[srv]

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container

# Define environment variable
#ENV NAME World
EXPOSE 5000

ENTRYPOINT  ["python3"]

CMD ["app.py"]


