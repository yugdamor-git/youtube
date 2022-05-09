#!/bin/sh
git pull
docker compose build
docker compose down
docker compose up -d backend-node
docker compose up -d nginx-node