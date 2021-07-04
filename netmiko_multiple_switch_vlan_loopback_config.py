from netmiko import ConnectHandler

iosv_l2_s1 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.122.81',
	'username': 'nerbert',
	'password': 'cisco'
}

iosv_l2_s2 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.122.82',
	'username': 'nerbert',
	'password': 'cisco'
}

iosv_l2_s3 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.122.83',
	'username': 'nerbert',
	'password': 'cisco'
}

all_devices = [iosv_l2_s1, iosv_l2_s2, iosv_l2_s3]


for devices in all_devices:
	net_connect = ConnectHandler(**devices)
	for v in range (2, 21):
		print ('Configuring VLAN ' + str(v))
		vlans = ['vlan ' + str(v), 'name Netmiko_VLAN ' + str(v)]
		output = net_connect.send_config_set(vlans)
		print (output)
	if devices == iosv_l2_s1:
		config_loopback = ['int loopback0', 'ip add 1.1.1.1 255.255.255.0', 'no shut']
		output = net_connect.send_config_set(config_loopback)
		print(output)
	elif devices == iosv_l2_s2:
		config_loopback = ['int loopback0', 'ip add 2.2.2.2 255.255.255.0', 'no shut']
		output = net_connect.send_config_set(config_loopback)
		print(output)
	elif devices == iosv_l2_s3:
		config_loopback = ['int loopback0', 'ip add 3.3.3.3 255.255.255.0', 'no shut']
		output = net_connect.send_config_set(config_loopback)
		print(output)