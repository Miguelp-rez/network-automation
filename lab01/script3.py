import getpass
import telnetlib

def get_version(target_string, delimiting_char):
    print("\nLooking for... " + target_string)
    start_position = version_output.index(target_string)
    end_position = version_output.find(delimiting_char, start_position)
    hits = version_output.count(target_string)
    print('Search hits:', hits)
    print(version_output[start_position : end_position])
    
devices = ["192.168.255.71", "192.168.255.72"]

for HOST in devices:
    print ("\nConnecting to host:", HOST)
    user = input("Enter your telnet username: ")
    password = getpass.getpass()

    tn = telnetlib.Telnet(HOST)

    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    tn.write(b"terminal length 0\n")
    tn.write(b"show version\n")
    tn.write(b"exit\n")

    version_output = tn.read_all().decode('ascii')

    # Get ios software name
    target_string = 'Software ('
    delimiting_char = ','
    get_version(target_string, delimiting_char)

    # Get ios version number
    target_string = 'Version '
    delimiting_char = '('
    get_version(target_string, delimiting_char)