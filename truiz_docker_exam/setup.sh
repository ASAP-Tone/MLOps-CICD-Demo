#!/bin/bash

# Build docker images
for x in 'authentication' 'authorization' 'content'
do 
cd test_$x
ls
echo "Building image $x"
docker image build . -t ${x}_image:latest
cd ..
done 

# Execute docker compose
docker-compose up

sleep 10 

docker-compose down