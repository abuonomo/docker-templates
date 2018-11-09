#!/usr/bin/env bash
docker run -p 80:80 -v $(pwd)/nginx:/etc/nginx  nginx
#--link flask_test:flask_test
