from getpass import getpass
from netmiko import ConnectHandler

username = input('Enter your SSH username: ')
password = getpass()

with open('commands_file') as f:
    commands_list = f.read().splitlines()

with open('devices_file') as f:
    devices_list = f.read().splitlines()

for ip_address in devices_list:
    print ('Connecting to device: ' + ip_address)
    ios_device = {
        'device_type': 'cisco_ios',
        'ip': ip_address,
        'username': 'miguel',
        'password': 'cisco'
    }

    net_connect = ConnectHandler(**ios_device)
    output = net_connect.send_config_set(commands_list)
    print (output)
