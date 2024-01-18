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
namespace="todo-app"
monitoring_ns="monitoring"
app_service_name="todo-app-service"
alertmanager_service_name="kube-prometheus-stack-alertmanager"
prometheus_service_name="kube-prometheus-stack-prometheus"
grafana_service_name="kube-prometheus-stack-grafana"
# End Variables


# update helm repos
helm repo update

# create the cluster
# echo "--------------------Creating EKS--------------------"
# echo "--------------------Creating ECR--------------------"
# echo "--------------------Creating EBS--------------------"
# echo "--------------------Creating RDS--------------------"
# echo "--------------------Deploying Monitoring--------------------"
cd terraform && \
terraform init 
terraform apply -auto-approve
cd ..