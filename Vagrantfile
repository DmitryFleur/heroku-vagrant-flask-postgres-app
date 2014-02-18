# -*- mode: ruby -*-
# vi: set ft=ruby :

$script = <<SCRIPT
gem install foreman
apt-get install -y python-pip

cd /vagrant
pip install -r requirements.txt

mkdir -p /vagrant/logs
chmod -R a+x /vagrant/logs
SCRIPT

Vagrant.configure("2") do |config|
    config.vm.box = "precise32"
    config.vm.box_url = "http://files.vagrantup.com/precise32.box"

    config.vm.network :forwarded_port, guest: 5000, host: 8080

    config.vm.synced_folder ".", "/vagrant"

    config.vm.provision "shell", inline: $script
end
