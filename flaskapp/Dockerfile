FROM python:3.7.2-stretch

WORKDIR /website

ADD . /website 

RUN pip install -r requirements.txt

CMD ["uwsgi","app.ini"]