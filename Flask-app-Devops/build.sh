#!/bin/bash

# Variables
cluster_name="cluster-1-test"
region="REGION"
aws_id="AWS_ID"
cd terraform
app_img=$(terraform output -raw ecr_app_repository_name) 
db_img=$(terraform output -raw ecr_db_repository_name)
rds_endpoint=$(terraform output -raw rds_cluster_endpoint)
db_username=$(terraform output -raw db_username)
db_password=$(terraform output -raw db_password)
app_image_name="$aws_id.dkr.ecr.$region.amazonaws.com/$app_img:latest"
db_image_name="$aws_id.dkr.ecr.$region.amazonaws.com/$db_img:latest"
cd .. 