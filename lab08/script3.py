from simplecrypt import decrypt
from pprint import pprint
from netmiko import ConnectHandler
import json
from time import time

# Thread poools limit the number of simultaneous threads, which is very
# useful when connecting to hundreds or thousands of devices. Let's say
# the maximum number of threads is two, this script will simultaneously 
# connect to two devices, then another two and so on.
 
from multiprocessing.dummy import Pool as ThreadPool

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
# This function a list of dictionaries
def config_worker( device_and_creds ):
    
    # Split the list into two separate dictionaries
    device = device_and_creds[0]
    creds = device_and_creds[1]

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

# Ask the user for the maximum number os threads
num_threads_str = input( '\nNumber of threads (5): ' ) or '5'
num_threads     = int( num_threads_str )


#---- Create a list of tuples. Each tuple contains config_worker parameters 
config_params_list = []
for ipaddr,device in devices.items():
   config_params_list.append( ( device, creds[ipaddr] ) )


# Begin timer
starting_time = time()

print ('\n---- Begin thread pool execution ------\n')

print ('\n--- Creating threadpool, launching get config threads\n')
# Create a thread pool
threads = ThreadPool( num_threads )
# Map each tread to one config_worker call
results = threads.map( config_worker, config_params_list )

# End timer
print ('\n---- End get config sequential, elapsed time=', time()-starting_time)
