import json
from napalm import get_network_driver

bgp_routers = [ '17.1.1.1',
            '17.1.1.2',
            '8.8.8.2',
            '15.1.1.2']

for ip_address in bgp_routers:
    print('Connecting to ' + ip_address)
    driver = get_network_driver('ios')
    iosv = driver(ip_address, 'miguel', 'cisco')
    iosv.open()
    bgp_neighbors = iosv.get_bgp_neighbors()
    print (json.dumps(bgp_neighbors, indent=4))
    iosv.close()