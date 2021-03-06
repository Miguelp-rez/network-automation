from netmiko import ConnectHandler

iosv_l2_s2 = {
    "device_type": "cisco_ios",
    "ip": "192.168.255.82",
    "username": "miguel",
    "password": "cisco"
}

iosv_l2_s3 = {
    "device_type": "cisco_ios",
    "ip": "192.168.255.83",
    "username": "miguel",
    "password": "cisco"
}

with open("iosv_l2_core") as f:
    lines = f.read().splitlines()
print (lines)


all_devices = [iosv_l2_s3, iosv_l2_s2]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output)
