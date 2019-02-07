FROM python:3.7.1
MAINTAINER Kouki Saito <dan.addr.skd@gmail.com>

RUN groupadd -r slackbot && useradd -r -g slackbot slackbot
WORKDIR /app
COPY ./setup.py setup.py
RUN pip install -e .
COPY . .

USER slackbot
CMD ["python", "input_emojis.py"]

