#/bin/bash

windows_username=coren

sudo useradd $windows_username -d /home/$windows_username -m -s /bin/bash
sudo usermod -aG sudo $windows_username
groupadd vagrant
sudo usermod -aG vagrant $windows_username
sudo passwd $windows_username

mkdir /home/coren/.ssh
mv /home/vagrant/keys/* /home/$windows_username/.ssh
chown $windows_username:$windows_username /home/$windows_username/.ssh/*
chmod 600 /home/$windows_username/.ssh/*

echo "alias r0='ssh rsp0diet32'" >> /home/$windows_username/.bash_aliases
echo "alias r4='ssh rsp4diet64go'" >> /home/$windows_username/.bash_aliases
echo "alias ll='ls -lrt'" >> /home/$windows_username/.bash_aliases
echo "alias hosts='ansible all --list-hosts'" >> /home/$windows_username/.bash_aliases

export PATH="${PATH}:/home/$windows_username/.local/bin"

mv /home/vagrant/ansible.cfg /home/$windows_username/ansible.cfg
mv /home/vagrant/inventaire /home/$windows_username/inventaire
mv /home/vagrant/play_installpython.yaml /home/$windows_username/play_installpython.yaml
mv /home/vagrant/play_changemotd.yaml /home/$windows_username/play_changemotd.yaml

mkdir /home/$windows_username/host_vars
echo "---" >> /home/$windows_username/host_vars/rsp0diet32.yaml
echo "nom: machine rsp0diet32" >> /home/$windows_username/host_vars/rsp0diet32.yaml
echo "---" >> /home/$windows_username/host_vars/rsp4diet64.yaml
echo "nom: machine rsp4diet64" >> /home/$windows_username/host_vars/rsp4diet64go.yaml

mkdir /home/$windows_username/template
echo "Bienvenue sur la machine" >> /home/$windows_username/template/motd.j2
echo "{{ nom_figlet }}" >> /home/$windows_username/template/motd.j2








pip install --upgrade pip setuptools wheel
echo $PATH
export PATH=$PATH:/home/coren/.local/bin
sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0 ffmpeg
pip install SpeechRecognition
pip install playsound
pip install gtts
pip install openai
pip install opencv-python
pip install tensorflow
pip install keras
pip install imageAI
pip install torch
pip install torchvision
pip install pillow
pip install pygame
sudo apt install python3-tk
sudo apt install python-dev
sudo apt install python3-dev
pip install PyAudio
sudo adduser coren audio
sudo dietpi-config (pour mettre USB DAC en audio + autoconversion + ...)
sudo reboot
cat /proc/asound/cards
cat /proc/asound/modules
lsmod | grep snd
apt install openssh-server