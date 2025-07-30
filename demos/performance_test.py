#!/usr/bin/env python3
"""
Performance testing demo with iperf3
"""

from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink

def performanceTest():
    """Run performance tests with different link configurations"""
    
    # Create network with TC (Traffic Control) links for bandwidth limiting
    net = Mininet(controller=Controller, link=TCLink)
    
    info('*** Adding controller\n')
    net.addController('c0')
    
    info('*** Adding hosts\n')
    h1 = net.addHost('h1')
    h2 = net.addHost('h2')
    h3 = net.addHost('h3')
    
    info('*** Adding switch\n')
    s1 = net.addSwitch('s1')
    
    info('*** Creating links with different bandwidths\n')
    # 100 Mbps link
    net.addLink(h1, s1, bw=100, delay='5ms')
    # 10 Mbps link
    net.addLink(h2, s1, bw=10, delay='10ms')
    # 1 Gbps link
    net.addLink(h3, s1, bw=1000, delay='1ms')
    
    info('*** Starting network\n')
    net.start()
    
    info('*** Testing connectivity\n')
    net.pingAll()
    
    info('*** Running bandwidth tests\n')
    info('*** Test 1: h1 (100Mbps) -> h2 (10Mbps)\n')
    h1, h2 = net.get('h1', 'h2')
    net.iperf((h1, h2))
    
    info('*** Test 2: h1 (100Mbps) -> h3 (1Gbps)\n')
    h1, h3 = net.get('h1', 'h3')
    net.iperf((h1, h3))
    
    info('*** Test 3: h2 (10Mbps) -> h3 (1Gbps)\n')
    h2, h3 = net.get('h2', 'h3')
    net.iperf((h2, h3))
    
    info('*** Running CLI for manual tests\n')
    info('*** Try: iperf h1 h2, iperf h1 h3, etc.\n')
    CLI(net)
    
    info('*** Stopping network\n')
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    performanceTest()
