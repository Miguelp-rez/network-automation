from simplecrypt import encrypt
import csv
import json

#---- Prompt the user for a filename and a key
plaintext_credentials = input('\nInput CSV filename [device-creds]:  ') or 'device-creds'
key = input('Encryption key [cisco]:  ') or 'cisco'

#---- Read in the device credentials from CSV file into list of device credentials
with open( plaintext_credentials, 'r' ) as input_file:
    # csv.reader returns sequence of lists.
    csv_contents = csv.reader( input_file ) # Each line of the csv file is a list.
    device_creds = [line for line in csv_contents] # Create a list of lists

print ('\n---------- Plaintext credentials----------')
plaintext = json.dumps( device_creds ) # Create nicely formated data 
print ( plaintext ) # This is what will be encrypted

#---- Prompt the user for a filename
encrypted_credentials = input('\nOutput filename [encrypted-device-creds]:  ') or 'encrypted-device-creds'

#---- Encrypt the device credentials using the key provided by the user
with open( encrypted_credentials, 'wb' ) as output_file:
    cyphertext = encrypt( key, plaintext ) # Bytes are returned
    output_file.write( cyphertext )

print ("woohoo I've encrypted the file")
print ('You should now delete the original file')
