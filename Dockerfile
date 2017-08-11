FROM python:2.7
MAINTAINER neo1218 <neo1218@yeah.net>

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . /usr/src/app

RUN pip install mana
RUN python deploy.py

ENV DEPLOY_PATH /deploy
WORKDIR /usr/src/app$DEPLOY_PATH

RUN pip install --index-url http://pypi.doubanio.com/simple/ -r requirements.txt --trusted-host=pypi.doubanio.com
# RUN pip install --index-url https://pypi.python.org/simple/ -r requirements.txt --trusted-host=pypi.python.org