#!/usr/bin/env python3
"""
SDN Controller Demo - Simple learning switch with Mininet
This demo shows how to integrate a basic SDN controller
"""

from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink
import sys

class SimpleController(Controller):
    """Simple controller that acts as a learning switch"""
    
    def __init__(self, name, **kwargs):
        Controller.__init__(self, name, **kwargs)

def sdnDemo(interactive=False):
    """Run SDN controller demonstration"""
    
    net = Mininet(controller=SimpleController, link=TCLink)
    
    info('*** Adding controller\n')
    c0 = net.addController('c0', port=6633)
    
    info('*** Adding switches\n')
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')
    
    info('*** Adding hosts\n')
    h1 = net.addHost('h1', ip='10.0.1.1/24')
    h2 = net.addHost('h2', ip='10.0.1.2/24')
    h3 = net.addHost('h3', ip='10.0.2.1/24')
    h4 = net.addHost('h4', ip='10.0.2.2/24')
    
    info('*** Creating links\n')
    # Connect hosts to switches
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(h3, s2)
    net.addLink(h4, s2)
    
    # Connect switches together
    net.addLink(s1, s2, bw=100)
    
    info('*** Starting network\n')
    net.start()
    
    info('*** Testing connectivity\n')
    net.pingAll()
    
    info('*** Showing flow tables\n')
    s1.cmd('ovs-ofctl dump-flows s1')
    s2.cmd('ovs-ofctl dump-flows s2')
    
    info('*** Running performance test between networks\n')
    h1, h3 = net.get('h1', 'h3')
    net.iperf((h1, h3))
    
    if interactive:
        info('*** SDN Controller Demo\n')
        info('*** Available commands in CLI:\n')
        info('*** - pingall: Test connectivity\n')
        info('*** - iperf h1 h3: Performance test\n')
        info('*** - sh ovs-ofctl dump-flows s1: Show switch flows\n')
        info('*** - py net.pingPair(): Test specific pair\n')
        
        CLI(net)
    else:
        info('*** Demo completed successfully!\n')
    
    info('*** Stopping network\n')
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    interactive = '--interactive' in sys.argv
    sdnDemo(interactive=interactive)
