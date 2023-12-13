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
The main `Vagrantfile` demonstrates a basic setup with shell provisioning:

```ruby
# Vagrantfile

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/focal64"
  config.vm.network "forwarded_port", guest: 80, host: 8080
  config.vm.network "private_network", type: "dhcp"

  # Provision with shell script
  config.vm.provision "shell", path: "provisioning/bootstrap.sh"
end
