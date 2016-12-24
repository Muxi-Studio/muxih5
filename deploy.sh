#!/bin/sh

cd deploy && docker-compose build && docker-compose up -d
