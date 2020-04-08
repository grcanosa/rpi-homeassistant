#!/bin/bash

cd nginx/ssl/
/usr/local/bin/certbot-auto certonly --standalone -d *.grcanosa.com
sudo chown -R grcanosa:grcanosa /etc/letsencrypt/archive/
cp /etc/letsencrypt/archive/home.grcanosa.com/*.pem .