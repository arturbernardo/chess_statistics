TODO:
- Add elo of the players to the analysis csv.
- Analyse only the movements of the user in question. It is currently evaluating all the movements of the game.
- .out is not showing the cp. But running in the terminal shows all the depths and cps. Some stdin stdout magic need to be solved. (DONE)
- update pip use to python3 -m pip install python-chess (DONE)
- Use pypy? (Only if some heavy work  is added to python code)
- git actions? (NO)
- exec all the pipeline when machine starts
- outputs with the status of the process. (DONE)
- Analysis based on knowledge from here https://drive.google.com/file/d/11IokKgTVSXdpYEzAuyViIleSZ_2wl0ag/view

# Stack result
aws cloudformation describe-stacks --stack-name chess-analysis

# connect
ssh -i chave.pem ubuntu@IP

# cloud-init logs
sudo tail -f /var/log/cloud-init-output.log


# Download file
scp -i chave.pem usuario@IP_DA_EC2:/caminho/do/arquivo ./ 

or

cd /home/ec2-user/dados
python3 -m http.server 8000


# transmitir arquivo
scp -i n8n.pem ~/Downloads/lichess_db_standard_rated_2013-01.pgn ubuntu@IP:/home/ubuntu


http://IP_DA_EC2:8000/resultado.csv

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


#pgn extractor
## tipo de jogo
Versao 25
pgn-extract -Wlalg --event "Rated Classical" input.pgn > classical.pgn
pgn-extract -Wlalg --event "Rated Blitz" input.pgn > blitz.pgn
pgn-extract -Wlalg --event "Rated Bullet" input.pgn > bullet.pgn

versao 15
touch criteria.txt
echo 'Event "Rated Blitz"' > criteria.txt
pgn-extract --tagsubstr -tcriteria.txt -o blitz.pgn input.pgn

or

touch blitz_white.txt
touch blitz_black.txt

cat <<EOF > blitz_white.txt
Event "Rated Blitz"
White "BFG9k"
EOF

cat <<EOF > blitz_black.txt
Event "Rated Blitz"
Black "BFG9k"
EOF

pgn-extract --tagsubstr -tblitz_white.txt -o tmp_white.pgn input.pgn
pgn-extract --tagsubstr -tblitz_black.txt -o tmp_black.pgn input.pgn

cat tmp_white.pgn tmp_black.pgn > blitz_player.pgn

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

# RUNS
python3 pgn_to_fen.py input.pgn \
| python3 eval.py \
> analysis.csv

python3 pgn_to_fen.py input.pgn \
| python3 eval.py \
| python3 cpl.py \
> analysis.csv

#sorted 
sort -t, -k1,1n -k2,2n analysis.csv > analysis_sorted.csv

# RUN and SORT
python3 pgn_to_fen.py input.pgn \
| python3 eval.py \
| { read -r header; echo "$header"; sort -t, -k1,1n -k2,2n; } \
> analysis.csv

python3 pgn_to_fen.py input.pgn \
| python3 eval.py \
| python3 cpl.py \
| { read -r header; echo "$header"; sort -t, -k1,1n -k2,2n; } \
> analysis.csv


python3 pgn_to_fen.py input.pgn | python3 eval.py | { read -r header; echo "$header"; sort -t, -k1,1n -k2,2n; } > analysis.csv


DEPRECATED:
1 
python3 pgn_to_fen.py input.pgn > positions.csv

2
./fen_to_uci.sh

3 (problems with stdin stdout) 
parallel -j 8 stockfish \< {} \> {.}.out ::: uci/*.uci

4
python3 parse_out.py > analysis.csv