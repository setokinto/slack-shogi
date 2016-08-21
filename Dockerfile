FROM python:3.5.1
MAINTAINER Kouki Saito <dan.addr.skd@gmail.com>

RUN groupadd -r slackbot && useradd -r -g slackbot slackbot
COPY . /app
WORKDIR /app
RUN python setup.py develop
COPY slackbot_settings.py.docker slackbot_settings.py

USER slackbot
CMD ["python", "main.py"]

