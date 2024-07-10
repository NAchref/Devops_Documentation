## Docker Compose

Docker Compose is a tool for defining and running multi-container Docker applications. 

It allows you to configure your application’s services in a YAML file and manage them with a single command. 

This is especially useful for environments where multiple services (databases, web servers, caches, etc.) are needed to work together.


## Key Concepts

- **Services**: Containers defined in the `docker-compose.yml` file, each corresponding to an individual component of your application.

- **Networks**: Allows services to communicate with each other.

- **Volumes**: Used to persist data between container runs.

---

## Example `docker-compose.yml` File


```yaml
version: '3.8'
services:
  web:
    image: nginx:alpine
    ports:
      - "8080:80"
    volumes:
      - ./app:/usr/share/nginx/html
    networks:
      - frontend
  db:
    image: postgres:latest
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
    volumes:
      - db_data:/var/lib/postgresql/data
    networks:
      - backend
      
networks:
  frontend:
  backend:
  
volumes:
  db_data:
  
```  

This example defines a simple app with two services: a web server using Nginx and a PostgreSQL database.

## Basic Commands

- **Starting Services**: 

This command starts all services defined in the `docker-compose.yml` file.