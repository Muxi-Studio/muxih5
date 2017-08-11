FROM python:2.7
MAINTAINER neo1218 <neo1218@yeah.net>

Add . .

RUN pip install mana
RUN python deploy.py

ENV DEPLOY_PATH /deploy

WORKDIR $DEPLOY_PATH

Add requirements.txt requirements.txt
RUN pip install --index-url http://pypi.doubanio.com/simple/ -r requirements.txt --trusted-host=pypi.doubanio.com
# RUN pip install --index-url https://pypi.python.org/simple/ -r requirements.txt --trusted-host=pypi.python.org
