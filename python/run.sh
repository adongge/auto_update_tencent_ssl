#!/usr/bin/env sh

export $(xargs < /python/.env)
/usr/bin/python /python/main.py