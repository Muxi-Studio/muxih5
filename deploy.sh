#!/bin/sh

cd deploy && docker-compose build && docker-compose stop && docker-compose up -d
