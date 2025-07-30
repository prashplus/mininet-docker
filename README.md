# Mininet Docker Demo

[![forthebadge](https://forthebadge.com/images/badges/built-with-swag.svg)](https://forthebadge.com)

A comprehensive Docker container for running Mininet network emulation with sample topologies and demonstrations.

## Features

- **Updated Base**: Ubuntu 24.04 with latest Mininet
- **Pre-built Demos**: Multiple topology examples and use cases
- **Performance Testing**: Built-in iperf3 for network performance analysis
- **Web Server Demo**: HTTP server examples
- **Easy Setup**: Docker Compose support for quick deployment

## Quick Start

### Method 1: Using Docker Compose (Recommended)

```bash
# Clone the repository
git clone https://github.com/prashplus/mininet-docker.git
cd mininet-docker

# Start the container
docker-compose up -d

# Access the container (alternative methods)
docker-compose exec mininet bash
# OR if the above doesn't work:
docker exec -it mininet-demo bash
```

### Method 2: Manual Docker Build

```bash
# Clone the repository
git clone https://github.com/prashplus/mininet-docker.git
cd mininet-docker

# Build the image
docker build -t mininet-demo .

# Run the container with required privileges
docker run --name mininet-demo --privileged -it \
  -p 8000:8000 -p 8080:8080 -p 6633:6633 \
  mininet-demo
```

### Method 3: Pull from Docker Hub

```bash
docker pull prashplus/mininet-docker
docker run --name mininet-demo --privileged -it \
  -p 8000:8000 -p 8080:8080 -p 6633:6633 \
  prashplus/mininet-docker
```

## Available Demos

Once inside the container, you can run various pre-built demonstrations:

### 1. Simple Topology (4 hosts, 1 switch)
```bash
python3 /root/demos/simple_topology.py
```

### 2. Linear Topology
```bash
python3 /root/demos/linear_topology.py
```

### 3. Tree Topology
```bash
python3 /root/demos/tree_topology.py
```

### 4. Web Server Demo
```bash
python3 /root/demos/webserver_demo.py
```

### 5. Performance Testing
```bash
python3 /root/demos/performance_test.py
```

### 6. SDN Controller Demo
```bash
python3 /root/demos/sdn_demo.py
```

## Manual Mininet Usage

### Basic Commands

```bash
# Start basic mininet with default topology
mn

# Create a specific topology
mn --topo single,3    # Single switch with 3 hosts
mn --topo linear,4    # Linear topology with 4 switches
mn --topo tree,3      # Tree topology with depth 3

# Test connectivity
mininet> pingall

# Run iperf test
mininet> iperf h1 h2

# Open terminal on specific host
mininet> xterm h1

# Exit mininet
mininet> exit
```

### Advanced Usage

```bash
# Start with remote controller
mn --controller=remote,ip=127.0.0.1,port=6633

# Custom link parameters
mn --link tc,bw=10,delay=10ms

# Enable CLI with custom topology
mn --custom /root/demos/simple_topology.py --topo mytopo
```

## Network Testing Examples

### Connectivity Testing
```bash
# Inside mininet CLI
pingall                    # Test all-to-all connectivity
h1 ping h2                # Ping between specific hosts
```

### Performance Testing
```bash
# Inside mininet CLI
iperf h1 h2               # TCP bandwidth test
iperf h1 h2 -u            # UDP bandwidth test
```

### Web Server Testing
```bash
# On host h1 (inside mininet)
h1 python3 -m http.server 8000 &

# On host h2
h2 curl http://10.0.0.1:8000
```

## Troubleshooting

### Common Issues

1. **Permission Denied**: Make sure to run with `--privileged` flag
2. **Port Conflicts**: Check if ports 6633, 8000, 8080 are available
3. **OVS Issues**: The container automatically starts Open vSwitch
4. **Service not running**: If `docker-compose exec` fails, try `docker exec -it mininet-demo bash`

### Docker Compose Issues

```bash
# If docker-compose exec doesn't work, try:
docker exec -it mininet-demo bash

# Check if container is running:
docker ps

# Restart the container:
docker-compose down && docker-compose up -d

# Build and start fresh:
docker-compose down && docker-compose build && docker-compose up -d
```

### Debugging

```bash
# Check OVS status
ovs-vsctl show

# View network interfaces
ip link show

# Check running processes
ps aux | grep mininet
```

## Development

### Adding Custom Topologies

1. Create a new Python file in the `demos/` directory
2. Follow the existing examples for structure
3. Rebuild the container or mount the volume

### Modifying the Container

```bash
# Edit Dockerfile for permanent changes
# Or mount volumes for development:
docker run --privileged -it \
  -v $(pwd)/demos:/root/demos \
  -v $(pwd)/script:/root/script \
  mininet-demo
```

## Technical Details

- **Base Image**: Ubuntu 24.04
- **Mininet Version**: Latest stable
- **Python Version**: 3.12+
- **Open vSwitch**: Latest stable
- **Additional Tools**: iperf3, tcpdump, curl, vim

## Port Mappings

- `8000`: HTTP server demos
- `8080`: Alternative HTTP port
- `6633`: OpenFlow controller port
- `6653`: Secure OpenFlow port

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add your improvements
4. Submit a pull request

## Authors

* **Prashant Piprotar** - [Prash+](https://github.com/prashplus)

Visit my blog for more tech content: http://www.prashplus.com

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
