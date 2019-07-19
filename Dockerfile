FROM python:3.7-slim

WORKDIR /usr/src/app

# Copy current working directory to /app/
COPY ./python/ /

# Install any needed packages specified in requirements.txt
RUN pip install -r /requirements.txt

# Run app.py when the container launches
CMD ["python", "/app.py"] 