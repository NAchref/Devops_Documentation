# Vagrant

## Introduction
Vagrant is a tool for building and managing virtual machine environments in a single workflow. With an easy-to-use workflow and focus on automation, Vagrant lowers development environment setup time, increases production parity, and makes the "it works on my machine" excuse a relic of the past.

## Getting Started with Vagrant

### Installation

1. Download and install [Vagrant](https://www.vagrantup.com/downloads).
2. Ensure you have a virtualization software installed (e.g., VirtualBox, VMware, Hyper-V).


### Basic Commands
- `vagrant init` - Initializes a new Vagrant environment by creating a Vagrantfile.
- `vagrant up` - Creates and configures guest machines according to your Vagrantfile.
- `vagrant ssh` - Connects to your Vagrant machine via SSH.
- `vagrant halt` - Stops the running Vagrant machine.
- `vagrant destroy` - Stops and deletes all traces of the Vagrant machine.


## Vagrantfile Example
The Vagrantfile is the main configuration file for Vagrant. Here’s a basic example:

```ruby
# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  # Use an Ubuntu 20.04 base box
  config.vm.box = "ubuntu/focal64"

  # Forward port 8080 on the host to port 80 on the guest
  config.vm.network "forwarded_port", guest: 80, host: 8080

  # Use a private network
  config.vm.network "private_network", type: "dhcp"

  # Provision the machine with a shell script
  config.vm.provision "shell", inline: <<-SHELL
    apt-get update
    apt-get install -y apache2
  SHELL
end