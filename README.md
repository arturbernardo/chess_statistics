TODO:
- Use pypy?
- git actions?
- exec all the pipeline when machine starts
- outputs with the status of the process.


# Jupyter hash key new login
journalctl -u jupyter

#Stockfish via terminal
stockfish
setoption name Hash value 1024
setoption name Threads value 16
position startpos
go depth 18


# Stockfish consuming all cores:
htop

# compilar stockfish otimizado para o processador
sudo apt install -y build-essential
git clone https://github.com/official-stockfish/Stockfish.git
cd Stockfish/src
make build ARCH=x86-64-avx2 -j$(nproc)
sudo cp stockfish /usr/local/bin/stockfish-avx2



# transmitir arquivo
scp -i n8n.pem ~/Downloads/lichess_db_standard_rated_2013-01.pgn ubuntu@IP:/home/ubuntu

#pgn extractor
## tipo de jogo
pgn-extract -Wlalg --event "Rated Classical" input.pgn > classical.pgn
pgn-extract -Wlalg --event "Rated Blitz" input.pgn > blitz.pgn
pgn-extract -Wlalg --event "Rated Bullet" input.pgn > bullet.pgn

## usuário
pgn-extract -Wlalg --player "BFG9k" input.pgn > bfg9k.pgn

## Combinado
pgn-extract -Wlalg \
  --event "Blitz" \
  --player "BFG9k" \
  input.pgn > bfg9k_blitz.pgn

### evita overhead de comentários e reescrita
-Wlalg

### se quiser apenas validar antes
--check-only


# 1 
python pgn_to_fen.py lichess_db_standard_rated_2013-01.pgn.pgn > positions.csv


# 2 
parallel -j 8 stockfish \< {} \> {.}.out ::: uci/*.uci

# 3
python parse_out.py > analysis.csv