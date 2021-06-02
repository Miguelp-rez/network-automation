from simplecrypt import decrypt
from pprint import pprint
from netmiko import ConnectHandler
import json
from time import time

import threading

#------------------------------------------------------------------------------
def read_devices( devices_filename ):

    devices = {}  # create our dictionary for storing devices and their info

    with open( devices_filename ) as devices_file:

        for device_line in devices_file:

            device_info = device_line.strip().split(',')  #extract device info from line

            device = {'ipaddr': device_info[0],
                      'type':   device_info[1],
                      'name':   device_info[2]}  # create dictionary of device objects ...

            devices[device['ipaddr']] = device  # store our device in the devices dictionary
                                                # the keys for devices dictionary are unique IP address

    print ('\n----- devices --------------------------')
    pprint( devices )

    return devices

#------------------------------------------------------------------------------
def read_device_creds( encrypted_credentials, key ):

    print ('\n... getting credentials ...\n')
    with open( encrypted_credentials, 'rb') as input_file:
        cyphertext = input_file.read() # Encrypted file contents
        plaintext = decrypt( key, cyphertext ) # Plaintext is a bunch of bytes

    plaintext = plaintext.decode('utf-8') # Convert bytes to utf-8

    print ('\n---------- Plaintext credentials----------')
    device_creds_list = json.loads( plaintext ) # Create a list of lists
    
    # Create dictionary of lists
    # The key is string containing an IP address
    device_creds = { dev[0]:dev for dev in device_creds_list }
    pprint( device_creds )

    return device_creds

#------------------------------------------------------------------------------
# This function receives two dictionaries as parameters
def config_worker( device, creds ):

    #---- Connect to the device ----
    if   device['type'] == 'junos-srx': device_type = 'juniper'
    elif device['type'] == 'cisco-ios': device_type = 'cisco_ios'
    elif device['type'] == 'cisco-xr':  device_type = 'cisco_xr'
    else:                               device_type = 'cisco_ios'    # attempt Cisco IOS as default

    print ('---- Connecting to device {0}, username={1}, password={2}'.format( device['ipaddr'],
                                                                                creds[1], creds[2] ))

    #---- Connect to the device
    session = ConnectHandler( device_type=device_type, ip=device['ipaddr'],
                                                       username=creds[1], password=creds[2] )


    if device_type == 'juniper':
        #---- Use CLI command to get configuration data from device
        print ('---- Getting configuration from device')
        session.send_command('configure terminal')
        config_data = session.send_command('show configuration')

    if device_type == 'cisco_ios':
        #---- Use CLI command to get configuration data from device
        print ('---- Getting configuration from device')
        config_data = session.send_command('show run')
   

    if device_type == 'cisco_xr':
        #---- Use CLI command to get configuration data from device
        print ('---- Getting configuration from device')
        config_data = session.send_command('show configuration running-config')
   
    #---- Write out configuration information to file
    config_filename = 'config-' + device['ipaddr']  # Important - create unique configuration file name

    print ('---- Writing configuration: ', config_filename)
    with open( config_filename, 'w' ) as config_out:  config_out.write( config_data )

    session.disconnect()

    return


#==============================================================================
# ---- Main: Get Configuration
#==============================================================================

# Dictionary of dictionaries
# The key is an IP address
# The value is a dictionary with some connection parameters
devices = read_devices( 'devices-file' ) 

# Dictionary of lists
# The key is an IP address
# The value is a dictionary with more connection parameters
creds   = read_device_creds( 'encrypted-device-creds', 'cisco' ) 

starting_time = time()

print ('\n---- Begin get config sequential ------\n')

# Create a list of threads
config_threads_list = []

# items() returns a sequence of (key, value) tuples
for ipaddr,device in devices.items():
    print ('Creating thread for: ', device)
    config_threads_list.append( threading.Thread( target=config_worker, args=(device, creds[ipaddr] ) ) )

print ('\n---- Begin get config threading ----\n')
 # Start all threads (one by one)
for config_thread in config_threads_list:
    config_thread.start()

# Wait until all thread terminate. Pause here.
for config_thread in config_threads_list:
    config_thread.join()

# Continue
print ('\n---- End get config sequential, elapsed time=', time()-starting_time)
