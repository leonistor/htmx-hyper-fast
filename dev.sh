#!/bin/bash

concurrently --kill-others-on-fail --names "CADDY,BACKEND,FRONTEND" \
    "caddy run --config ./Caddyfile" \
    "cd server && pipenv run python -m uvicorn main:app --reload" \
    "cd web && pnpm run dev"
