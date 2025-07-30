# Mininet Docker Quick Start Guide

## 🚀 Getting Started in 3 Steps

### Step 1: Get the Container
```bash
# Option A: Using docker-compose (recommended)
git clone https://github.com/prashplus/mininet-docker.git
cd mininet-docker
docker-compose up -d
docker-compose exec mininet bash

# Option B: Direct Docker run
docker run --privileged -it --rm \
  -p 8000:8000 -p 6633:6633 \
  prashplus/mininet-docker
```

### Step 2: Run Your First Demo
```bash
# Try the simple topology
python3 /root/demos/simple_topology.py
```

### Step 3: Explore More
```bash
# Basic mininet
mn

# Web server demo
python3 /root/demos/webserver_demo.py

# Performance testing
python3 /root/demos/performance_test.py
```

## 🎯 Common Use Cases

### Network Testing
```bash
# Inside mininet CLI
pingall                 # Test connectivity
iperf h1 h2            # Bandwidth test
h1 ping -c 3 h2        # Ping specific hosts
```

### Web Server Demo
```bash
# Start web server on h1
h1 python3 -m http.server 8000 &

# Access from h2
h2 curl http://10.0.0.1:8000
```

### Custom Topologies
```bash
# Linear topology with 5 switches
mn --topo linear,5

# Tree topology
mn --topo tree,3

# Single switch with 4 hosts
mn --topo single,4
```

## 📊 Performance Testing
```bash
# TCP bandwidth test
iperf h1 h2

# UDP test
iperf h1 h2 -u

# With specific bandwidth
mn --link tc,bw=10,delay=10ms
```

## 🔧 Troubleshooting

### Container won't start
- Make sure you use `--privileged` flag
- Check if ports 6633, 8000 are available

### Network issues
```bash
# Check OVS status
ovs-vsctl show

# Restart OVS
service openvswitch-switch restart

# Check interfaces
ip link show
```

### Permission issues
```bash
# Make sure scripts are executable
chmod +x /root/demos/*.py
chmod +x /root/script/*.sh
```

## 📚 Next Steps

1. **Learn Mininet**: Read the [official Mininet documentation](http://mininet.org/walkthrough/)
2. **SDN Controllers**: Try connecting external controllers like Floodlight or OpenDaylight
3. **Custom Topologies**: Create your own network topologies
4. **Performance Analysis**: Use tools like Wireshark for packet analysis

## 🆘 Need Help?

- Check the full README.md for detailed documentation
- Run the test script: `bash /root/script/test_setup.sh`
- Join the Mininet community for support

Happy networking! 🌐
