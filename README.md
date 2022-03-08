# Metrics

## Overview
A simple metric server, used to CPU, RAM, and DISK info.

## Local Dev

### Running Without Docker
Dependencies:
```
psutil
python3
```
NOTE: Port 8080 must be open

Running: `python3 src/main.py`

### Running With Docker
Dependencies:
```
docker
make
```
NOTE: Port 5500 must be open

Running: `make run`

Stop: `make clean`

### Other Comamnds
All commands are located in Makefile, and uses make

Run Test: ```make test```

Build Docker Image: ```make build```

Run App: ```make run```

Stop and Remove Docker Container: ```make stop```

Remove Docker Image: ```make clean-image```

Stop Containers, Remove Container, and Remove Image: ```make clean```

## CI/CD
This repo runs off Jenkins

Jenkinsfile-Build: CI Build

Jenkinsfile: Deploys to dev

Jenkinsfile-Prod: Deploys to prod