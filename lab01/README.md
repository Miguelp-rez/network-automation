# Lab01: Basic device configuration  

## Objectives

1. Create two loopback interfaces on R1.
2. Create 100 VLANs on S1.
3. Get version information from both R1 and S1.

## Topology

![Topology](/lab01/lab01.PNG)

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
    username miguel password cisco
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
    username miguel password cisco
    line vty 0 4
    login local
    transport input all
    int vlan 1
    ip address 192.168.255.72 255.255.255.0
    no shut

## Activities
Test the scripts from the Ubuntu host.  

**NOTE:** The script number indicates which objective is being accomplished.