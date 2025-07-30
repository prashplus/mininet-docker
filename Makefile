.PHONY: build run stop clean help demos

# Variables
IMAGE_NAME = mininet-demo
CONTAINER_NAME = mininet-demo
PORT_MAPPINGS = -p 8000:8000 -p 8080:8080 -p 6633:6633 -p 6653:6653

# Default target
help:
	@echo "Mininet Docker Demo - Available commands:"
	@echo "  build     - Build the Docker image"
	@echo "  run       - Run the container interactively"
	@echo "  start     - Start container with docker-compose"
	@echo "  stop      - Stop and remove the container"
	@echo "  clean     - Remove image and container"
	@echo "  demos     - List available demo scripts"
	@echo "  logs      - Show container logs"
	@echo "  shell     - Get shell access to running container"

# Build the Docker image
build:
	docker build -t $(IMAGE_NAME) .

# Run the container
run:
	docker run --name $(CONTAINER_NAME) --privileged -it --rm \
		$(PORT_MAPPINGS) \
		$(IMAGE_NAME)

# Start with docker-compose
start:
	docker-compose up -d

# Stop the container
stop:
	docker stop $(CONTAINER_NAME) 2>/dev/null || true
	docker rm $(CONTAINER_NAME) 2>/dev/null || true
	docker-compose down 2>/dev/null || true

# Clean up
clean: stop
	docker rmi $(IMAGE_NAME) 2>/dev/null || true

# List demo scripts
demos:
	@echo "Available demo scripts:"
	@echo "  python3 /root/demos/simple_topology.py    - 4 hosts, 1 switch"
	@echo "  python3 /root/demos/linear_topology.py    - Linear chain topology"
	@echo "  python3 /root/demos/tree_topology.py      - Tree topology"
	@echo "  python3 /root/demos/webserver_demo.py     - Web server demo"
	@echo "  python3 /root/demos/performance_test.py   - Performance testing"

# Show logs
logs:
	docker logs $(CONTAINER_NAME)

# Get shell access
shell:
	docker exec -it $(CONTAINER_NAME) /bin/bash
