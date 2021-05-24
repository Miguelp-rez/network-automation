import json
from napalm import get_network_driver

network_devices = [ '192.168.255.72',
                    '192.168.255.71',
                    ]

config_files = ['ACL100.txt', 
                'ospf1.txt'
                ]

for ip_address in network_devices:
    print ('Accessing ' + ip_address)
    driver = get_network_driver('ios')
    iosvl2 = driver(ip_address, 'miguel', 'cisco')
    iosvl2.open()
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