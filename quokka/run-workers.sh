cd ~/quokka
sudo python3 workers/quokka_worker.py -H ${1:-15} -W capture -Q localhost -S 111-111-111 -C rabbitmq &
sudo python3 workers/quokka_worker.py -H ${1:-15} -W portscan -Q localhost -S 111-111-111 -C rabbitmq &
sudo python3 workers/quokka_worker.py -H ${1:-15} -W traceroute -Q localhost -S 111-111-111 -C rabbitmq &
