# htmx and hyperscript examples with FastAPI backend

A learning project.

## server

Create pipenv virtualenv local:

`set -x PIPENV_VENV_IN_PROJECT 1; pipenv shell`

## web

css: https://github.com/picocss/pico

icons: https://glyphs.fyi/dir?i=cog

## API Gateway / Reverse Proxy: caddy

see `Caddyfile`

- install: https://caddyserver.com/docs/install#static-binaries
- reverse proxy doc: https://caddyserver.com/docs/caddyfile/directives/reverse_proxy
- tut: https://florian-vick.medium.com/why-you-should-use-caddy-as-your-webserver-19f5947efb3e

#### if not enough use krakend

- install: https://www.krakend.io/docs/overview/introduction/
- conf designer: https://github.com/devopsfaith/krakendesigner

## dev config

Prerequisites:

- install caddy (void linux has latest binary but no plugins dev)
- in `server` activate venv: 'pipenv shell' and install `pipenv install`
- install pnpm (although just npm might work) and install node packages in `web`

Must launch three "servers" from project root dir:

- caddy: `caddy run --config ./Caddyfile`
- backend: `cd server && python -m uvicorn main:app --reload`
- frontend: `cd web && pnp run dev`

Using https://github.com/open-cli-tools/concurrently is nicer:

```sh
concurrently --kill-others-on-fail --names "CADDY,BACKEND,FRONTEND" \
      "caddy run --config ./Caddyfile" \
      "cd server && python -m uvicorn main:app --reload" \
      "cd web && pnpm run dev"
```
