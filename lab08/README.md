# Lab08: Netmiko automation

## Objectives

0. Encrypt and decrypt user credentials.
1. Get the running configuration from all devices in the topology.
2. Use multithreading to reduce the execution time of the script.
3. Use thread pools to reduce the execution time of the script.

## Topology

![Topology](/lab08/lab08.PNG)

## Initial state

To erase any previous configurations use the following command on privilege mode:  
\# write erase  

To access the ubuntu host, use the following credentials:
- username: ubuntu
- password: cisco

To access end user devices, use the following credentials:
- username: cisco
- password: cisco

Copy and paste the following commands on each device to restore the initial configuration

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
    ip address 192.168.255.71 255.255.255.0
    no shut

##### Switch S2
    enable
    conf t
    hostname S2
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

##### Switch S3
    enable
    conf t
    hostname S3
    ip domain-name csco.com
    crypto key generate rsa modulus 1024
    enable password cisco
    username miguel privilege 15 password cisco
    line vty 0 4
    login local
    transport input all
    int vlan 1
    ip address 192.168.255.73 255.255.255.0
    no shut

##### Switch S4
    enable
    conf t
    hostname S4
    ip domain-name csco.com
    crypto key generate rsa modulus 1024
    enable password cisco
    username miguel privilege 15 password cisco
    line vty 0 4
    login local
    transport input all
    int vlan 1
    ip address 192.168.255.74 255.255.255.0
    no shut

##### Switch S5
    enable
    conf t
    hostname S5
    ip domain-name csco.com
    crypto key generate rsa modulus 1024
    enable password cisco
    username miguel privilege 15 password cisco
    line vty 0 4
    login local
    transport input all
    int vlan 1
    ip address 192.168.255.75 255.255.255.0
    no shut

## Activities
Install netmiko on the Ubuntu host.

    sudo apt-get update
    sudo apt-get install python3-pip
    python3 -m pip install -U pip
    pip3 install -U netmiko
    pip3 install -U simple-crypt

Test the scripts from the Ubuntu host.  

**NOTE:** The script number indicates which objective is being accomplished.