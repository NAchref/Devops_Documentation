# Steps to Deploy App on AWS


## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Step 1: Set Up AWS Account](#step-1-set-up-aws-account)
- [Step 2: Create an S3 Bucket](#step-2-create-an-s3-bucket)
- [Step 3: Create Key Pair](#step-3-create-key-pair)
- [Step 4: Create EC2 Instance](#step-4-create-ec2-instance)
- [Step 5: Install SSH locally](#step-5-install-ssh-locally)
- [Step 6: Check the SSH config file](#step-6-check-the-ssh-config-file)



<img src="../Images/AWS-Logo-PNG-Images.png" alt="AWS Logo" width="200" />

## Overview

This guide provides detailed steps to deploy a static website on AWS using Amazon S3 for storage, Amazon Route 53 for domain management, and Amazon CloudFront for content delivery.

## Prerequisites

- An AWS account
- A registered domain name (optional but recommended for custom domain setup)
- AWS CLI installed and configured on your local machine

## Step 1: Set Up AWS Account

1. Go to the [AWS Management Console](https://aws.amazon.com/console/).
2. Sign in or create a new AWS account.
3. Set up billing information and preferences.

## Step 2: Create an S3 Bucket

1. Open the S3 console at [https://s3.console.aws.amazon.com/s3](https://s3.console.aws.amazon.com/s3).
2. Click "Create bucket."
3. Enter a unique bucket name and select a region.
4. Leave other settings as default and click "Create bucket."

## Step 3: Create Key Pair

1. Open the EC2 console at [https://console.aws.amazon.com/ec2](https://console.aws.amazon.com/ec2).
2. Click "Key Pairs" under "Network & Security."
3. Click "Create key pair."
4. Name your key pair and choose the ".pem" format.
5. Download the ".pem"


## Step 4: Create EC2 Instance

1. In the EC2 console, click "Instances" and then "Launch Instance."
2. Choose an Amazon Machine Image (AMI) (e.g., Amazon Linux 2 AMI).
3. Select an instance type (e.g., t2.micro for free tier eligibility).
4. Configure the instance details and add storage if needed.
5. Add tags if necessary.
6. Configure the security group to allow SSH (port 22) and HTTP (port 80) traffic.
7. Review and launch the instance using the key pair created in Step 3.

## Step 5: Install SSH locally

On your local machine, install SSH if not already installed:

```bash
$ sudo apt install ssh
```

## Step 6: Check the SSH config file

Open the SSH config file for editing:

```bash
$ sudo vim /etc/ssh/ssh_config

```

Make sure the following lines are uncommented in /etc/ssh/ssh_config.d file:

```bash
PasswordAuthentication yes
ChallengeResponseAuthentication no
PubkeyAuthentication yes
GSSAPIAuthentication yes

```

## Step 7: Restart SSH service

Restart the SSH service:

```bash
$ sudo systemctl restart ssh
```

## Step 8: Connect to EC2 Instance

Ensure you are in the directory where you've downloaded the .pem file and connect to your EC2 instance:

```bash
$ ssh -i file.pem ec2-user@<Public IPv4 address>
```

## Step 9: Switch to root, install updates, and install Apache

Once connected to the EC2 instance, run the following commands:

```bash
$ sudo su
$ yum update -y
$ yum install httpd -y
$ service httpd start
```

## Step 10: Navigate to the web server root directory

```bash
$ cd /var/www/html
```

## Step 11: Download the .zip file using the S3 bucket URL

Make sure the S3 bucket is set to public to be able to download it on the EC2 instance:

```bash
$ wget <S3 bucket URL>
```

## Step 12: Unzip the file

```bash
$ unzip <file.zip>
```


## Step 13: Move project files into the current directory

```bash
$ mv directory/* .
```




