#!/bin/sh
exec "git pull"
exec "docker compose build"
exec "docker compose down"
exec "docker compose up -d backend-node"
exec "docker compose up -d nginx-node"