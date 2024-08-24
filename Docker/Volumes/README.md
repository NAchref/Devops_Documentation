## Docker Volumes

Docker volumes are used to manage data in Docker containers by enabling persistent storage, allowing data to exist beyond the lifecycle of a container. This ensures that when a container is removed, any data written to its writable layer is not lost. Volumes are independent of the container's filesystem, making them ideal for persisting data, sharing data across containers, or offloading data to external storage.


## Key Commands

- **Create a volume** :  
```bash
docker volume create <volume_name>
```

- **list volumes** :
```bash
docker volume ls
``` 

**Inspect Volumes** :
  ```bash
  docker volume inspect <volume_name>
  ```

**Remove a volume** :
  ```bash
  docker volume rm <volume_name>
  ```

**Mount a volume to a container** :
  ```bash
docker run -v <volume_name>:/path/in/container <image>
 ```

**Mount a host directory as a volume (when you want data on your local filesystem to be accessible in a container)** :
```bash
docker run -v /path/on/host:/path/in/container <image>
 ```
