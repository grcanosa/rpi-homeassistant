#!/bin/bash

git clone https://github.com/Koenkk/zigbee-shepherd-converters.git ./zigbee2mqtt/zigbee-shepherd-converters
wget https://raw.githubusercontent.com/Koenkk/zigbee2mqtt/master/lib/extension/homeassistant.js -O ./zigbee2mqtt/lib/extension/homeassistant.js
mkdir -p mosquitto/data