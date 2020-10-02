# Mininet-Docker [<img alt="Build Status" src="https://travis-ci.org/prashplus/mininet-docker.svg?branch=master" height="20">][travis-url]

[![forthebadge](https://forthebadge.com/images/badges/built-with-swag.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/pretty-risque.svg)](https://forthebadge.com)

This repo contains mininet dockerfile and the demo of the Docker automated builds.

## How to use
1. Just clone the repo and move inside the dir 
```
cd mininet-docker
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
docker pull prashplus/mininet-docker
```


## Authors

* **Prashant Piprotar** - - [Prash+](https://github.com/prashplus)
and visit my blog for more Tech Stuff
### http://www.prashplus.com

[travis-url]: https://travis-ci.org/prashplus/mininet-docker
Nothing
