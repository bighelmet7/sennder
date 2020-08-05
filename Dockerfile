FROM python:3

LABEL "autor"="Abner Andino"
LABEL "github"="@bighelmet7"
LABEL "version"="1.0"
LABEL "description"="Sennder technical exam"

RUN apt-get update && apt-get install -yyq netcat

WORKDIR /opt/sennder
ADD . /opt/sennder

RUN mkdir -p /var/logs/sennder && touch /var/logs/sennder/sennder.logs

RUN pip install -r requirements.txt

RUN chmod 755 entrypoint.sh

EXPOSE 5001
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV FLASK_APP app.py