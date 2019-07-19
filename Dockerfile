FROM python:3.7-slim

WORKDIR /usr/src/app

COPY ./python/ /

RUN pip install -r /requirements.txt

CMD ["python", "/app.py"] 