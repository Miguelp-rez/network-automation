from simplecrypt import encrypt, decrypt
from pprint import pprint
import csv
import json

#---- Read in pertinent information from user
encrypted_credentials = input('\nInput CSV filename [encrypted-device-creds]:  ') or 'encrypted-device-creds'
key = input('Encryption key [cisco]:  ') or 'cisco'

#---- Read in the device credentials from CSV file into list of device credentials
print ('\n... getting credentials ...\n')
with open( encrypted_credentials, 'rb') as input_file:
    device_creds_json = decrypt( key, input_file.read() )

device_creds_list = json.loads( device_creds_json.decode('utf-8'))
pprint( device_creds_list )

print ('\n----- confirm: device_creds json in -----------------------------------')

# convert to dictionary of lists using dictionary comprehension
device_creds = { dev[0]:dev for dev in device_creds_list } # Whats happening?
pprint( device_creds )