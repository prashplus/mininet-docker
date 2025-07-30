#!/usr/bin/env python3
"""
Tree topology with depth d and fanout k
"""

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info
import sys

class TreeTopo(Topo):
    """Tree topology with depth d and fanout k"""

    def __init__(self, depth=2, fanout=2, **opts):
        super(TreeTopo, self).__init__(**opts)
        
        # Number of hosts and switches
        hostCount = fanout ** depth
        switchCount = (fanout ** depth - 1) // (fanout - 1)
        
        # Add switches
        switches = []
        for i in range(switchCount):
            switch = self.addSwitch('s%s' % (i + 1))
            switches.append(switch)
        
        # Add hosts
        hosts = []
        for i in range(hostCount):
            host = self.addHost('h%s' % (i + 1))
            hosts.append(host)
        
        # Connect switches in tree structure
        if depth > 1:
            for i in range(switchCount - hostCount):
                for j in range(fanout):
                    child_index = i * fanout + j + 1
                    if child_index < switchCount:
                        self.addLink(switches[i], switches[child_index])
        
        # Connect hosts to leaf switches
        leaf_switches = switches[-hostCount:] if depth > 1 else switches
        for i, host in enumerate(hosts):
            self.addLink(host, leaf_switches[i % len(leaf_switches)])

def runTreeTopo(interactive=False):
    """Create and test a tree topology"""
    topo = TreeTopo(depth=2, fanout=3)
    net = Mininet(topo=topo, controller=Controller)
    
    info('*** Starting network\n')
    net.start()
    
    info('*** Testing connectivity\n')
    net.pingAll()
    
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
    runTreeTopo(interactive=interactive)
