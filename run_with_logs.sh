#!/bin/bash

TTY=$(ls /dev/ttyACM*)
echo $TTY
sed s#TTYDEVICE#$TTY#g template-docker-compose.yml > no-commit-docker-compose.yaml
docker-compose -f no-commit-docker-compose.yaml down
docker container prune
docker-compose -f no-commit-docker-compose.yaml up