# Lab02: Configuration of multiple devices  

## Objectives

1. Configure multiple vlans on each switch with a loop.
2. Backup the switches' configurations.

## Topology

![Topology](/lab02/lab02.PNG)

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
    enable password cisco
    username miguel privilege 15 password cisco
    line vty 0 4
    login local
    transport input all
    int gi 0/0
    ip address 192.168.255.71 255.255.255.0
    no shut

##### Switch S1
    enable
    conf t
    hostname S1
    enable password cisco
    username miguel privilege 15 password cisco
    line vty 0 4
    login local
    transport input all
    int vlan 1
    ip address 192.168.255.72 255.255.255.0
    no shut

##### Switch S2
    enable
    conf t
    hostname S2
    enable password cisco
    username miguel privilege 15 password cisco
    line vty 0 4
    login local
    transport input all
    int vlan 1
    ip address 192.168.255.82 255.255.255.0
    no shut

##### Switch S3
    enable
    conf t
    hostname S3
    enable password cisco
    username miguel privilege 15 password cisco
    line vty 0 4
    login local
    transport input all
    int vlan 1
    ip address 192.168.255.83 255.255.255.0
    no shut

##### Switch S4
    enable
    conf t
    hostname S4
    enable password cisco
    username miguel privilege 15 password cisco
    line vty 0 4
    login local
    transport input all
    int vlan 1
    ip address 192.168.255.84 255.255.255.0
    no shut

##### Switch S5
    enable
    conf t
    hostname S5
    enable password cisco
    username miguel privilege 15 password cisco
    line vty 0 4
    login local
    transport input all
    int vlan 1
    ip address 192.168.255.85 255.255.255.0
    no shut

##### Switch S6
    enable
    conf t
    hostname S6
    enable password cisco
    username miguel privilege 15 password cisco
    line vty 0 4
    login local
    transport input all
    int vlan 1
    ip address 192.168.255.86 255.255.255.0
    no shut

## Activities
Test the scripts from the Ubuntu host.  

**NOTE:** The script number indicates which objective is being accomplished.