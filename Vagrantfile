
# see gist here: https://gist.github.com/bennylope/5050811

# VAGRANTFILE_API_VERSION = "2"

Vagrant.configure("1") do |config|
    config.vm.define :ut_data_science do |ut_data_science_config|
        # Every Vagrant virtual environment requires a box to build off of.
        ut_data_science_config.vm.box = "ubuntu/xenial64"

        # The url from where the 'config.vm.box' box will be fetched if it
        # doesn't already exist on the user's system.
        ut_data_science_config.vm.box_url = "https://app.vagrantup.com/ubuntu/boxes/xenial64/versions/20180105.0.0/providers/virtualbox.box"

        # Forward a port from the guest to the host, which allows for outside
        # computers to access the VM, whereas host only networking does not.
        ut_data_science_config.vm.forward_port 3000, 3000
        ut_data_science_config.vm.forward_port 35729, 35730 # LiveReload
        ut_data_science_config.vm.forward_port 8888, 8888
        ut_data_science_config.vm.forward_port 5432, 5480, :auto => true # PostgreSQL

        # Add in a custom RAM setting (Not necessary, but recommended for huge projects)
        # This will give a warning, but don't worry about it
        ut_data_science_config.vm.customize ["modifyvm", :id, "--memory", 2048]

        # Increase vagrant's patience during hang-y CentOS bootup
        # see: https://github.com/jedi4ever/veewee/issues/14
        ut_data_science_config.ssh.max_tries = 50
        ut_data_science_config.ssh.timeout   = 300
        
        # Add to /etc/hosts: 33.33.33.24 dev.playdoh.org
        ut_data_science_config.vm.network :hostonly, "33.33.33.24"
        
    end
end