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



# transmotir arquivo
scp -i n8n.pem ~/Downloads/lichess_db_standard_rated_2013-01.pgn ubuntu@204.236.198.227:/home/ubuntu


# 1 
python pgn_to_fen.py lichess_db_standard_rated_2013-01.pgn.pgn > positions.csv


# 2 

