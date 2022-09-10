# syntax=docker/dockerfile:1

FROM python:3.10-alpine

WORKDIR /bot

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

RUN python3 -m pip install python-dotenv

COPY . .

CMD [ "python3", "bot.py"]