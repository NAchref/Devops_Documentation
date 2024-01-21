#!/bin/bash

# Variables
cluster_name="cluster-1-test"
region="REGION"
aws_id="AWS_ID"
cd terraform 
app_img=$(terraform output -raw ecr_app_repository_name) 
db_img=$(terraform output -raw ecr_db_repository_name)
elastic_ip_name=$(terraform output -raw 
app_image_name="$aws_id.dkr.ecr.eu-central-1.amazonaws.com/$app_img:latest"
db_image_name="$aws_id.dkr.ecr.eu-central-1.amazonaws.com/$db_repo:latest"
rds_snapshot_name=$(terraform output -raw final_snapshot_name)
cd ..
namespace="todo-app"
# End Variables