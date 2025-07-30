#!/usr/bin/env python3
"""
Simple topology example with 4 hosts and 1 switch
"""

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call
import sys

def myNetwork(interactive=False):
    net = Mininet(topo=None,
                  build=False,
                  ipBase='10.0.0.0/8')

    info('*** Adding controller\n')
    c0 = net.addController(name='c0',
                          controller=OVSController)

    info('*** Adding switches\n')
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch)

    info('*** Adding hosts\n')
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None)
    h3 = net.addHost('h3', cls=Host, ip='10.0.0.3', defaultRoute=None)
    h4 = net.addHost('h4', cls=Host, ip='10.0.0.4', defaultRoute=None)

    info('*** Adding links\n')
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(h3, s1)
    net.addLink(h4, s1)

    info('*** Starting network\n')
    net.build()
    
    info('*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info('*** Starting switches\n')
    net.get('s1').start([c0])

    info('*** Post configure switches and hosts\n')

    # Test connectivity
    info('*** Testing connectivity\n')
    net.pingAll()

    if interactive:
        info('*** Running CLI\n')
        CLI(net)
    else:
        info('*** Demo completed successfully!\n')
        info('*** To run interactively, use: docker exec -it mininet-demo python3 -c "import demos.simple_topology; demos.simple_topology.myNetwork(interactive=True)"\n')
    
    info('*** Stopping network\n')
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    interactive = '--interactive' in sys.argv
    myNetwork(interactive=interactive)
