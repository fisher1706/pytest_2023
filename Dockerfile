FROM python:3.8-alpine

LABEL "channel"="SolveMe"
LABEL "creator"="SolveMe community"

WORKDIR ./usr/lessons
COPY . .

RUN apk update && apk upgrade && apk add bash
RUN pip3 install -r requirements.txt

CMD pytest -s -v tests/*
