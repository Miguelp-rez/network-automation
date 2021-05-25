from simplecrypt import encrypt, decrypt
from pprint import pprint
import csv
import json

#---- Read in pertinent information from user
raw_credentials = input('\nInput CSV filename [device-creds]:  ') or 'device-creds'
key = input('Encryption key [cisco]:  ') or 'cisco'

#---- Read in the device credentials from CSV file into list of device credentials
with open( raw_credentials, 'r' ) as input_file:
    device_creds_reader = csv.reader( input_file )
    device_creds_list = [device for device in device_creds_reader]  # Whats happening?

print ('\n----- device_creds ---------------------------------------------------')
pprint( device_creds_list )

#---- Encrypt the device credentials using ken from user
encrypted_credentials = input('\nOutput encrypted filename [encrypted-device-creds]:  ') or 'encrypted-device-creds'

with open( encrypted_credentials, 'wb' ) as output_file:
    output_file.write( encrypt( key, json.dumps( device_creds_list ) ) )

print ("woohoo I've encrypted the file")
