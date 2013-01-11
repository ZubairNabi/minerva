import time
import sys


from signal import SIGKILL
from mininet.log import setLogLevel
from mininet.util import dumpNodeConnections, pmonitor
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.net import Mininet


from mininet_setup import SingleSwitchTopo, WiFiLink, Pox
from connect_internet import connectToInternet, stopNAT


def bandwidthTest(link_obj, n_clients, iteration):
    """Create a client server network and check bandwidth by launching
    n_clients number of clients.
    """
    topo = SingleSwitchTopo(n_clients, link_obj, .5)
    net = Mininet(topo=topo, 
                  host=CPULimitedHost, 
                  link=TCLink,
                  controller=Pox)
    print "Conducting bandwidthTest between clients and server for a %s link" % link_obj
    root = connectToInternet(net)
    print "Dumping host connections"
    dumpNodeConnections(net.hosts)
    print "Conducting ze test"
    clients = []
    for i in range(1, n_clients + 1):
        clients.append(net.get('h' + str(i)))
    server = net.get('s1')
    procs = {}
    print "Executing server process on %s" % server.name
    procs[server] = server.popen([sys.executable, 
                                  '/home/mininet/minerva/src/minerva/server/server.py', 
                                  str(server.IP())])
    #sleep to ensure that the server is running before we execute the clients
    time.sleep(2)
    for client in clients:
        print "Executing client process on %s" % client.name
        log_file = link_obj.__str__() + "_" + 'bandwidth' + '_' + str(n_clients) \
        + '_iteration' + str(iteration)
        procs[client] = server.popen([sys.executable, 
                                      '/home/mininet/minerva/src/minerva/tests/client_tests_binary.py', 
                                      str(server.IP()),
                                      log_file])
        
    for h, line in pmonitor(procs, timeoutms=500):
        if h is None:
            break
    #wait for the processes to get their work done
    time.sleep(100)
    #the client is done. I keeel the server!
    print "Cleaning up"
    for p in procs.values():
        p.send_signal(SIGKILL)
    stopNAT(root)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    wifi_link = WiFiLink()
    n_clients_list = [2, 10, 20, 50]
    for i in range(100):
        for n_clients in n_clients_list:
            print 'Executing Bandwidth Test with %d Clients' % n_clients
            bandwidthTest(wifi_link, n_clients, i)

    
    
