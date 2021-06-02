from simplecrypt import decrypt
import json

#---- Prompt the user for a filename and a key
encrypted_credentials = input('\nInput filename [encrypted-device-creds]:  ') or 'encrypted-device-creds'
key = input('Encryption key [cisco]:  ') or 'cisco'

#---- Read in the encrypted credentials file as binary
print ('\n... getting credentials ...\n')
with open( encrypted_credentials, 'rb') as input_file:
    cyphertext = input_file.read() # Encrypted file contents
    plaintext = decrypt( key, cyphertext ) # Plaintext is a bunch of bytes

plaintext = plaintext.decode('utf-8') # Convert bytes to utf-8

print ('\n---------- Plaintext credentials----------')
device_creds = json.loads( plaintext ) # Create a list of lists
print( json.dumps( device_creds ) ) # This is what was decrypted