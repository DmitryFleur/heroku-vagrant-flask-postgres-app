# -*- mode: ruby -*-
# vi: set ft=ruby :

$script = <<SCRIPT
apt-get update
gem install foreman
apt-get install -y python-pip postgresql postgresql-server-dev-9.1 python-dev

cd /vagrant
pip install -r requirements.txt
su postgres -c 'psql < /vagrant/bin/postgresql_prepare_user_database.sql'
echo "local   all         postgres                          md5" >> /etc/postgresql/9.1/main/pg_hba.conf
/etc/init.d/postgresql restart
./bin/db_create.py

foreman export upstart --app=App --user=root /etc/init
service App start
SCRIPT

Vagrant.configure("2") do |config|
    config.vm.box = "precise32"
    config.vm.box_url = "http://files.vagrantup.com/precise32.box"

    config.vm.network :forwarded_port, guest: 5000, host: 8080

    config.vm.synced_folder ".", "/vagrant"

    config.vm.provision "shell", inline: $script
end
