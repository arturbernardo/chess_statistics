#!/bin/bash

THREADS=1
HASH=1024
DEPTH=18

mkdir -p uci

while IFS=, read -r game move fen; do
  file="uci/g${game}_m${move}.uci"
  cat > "$file" <<EOF
uci
isready
setoption name Threads value $THREADS
setoption name Hash value $HASH
position fen $fen
go depth $DEPTH
EOF
done < positions.csv
