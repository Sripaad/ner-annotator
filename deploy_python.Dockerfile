FROM python:3.8-slim-buster

WORKDIR /app

COPY ./annotator /app
COPY requirements.txt /app

RUN pip install -r requirements.txt

# CMD ["python", "server.py"]
CMD ["python", "-m", "uvicorn", "app:app", "--reload", "--port=5555"]
