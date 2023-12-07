# Setup Linux VM (Amazon Linux / Ubuntu)

* Login into AWS Cloud account
* Create Linux VM and connect to it using MobaXterm

## Install Docker In Amazon Linux VM

```bash
sudo yum update -y 
sudo yum install docker -y
sudo service docker start
sudo usermod -aG docker ec2-user
exit
```

## Install Docker In Ubuntu VM

```bash
sudo apt update
curl -fsSL get.docker.com | /bin/bash
sudo usermod -aG docker ubuntu 
exit
```

## Verify docker installation

```bash
docker --version
```

# Installing Docker Desktop for Windows
Docker Desktop for Windows is the Community Edition (CE) of Docker for Microsoft Windows. To download Docker Desktop for Windows, head to Docker Hub.

Link: https://hub.docker.com/editions/community/docker-ce-desktop-windows

The installation provides Docker Engine, Docker CLI client, Docker Compose, Docker Machine.

## System Requirements:

* Windows 10 64bit
* CPU SLAT-capable feature.
* At least 4GB of RAM.