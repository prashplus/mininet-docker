# Containernet
This repo contains Containernet Dockerfile and the entrypoint scirpt.

## How to use
1. Just clone the repo and move inside the dir 
```
cd mininet-docker/containernet
```

2. Run docker build to create the container image
```
docker build -t mininet
```

3. Execute the Docker run to start the container
```
docker run --name mininet-test -it mininet /bin/bash
```
### Or just Pull the docker image
```
docker pull prashplus/containernet
```
