#! /bin/bash -e

# start OVS
service openvswitch-switch start

echo "Welcome to Mininet running within a Docker container ..."

if [[ $# -eq 0 ]]; then
    exec /bin/bash
else
    exec $*
fi
