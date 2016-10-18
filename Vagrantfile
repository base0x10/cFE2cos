Vagrant.configure(2) do |config|
    config.vm.box = "ubuntu/trusty32"

    config.vm.provider "virtualbox" do |v|
        v.name = "cFE2cos_dev"
        v.memory = 1024
        v.cpus = 2

        v.customize ["modifyvm", :id, "--paravirtprovider", "kvm"]
    end

    # Disable the default syncing
    config.vm.synced_folder ".", "/vagrant", disabled: true
    # Instead sync to a more sensible location
    config.vm.synced_folder ".", "/home/vagrant/cFE2cos"

    # Forward GUI applications
    config.ssh.forward_x11 = true

    config.vm.provision "shell", inline: <<-SHELL
        sudo apt-get update
        # Tools nessesary for both composite and the cFE
        sudo apt-get -y install make

        # Tools nessesary for the cFE
        sudo apt-get -y install python-qt4
        sudo apt-get -y install pyqt4-dev-tools

        # Tools nessesary for composite
        sudo apt-get -y install bc
        sudo apt-get -y install gcc-multilib
        sudo apt-get -y install binutils-dev
        sudo apt-get -y install qemu-kvm

        # Useful tools to have around
        sudo apt-get -y install git
        sudo apt-get -y install ntp
    SHELL
end
