FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY ./app /app/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
