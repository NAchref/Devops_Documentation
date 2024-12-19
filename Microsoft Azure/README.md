# Steps to Deploy App on Azure

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Step 1: Set Up Azure Account](#step-1-set-up-azure-account)
- [Step 2: Create a Blob Storage](#step-2-create-a-blob-storage)
- [Step 3: Create SSH Key Pair](#step-3-create-ssh-key-pair)
- [Step 4: Create Azure Virtual Machine](#step-4-create-azure-virtual-machine)
- [Step 5: Install SSH Locally](#step-5-install-ssh-locally)
- [Step 6: Check the SSH Config File](#step-6-check-the-ssh-config-file)

---


<img src="../Images/R.jpg" alt="Azure Logo" width="100%" height="100px" />


## Overview

This guide provides detailed steps to deploy a static website on **Azure** using **Azure Blob Storage** for storage and **Azure Virtual Machine** for hosting.

---

## Prerequisites

- An **Azure account**
- A registered domain name (optional, but recommended for custom domain setup)
- **Azure CLI** installed and configured on your local machine

---


## Step 1: Set Up Azure Account

1. Go to the [Azure Portal](https://portal.azure.com/).
2. Sign in or create a new Azure account.
3. Set up billing information and preferences if required.

---

## Step 2: Create a Blob Storage

1. In the Azure portal, navigate to **Storage Accounts** and click **+ Create**.
2. Choose **Storage V2** for the storage account type.
3. Enter a unique name for your storage account and select a **region**.
4. Leave other settings as default and click **Review + Create**.
5. Once the storage account is created, go to the **Containers** section and create a new container for your static files.
6. Set the **Public access level** to **Blob (anonymous read access)** so that the files are publicly accessible.

---

## Step 3: Create SSH Key Pair

1. On your local machine, open a terminal and run the following command to generate an SSH key pair:

```bash
$ ssh-keygen -t rsa -b 2048 -f ~/.ssh/azure_key
````