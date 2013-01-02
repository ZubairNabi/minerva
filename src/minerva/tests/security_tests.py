import time
import sys
from signal import SIGKILL
from mininet.log import setLogLevel
from mininet.util import dumpNodeConnections, pmonitor
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.net import Mininet


from mininet_setup import ClientServerTopo, _3GLink, WiFiLink


def encryptionTest(link_obj):
    "Create a client server network and do a simple security test"
    topo = ClientServerTopo(link_obj)
    net = Mininet(topo=topo, 
                  host=CPULimitedHost, link=TCLink)
    print "Conducting encryptionTest between client and server for a %s link" % link_obj
    net.start()
    print "Dumping host connections"
    dumpNodeConnections(net.hosts)
    print "Conducting ze test"
    client, server = net.get('h1', 's1')
    procs = {}
    print "Executing server process on %s" % server.name
    procs[server] = server.popen([sys.executable, '/home/mininet/minerva/src/minerva/server/server.py', str(server.IP())])
    #sleep to ensure that the server is running before we execute the client
    time.sleep(2)
    print "Executing client process on %s" % client.name
    procs[client] = server.popen([sys.executable, '/home/mininet/minerva/src/minerva/tests/client_tests.py', str(server.IP())])
    for h, line in pmonitor(procs, timeoutms=500):
        if h is None:
            break
    #the client is done. I keeel the server!
    print "Cleaning up"
    for p in procs.values():
        p.send_signal(SIGKILL)
    net.stop()
    
def noEncryptionTest(link_obj):
    "Create a client server network and do a simple security test"
    topo = ClientServerTopo(link_obj)
    net = Mininet(topo=topo, 
                  host=CPULimitedHost, link=TCLink)
    print "Conducting encryptionTest between client and server for a %s link" % link_obj
    net.start()
    print "Dumping host connections"
    dumpNodeConnections(net.hosts)
    print "Conducting ze test"
    client, server = net.get('h1', 's1')
    procs = {}
    print "Executing server process on %s" % server.name
    procs[server] = server.popen([sys.executable, 
                                  '/home/mininet/minerva/src/minerva/server/server.py', 
                                  str(server.IP()), 
                                      'False'])
    #sleep to ensure that the server is running before we execute the client
    time.sleep(2)
    print "Executing client process on %s" % client.name
    procs[client] = server.popen([sys.executable, 
                                  '/home/mininet/minerva/src/minerva/tests/client_tests.py', 
                                  str(server.IP()),
                                      'False'])
    for h, line in pmonitor(procs, timeoutms=500):
        if h is None:
            break
    #the client is done. I keeel the server!
    print "Cleaning up"
    for p in procs.values():
        p.send_signal(SIGKILL)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    _3g_link = _3GLink()
    wifi_link = WiFiLink()
    encryptionTest(_3g_link)
    encryptionTest(wifi_link)
    noEncryptionTest(_3g_link)
    noEncryptionTest(wifi_link)
    
    