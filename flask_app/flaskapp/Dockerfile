FROM --platform=linux/arm/v7 python:3.7.2-stretch

WORKDIR /Docker/flaskapp

ADD . /Docker/flaskapp 

RUN pip install -r requirements.txt

CMD ["uwsgi","app.ini"]
