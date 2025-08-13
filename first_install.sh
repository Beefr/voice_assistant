#!/bin/bash

echo "Il faut mettre son wifi en compatibilité 2.4 Ghz"
echo "Ensuite il faut appeler ce script avec comme paramètre le mot de passe wifi puis le nom du wifi entre ' et '"


if [ $# -eq 2 ]; then
	connexion="$2"
else
	connexion='Mi 10T Lite'
fi

nmcli device wifi connect "$connexion" password "$1"

nmcli connection show --active


sudo apt update
sudo apt upgrade -y
sudo apt install python3 -y
sudo apt install vim -y
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
