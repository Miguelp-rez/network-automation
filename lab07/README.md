# Lab07: Netmiko examples  

## Objectives

1. Send a single command to switch S1.
2. Send a file of commands to switch S1.
3. Configure multiple devices using a file of IP addresses.
4. Prompt the user for her credentials.
5. Add error handling to the script.
6. Run device specific commands based on the software version found.

## Topology

![Topology](/lab07/lab07.PNG)

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
    ip address 192.168.255.81 255.255.255.0
    no shut

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
    ip address 192.168.255.82 255.255.255.0
    no shut

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

## Activities
Install netmiko and on the Ubuntu host.

    sudo apt-get update
    sudo apt-get install python3-pip
    python3 -m pip install -U pip
    pip3 install -U netmiko
    
Test the scripts from the Ubuntu host.  

**NOTE:** The script number indicates which objective is being accomplished.