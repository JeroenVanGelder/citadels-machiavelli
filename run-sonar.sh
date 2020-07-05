#!/bin/bash

docker run -d --name sonarqube -p 9000:9000 sonarqube:latest

wait 10

docker run -e SONAR_HOST_URL=http://192.168.2.8:9000 -e SONAR_TOKEN=1ef536359540a9dc675dc05cddd95d37afb97230 -it -v "$PWD:/usr/src" sonarsource/sonar-scanner-cli
