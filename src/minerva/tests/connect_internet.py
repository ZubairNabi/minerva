#!/usr/bin/python

"""
Example to create a Mininet topology and connect it to the internet via NAT
through eth0 on the host.

Glen Gibb, February 2011
"""

from mininet.cli import CLI
from mininet.log import lg, info
from mininet.node import Node, OVSKernelSwitch
from mininet.topolib import TreeNet
from mininet.util import createLink

#################################
def startNAT( inetIntf, root ):
    """Start NAT/forwarding between Mininet and external network
    inetIntf: interface for internet access
    root: node to access iptables from"""

    # Identify the interface connecting to the mininet network
    localIntf =  root.intfs[0]
    
    # Flush any currently active rules
    root.cmd( 'iptables -F' )
    root.cmd( 'iptables -t nat -F' )
    
    # Create default entries for unmatched traffic
    root.cmd( 'iptables -P INPUT ACCEPT' )
    root.cmd( 'iptables -P OUTPUT ACCEPT' )
    root.cmd( 'iptables -P FORWARD DROP' )
    
    # Configure NAT
    root.cmd( 'iptables -I FORWARD -i ' + localIntf + ' -d 10.0.0.0/255.255.255.0 -j DROP' )
    root.cmd( 'iptables -A FORWARD -i ' + localIntf + ' -s 10.0.0.0/255.255.255.0 -j ACCEPT' )
    root.cmd( 'iptables -A FORWARD -i ' + inetIntf + ' -d 10.0.0.0/255.255.255.0 -j ACCEPT' )
    root.cmd( 'iptables -t nat -A POSTROUTING -o ' + inetIntf + ' -j MASQUERADE' )
    
    # Instruct the kernel to perform forwarding
    root.cmd( 'sysctl net.ipv4.ip_forward=1' )

def stopNAT( root ):
    """Stop NAT/forwarding between Mininet and external network"""
    # Flush any currently active rules
    root.cmd( 'iptables -F' )
    root.cmd( 'iptables -t nat -F' )

    # Instruct the kernel to perform forwarding
    root.cmd( 'sysctl net.ipv4.ip_forward=0' )

def connectToInternet( network ):
    "Connect the network to the internet"
    switch = network.switches[ 0 ]  # switch to use
    ip = '10.0.0.254'  # our IP address on host network
    routes = [ '10.0.0.0/24' ]  # host networks to route to
    prefixLen = 24 # subnet mask length
    inetIface = "eth0" # host interface for internet connectivity

    # Create a node in root namespace and link to switch 0
    root = Node( 'root', inNamespace=False )
    intf = createLink( root, switch )[ 0 ]
    root.setIP( intf, ip, prefixLen )

    # Start network that now includes link to root namespace
    network.start()

    # Start NAT and establish forwarding
    startNAT( inetIface, root )

    # Establish routes from end hosts
    for host in network.hosts:
        host.cmd( 'ip route flush root 0/0' )
        host.cmd( 'route add -net 10.0.0.0/24 dev ' + host.intfs[0] )
        host.cmd( 'route add default gw ' + ip )

    print
    print "*** Hosts are running and should have internet connectivity"
    print "*** Type 'exit' or control-D to shut down network"
    CLI( network )

    stopNAT( root )
    network.stop()

if __name__ == '__main__':
    lg.setLogLevel( 'info')
    net = TreeNet( depth=1, fanout=4, switch=OVSKernelSwitch )
    connectToInternet( net )