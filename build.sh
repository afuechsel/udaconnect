#! /bin/bash

MODULES=modules
SERVICES=$MODULES/services

docker login -u afuechsel 

docker build -t udaconnect-connection-api $SERVICES/connection
docker build -t udaconnect-location-api $SERVICES/location
docker build -t udaconnect-person-api $SERVICES/person
docker build -t udaconnect-frontend $MODULES/frontend

docker tag udaconnect-connection-api afuechsel/udaconnect-connection-api
docker tag udaconnect-location-api afuechsel/udaconnect-location-api
docker tag udaconnect-person-api afuechsel/udaconnect-person-api
docker tag udaconnect-frontend afuechsel/udaconnect-frontend

docker push afuechsel/udaconnect-connection-api
docker push afuechsel/udaconnect-location-api
docker push afuechsel/udaconnect-person-api
docker push afuechsel/udaconnect-frontend
