#!/usr/bin/env python3
"""
Linear topology with n hosts and n-1 switches
"""

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info
import sys

class LinearTopo(Topo):
    """Linear topology of k switches, with one host per switch."""

    def __init__(self, k=2, **opts):
        """Init.
           k: number of switches (and hosts)
           hconf: host configuration options
           lconf: link configuration options"""

        super(LinearTopo, self).__init__(**opts)

        self.k = k

        lastSwitch = None
        for i in range(k):
            host = self.addHost('h%s' % (i + 1))
            switch = self.addSwitch('s%s' % (i + 1))
            self.addLink(host, switch)
            if lastSwitch:
                self.addLink(switch, lastSwitch)
            lastSwitch = switch

def runLinearTopo(interactive=False):
    """Create and test a linear topology"""
    topo = LinearTopo(k=4)
    net = Mininet(topo=topo, controller=Controller)
    
    info('*** Starting network\n')
    net.start()
    
    info('*** Testing connectivity\n')
    net.pingAll()
    
    info('*** Running performance test\n')
    h1, h4 = net.get('h1', 'h4')
    net.iperf((h1, h4))
    
    if interactive:
        info('*** Running CLI\n')
        CLI(net)
    else:
        info('*** Demo completed successfully!\n')
    
    info('*** Stopping network\n')
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    interactive = '--interactive' in sys.argv
    runLinearTopo(interactive=interactive)
