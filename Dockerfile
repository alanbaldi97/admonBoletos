FROM python:3.8.3-alpine3.12
RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip

COPY . /usr/src/app
WORKDIR /usr/src/app

RUN chmod -R o+rX .

RUN apk add --update --no-cache g++ gcc libxml2-dev libxslt-dev python3-dev libffi-dev openssl-dev make
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 5000
CMD ["python3","main.py"]