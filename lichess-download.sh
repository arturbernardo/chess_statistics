#!/usr/bin/env bash
set -e

URL="https://lichess.org/api/games/user/${LICHESS_USER}?rated=true&tags=true&clocks=false&evals=false&opening=false&literate=false&max=${SIZE}&since=${SINCE}&until=${UNTIL}&perfType=${PERF_TYPE}"

curl -fL -H "Accept: application/x-chess-pgn" "$URL" -o /home/ubuntu/games.pgn