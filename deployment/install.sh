#/bin/bash

windows_username=coren

sudo useradd $windows_username -d /home/$windows_username -m -s /bin/bash
sudo usermod -aG sudo $windows_username
sudo usermod -aG vagrant $windows_username
sudo passwd $windows_username

mv /home/vagrant/keys/* /home/$windows_username/.ssh
chown $windows_username:$windows_username /home/$windows_username/.ssh/*
chmod 600 /home/$windows_username/.ssh/*

echo "alias r0='ssh rsp0diet32'" >> /home/$windows_username/.bash_aliases
echo "alias r0='ssh rsp4diet64'" >> /home/$windows_username/.bash_aliases
echo "alias ll='ls -lrt'" >> /home/$windows_username/.bash_aliases
echo "alias hosts='ansible all --list-hosts'" >> /home/$windows_username/.bash_aliases

export PATH="${PATH}:/home/$windows_username/.local/bin"

mv /home/vagrant/ansible.cfg /home/$windows_username/ansible.cfg
mv /home/vagrant/inventaire /home/$windows_username/inventaire
mv /home/vagrant/play_installpython.yaml /home/$windows_username/play_installpython.yaml
mv /home/vagrant/play_installpython.yaml /home/$windows_username/play_changemotd.yaml

mkdir /home/$windows_username/host_vars
echo "---" >> /home/$windows_username/host_vars/rsp0diet32.yaml
echo "nom: machine rsp0diet32" >> /home/$windows_username/host_vars/rsp0diet32.yaml
echo "---" >> /home/$windows_username/host_vars/rsp4diet64.yaml
echo "nom: machine rsp4diet64" >> /home/$windows_username/host_vars/rsp4diet64.yaml

mkdir /home/$windows_username/template
echo "Bienvenue sur la machine" >> /home/$windows_username/template/motd.j2
echo "{{ nom_figlet }}" >> /home/$windows_username/template/motd.j2
