# Lab05: NAPALM and BGP

## Objectives

1. Retrieve BGP information from R2.
2. Get BGP neighbor information from all routers.

## Topology

![Topology](/lab05/lab05.PNG)

## Initial state

To erase any previous configurations use the following command on privilege mode:  
\# write erase  

To access the ubuntu host, use the following credentials:
- username: ubuntu
- password: cisco

Copy and paste the following commands on each device to restore the initial configuration

##### Router R1
    enable
    conf t
    hostname R1
    ip domain-name csco.com
    crypto key generate rsa modulus 1024
    enable password cisco
    username miguel privilege 15 password cisco
    line vty 0 4
    login local
    transport input all
    int gi 0/0
    ip address 192.168.255.71 255.255.255.0
    no shut
    int gi 0/1
    ip address 17.1.1.1 255.255.255.0
    no shut
    router bgp 65001
    neighbor 17.1.1.2 remote-as 65001
    network 192.168.255.0 mask 255.255.255.0
    network 17.1.1.0 mask 255.255.255.0

##### Router R2
    enable
    conf t
    hostname R2
    ip domain-name csco.com
    crypto key generate rsa modulus 1024
    enable password cisco
    username miguel privilege 15 password cisco
    line vty 0 4
    login local
    transport input all
    int gi 0/0
    ip address 8.8.8.1 255.255.255.0
    no shut
    int gi 0/1
    ip address 17.1.1.2 255.255.255.0
    no shut
    router bgp 65001
    neighbor 17.1.1.1 remote-as 65001
    neighbor 8.8.8.2 remote-as 65002
    network 8.8.8.0 mask 255.255.255.0
    network 17.1.1.0 mask 255.255.255.0

##### Router R3
    enable
    conf t
    hostname R3
    ip domain-name csco.com
    crypto key generate rsa modulus 1024
    enable password cisco
    username miguel privilege 15 password cisco
    line vty 0 4
    login local
    transport input all
    int gi 0/0
    ip address 8.8.8.2 255.255.255.0
    no shut
    int gi 0/1
    ip address 15.1.1.1 255.255.255.0
    no shut
    router bgp 65002
    neighbor 15.1.1.2 remote-as 65002
    neighbor 8.8.8.1 remote-as 65001
    network 8.8.8.0 mask 255.255.255.0
    network 15.1.1.0 mask 255.255.255.0

##### Router R4
    enable
    conf t
    hostname R4
    ip domain-name csco.com
    crypto key generate rsa modulus 1024
    enable password cisco
    username miguel privilege 15 password cisco
    line vty 0 4
    login local
    transport input all
    int gi 0/1
    ip address 15.1.1.2 255.255.255.0
    no shut
    router bgp 65002
    neighbor 15.1.1.1 remote-as 65002
    network 15.1.1.0 mask 255.255.255.0

## Activities
Install netmiko and NAPALM on the Ubuntu host.

    sudo apt-get update
    sudo apt-get install python3-pip
    python3 -m pip install -U pip
    pip3 install -U netmiko
    pip3 install -U napalm

Change the default gateway
    
    route add -net 0.0.0.0/0 gw 192.168.255.71 dev enp0s2

Test the scripts from the Ubuntu host.
