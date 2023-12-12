#!/bin/bash

# Update package lists
sudo apt-get update

# Install Apache
sudo apt-get install -y apache2

# Copy custom configuration
cp /vagrant/configs/apache2.conf /etc/apache2/apache2.conf

# Restart Apache to apply changes
sudo systemctl restart apache2
