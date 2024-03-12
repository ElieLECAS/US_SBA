#!/bin/sh

docker build -t elielecas/us_sba-app ./app/
docker push elielecas/us_sba-app

docker build -t elielecas/us_sba-api ./api/
docker push elielecas/us_sba-api

az container create --resource-group RG_LECASE --file deploy.yaml