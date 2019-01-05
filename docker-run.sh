#!/bin/bash

docker run --rm -d -v $(pwd)/public:/root/public -p 80:80 --name rsspaper rsspaper
