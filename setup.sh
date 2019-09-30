#!/bin/bash

git clone https://github.com/Koenkk/zigbee-shepherd-converters.git ./zigbee2mqtt/zigbee-shepherd-converters
mkdir -p zigbee2mqtt/lib/extension/
wget https://raw.githubusercontent.com/Koenkk/zigbee2mqtt/master/lib/extension/homeassistant.js -O ./zigbee2mqtt/lib/extension/homeassistant.js

docker network create --driver=bridge --subnet=172.100.50.0/24 --ip-range=172.100.50.0/24 --gateway=172.100.50.1 nginx_network

mkdir -p mosquitto/data