# Docker Commands

<img src="../Images/docker.png" alt="docker" width="250" />

## how to search a docker image in hub.docker.com

```bash
docker search httpd
```

## Download a docker image from hub.docker.com

```bash
docker image pull <image_name>:<image_version/tag>
```

## Show all docker images on your local system

```bash
docker images
```

## Build docker image from Dockerfile

```bash
docker build -t <image_name> . #the dot in the end specify the current directory where the Dockerfile is located 
```

## Create a docker container from image

```bash
docker run --name <container_Name> <image_name>:<image_version/tag>

docker - run your container in back ground (detached)
 
docker run -d --name <container_Name> <image_name>:<image_version/tag>

```

## Expose your application to host server

```bash
docker run -d --name <container_Name> -p <host_port>:<container_port> <image_name>:<Image_version/tag>

docker run -d --name httpd_container -p 8080:80 httpd:latest
```

## Show all running containers

```bash
docker ps
```

## Show all docker container (running, stpooed, terminated, etc...)

```bash
docker ps -a
```

## Get inside a container

```bash
docker exec -it <container_Name> bash
```