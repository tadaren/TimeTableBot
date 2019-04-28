FROM python:3.7-alpine3.9

WORKDIR /app

ADD . /app

RUN pip install pymongo bottle

ENV DB_URL "mongodb://127.0.0.1:27017"
ENV HOST "0.0.0.0"
ENV PORT "8000"

EXPOSE 8000

CMD ["python3", "server.py"]
