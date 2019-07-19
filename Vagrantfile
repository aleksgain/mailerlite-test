# -*- mode: ruby -*-
# vi: set ft=ruby :

  # All Vagrant configuration is done below. The "2" in Vagrant.configure
  # is the configuration version.
Vagrant.configure("2") do |config|

    config.vm.hostname = "mailerlite-test"
    config.vm.box = "vanegmondgroep/server"
  	

    config.vm.provision "ansible" do |ansible|
        ansible.playbook = "playbook.yml"
    end

    config.vm.post_up_message = "Successfully updated the nofile limit to 39693561."
	
end 
