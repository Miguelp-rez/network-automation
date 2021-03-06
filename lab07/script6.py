from getpass import getpass
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException

username = input('Enter your SSH username: ')
password = getpass()

with open('commands_file_switch') as f:
    commands_list_switch = f.read().splitlines()

with open('commands_file_router') as f:
    commands_list_router = f.read().splitlines()

with open('devices_file') as f:
    devices_list = f.read().splitlines()

for ip_address in devices_list:
    print ('Connecting to device" ' + ip_address)
    ios_device = {
        'device_type': 'cisco_ios',
        'ip': ip_address, 
        'username': username,
        'password': password
    }

    try:
        net_connect = ConnectHandler(**ios_device)
    except (AuthenticationException):
        print ('Authentication failure: ' + ip_address)
        continue
    except (NetMikoTimeoutException):
        print ('Timeout to device: ' + ip_address)
        continue
    except (EOFError):
        print ('End of file while attempting device ' + ip_address)
        continue
    except (SSHException):
        print ('SSH Issue. Are you sure SSH is enabled? ' + ip_address)
        continue
    except Exception as unknown_error:
        print ('Some other error: ' + str(unknown_error))
        continue

    # Types of devices
    list_versions = ['vios_l2-ADVENTERPRISEK9-M',
                     'VIOS-ADVENTERPRISEK9-M'
                     ]

    # Check software versions
    for software_ver in list_versions:
        print ('Checking for ' + software_ver)
        output_version = net_connect.send_command('show version')
        int_version = 0 # Reset integer value
        int_version = output_version.find(software_ver) # Check software version
        if int_version > 0:
            print ('Software version found: ' + software_ver)
            break
        else:
            print ('Did not find ' + software_ver)

    if software_ver == 'vios_l2-ADVENTERPRISEK9-M':
        print ('Running ' + software_ver + ' commands')
        output = net_connect.send_config_set(commands_list_switch)
    elif software_ver == 'VIOS-ADVENTERPRISEK9-M':
        print ('Running ' + software_ver + ' commands')
        output = net_connect.send_config_set(commands_list_router)
    print (output) 
