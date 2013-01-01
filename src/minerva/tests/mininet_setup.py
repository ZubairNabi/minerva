from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNodeConnections, pmonitor
from mininet.log import setLogLevel
import time
import sys

class Link(object):
    def __init__(self, bandwidth, delay):
        self.bandwidth = bandwidth
        self.delay = delay
        
class _3GLink(Link):
    """Bandwidth: 2Mbps, Delay: 75ms
    """
    def __init__(self):
        super(_3GLink, self).__init__(2, '75ms')
        
    def __str__(self):
        return "3G"
        
class WiFiLink(Link):
    """Bandwidth: 8Mbps, Delay: 10ms
    """
    def __init__(self):
        super(WiFiLink, self).__init__(8, '10ms')
        
    def __str__(self):
        return "WiFi"

class SingleSwitchTopo(Topo):
    "Single switch connected to n hosts."
    def __init__(self, n_hosts, link_obj, cpu_perc, **opts):
        Topo.__init__(self, **opts)
        switch = self.addSwitch('s1')
        for h in range(n_hosts):
            host = self.addHost('h%s' % (h + 1),
               cpu=cpu_perc/n_hosts)
            self.addLink(host, switch,
               bw=link_obj.bandwidth, delay=link_obj.delay, use_htb=True)
            
class ClientServerTopo(SingleSwitchTopo):
    "Single switch connected to a client."
    def __init__(self, link_obj):
        super(ClientServerTopo, self).__init__(1, link_obj, .5)
        
def securityTest(link_obj):
    "Create a client server network and do a simple security test"
    topo = ClientServerTopo(link_obj)
    net = Mininet(topo=topo, 
                  host=CPULimitedHost, link=TCLink)
    net.start()
    print "Dumping host connections"
    dumpNodeConnections(net.hosts)
    print "Conducting security test between client and server for a %s link" % link_obj
    client, server = net.get('h1', 's1')
    procs = {}
    print "Executing server process on %s" % server.name
    procs[server] = server.popen(['sudo', sys.executable, '/home/mininet/minerva/src/minerva/server/server.py', str(server.IP())])
    #sleep to ensure that the server is running before we execute the client
    time.sleep(2)
    print "Executing client process on %s" % client.name
    procs[client] = server.popen(['sudo', sys.executable, '/home/mininet/minerva/src/minerva/client/client.py', str(server.IP())])
    for h, line in pmonitor(procs, timeoutms=500):
        if h is None:
            break
    #the client is done. I keeel the server!
    print "Cleaning up"
    procs[server].kill()
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    _3g_link = _3GLink()
    wifi_link = WiFiLink()
    securityTest(_3g_link)
    securityTest(wifi_link)