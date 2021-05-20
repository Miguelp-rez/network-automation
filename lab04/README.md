# Lab04: NAPALM installation and examples

## Objectives

1. Get facts about S1 using NAPALM.
2. Get interface information about S1.
3. Get the mac address table and the arp cache on S1.
4. Get bgp neighbor information on S1.
5. Get bgp neighbor information on S1 and R1.

## Topology

![Topology](/lab04/lab04.PNG)

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
    int loopback 0
    ip address 2.2.2.2 255.255.255.255 
    no shut
    router bgp 65000
    neighbor 192.168.255.72 remote-as 65000
    network 2.2.2.2 mask 255.255.255.255

##### Switch S1
    enable
    conf t
    hostname S1
    ip domain-name csco.com
    crypto key generate rsa modulus 1024
    enable password cisco
    username miguel privilege 15 password cisco
    line vty 0 4
    login local
    transport input all
    int vlan 1
    ip address 192.168.255.72 255.255.255.0
    no shut
    int loopback 0
    ip address 1.1.1.1 255.255.255.255 
    no shut
    router bgp 65000
    neighbor 192.168.255.71 remote-as 65000
    network 1.1.1.1 mask 255.255.255.255

## Activities
Install netmiko and NAPALM on the Ubuntu host.

    sudo apt-get update
    sudo apt-get install python3-pip
    sudo python3 -m pip install -U pip
    pip3 install -U netmiko
    pip3 install -U napalm

Test the scripts from the Ubuntu host.