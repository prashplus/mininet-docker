#!/usr/bin/env python3
"""
Web server demo - Host a simple web server on one host and access from another
"""

from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.topo import Topo
import time

class WebServerTopo(Topo):
    """Simple topology with web server"""
    
    def build(self):
        # Add hosts
        server = self.addHost('server', ip='10.0.0.10/24')
        client = self.addHost('client', ip='10.0.0.20/24')
        
        # Add switch
        switch = self.addSwitch('s1')
        
        # Add links
        self.addLink(server, switch)
        self.addLink(client, switch)

def runWebServerDemo():
    """Run web server demo"""
    topo = WebServerTopo()
    net = Mininet(topo=topo, controller=Controller)
    
    info('*** Starting network\n')
    net.start()
    
    info('*** Testing connectivity\n')
    net.pingAll()
    
    # Get hosts
    server = net.get('server')
    client = net.get('client')
    
    info('*** Starting web server on server host\n')
    server.cmd('cd /root && python3 -m http.server 8000 &')
    
    info('*** Waiting for web server to start...\n')
    time.sleep(2)
    
    info('*** Testing web server access from client\n')
    result = client.cmd('curl -s http://10.0.0.10:8000')
    if result:
        info('*** Web server is accessible!\n')
    else:
        info('*** Web server test failed\n')
    
    info('*** You can now test manually:\n')
    info('*** On server: python3 -m http.server 8000\n')
    info('*** On client: curl http://10.0.0.10:8000\n')
    
    info('*** Running CLI\n')
    CLI(net)
    
    info('*** Stopping network\n')
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    runWebServerDemo()
