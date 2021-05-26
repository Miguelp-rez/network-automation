# Lab06: Device configuration with NAPALM   

## Objectives

1. Create ACL 100 on S1.
2. Compare existing configurations on S1 before commiting new changes.
3. Use multiple configuration files on the same script.
4. Configure multiple devices with multiple configuration files with one script.

## Topology

![Topology](/lab06/lab06.PNG)

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
    ip scp server enable 
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

##### Switch S1
    enable
    conf t
    ip scp server enable 
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

## Activities
Install netmiko and NAPALM on the Ubuntu host.

    sudo apt-get update
    sudo apt-get install python3-pip
    python3 -m pip install -U pip
    pip3 install -U netmiko
    pip3 install -U napalm
    
Test the scripts from the Ubuntu host.  

**NOTE:** The script number indicates which objective is being accomplished.  