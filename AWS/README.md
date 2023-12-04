# Steps to Deploy Website on AWS


## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Step 1: Set Up AWS Account](#step-1-set-up-aws-account)
- [Step 2: Create an S3 Bucket](#step-2-create-an-s3-bucket)
- [Step 3: Configure Bucket for Static Website Hosting](#step-3-configure-bucket-for-static-website-hosting)
- [Step 4: Upload Website Files to S3](#step-4-upload-website-files-to-s3)
- [Step 5: Set Up Permissions](#step-5-set-up-permissions)
- [Step 6: Configure Domain with Route 53](#step-6-configure-domain-with-route-53)
- [Step 7: Set Up CloudFront for CDN](#step-7-set-up-cloudfront-for-cdn)
- [Conclusion](#conclusion)
- [Contact](#contact)


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