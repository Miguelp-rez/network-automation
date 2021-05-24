import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl2 = driver('192.168.255.72', 'miguel', 'cisco')
iosvl2.open()

print ('Accessing 192.168.255.72')

config_files = ['ACL100.txt', 'ospf1.txt']
for filename in config_files:
    iosvl2.load_merge_candidate(filename=filename)
    diffs = iosvl2.compare_config()
    if len(diffs) > 0:
        print(diffs)
        iosvl2.commit_config()
    else:
        print(filename + ' configuration is not required')
        iosvl2.discard_config()

iosvl2.close()