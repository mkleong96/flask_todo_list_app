# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim

WORKDIR /app

ENV FLASK_APP=run.py

COPY ./requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["flask", "run", "-h", "0.0.0.0", "--cert=adhoc"]
