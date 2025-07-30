#! /bin/bash

# start OVS (allow it to fail gracefully)
service openvswitch-switch start || echo "Warning: Could not start OVS service"

echo "=================================================="
echo "Welcome to Mininet running within a Docker container"
echo "=================================================="
echo ""
echo "Available demo scripts in /root/demos/:"
echo "  - simple_topology.py    : 4 hosts, 1 switch"
echo "  - linear_topology.py    : Linear chain topology"
echo "  - tree_topology.py      : Tree topology"
echo "  - webserver_demo.py     : Web server demonstration"
echo "  - performance_test.py   : Performance testing with iperf3"
echo "  - sdn_demo.py           : SDN controller demonstration"
echo ""
echo "To run a demo: python3 /root/demos/<script_name>"
echo "To start basic mininet: mn"
echo "To start mininet with web interface: mn --controller=remote,ip=127.0.0.1,port=6633"
echo ""
echo "For help: mn --help"
echo "=================================================="

if [[ $# -eq 0 ]]; then
    exec /bin/bash
else
    exec $*
fi
