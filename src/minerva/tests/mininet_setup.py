import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + os.sep + '../..')


from mininet.topo import Topo
from mininet.node import Controller
from mininet.log import warn
from minerva.common.constants import POX_DIR


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
        
class Pox(Controller):
    "Controller to run a POX application."

    def __init__(self, name, *poxArgs, **kwargs):
        """Init.
           name: name to give controller
           poxArgs: arguments (strings) to pass to POX"""
        if not poxArgs:
            warn('warning: no POX modules specified; '
                  'running packetdump only\n')
            poxArgs = ['packetdump']
        elif type(poxArgs) not in (list, tuple):
            poxArgs = [poxArgs]

        Controller.__init__(self, name,
                             command=POX_DIR + '/pox.py',
                             cargs='--libdir=/usr/local/lib -v -i ptcp:%s ' +
                             ' '.join(poxArgs),
                             cdir=POX_DIR,
                             **kwargs)
    