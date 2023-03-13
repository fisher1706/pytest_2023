FROM python:3.8-alpine

ARG run_env=development
ENV env $run_env

LABEL "channel"="SolveMe"
LABEL "creator"="SolveMe community"

WORKDIR ./usr/lessons

VOLUME /allureResults

COPY requirements.txt .

RUN pip3 install -r requirements.txt
RUN apk update && apk upgrade && apk add bash

COPY . .

CMD pytest -m "$env" -s -v tests/* --alluredir=allureResults
