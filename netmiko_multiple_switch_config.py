# TOPOLOGY USED: https://www.dropbox.com/s/dkohdba5tpe6sxd/Cisco%20Network%20Automation%20-%20Beginner.png?dl=0

# Configuring multiple switches using netmiko SSH

from netmiko import ConnectHandler


iosv_l2_s1 = {
    "device_type": "cisco_ios",
    "host": "192.168.122.72",           # Switch: S1 IP address
    "username": "nerbertb",
    "password": "cisco",
}

iosv_l2_s2 = {
    "device_type": "cisco_ios",
    "host": "192.168.122.82",           # Switch: S2 IP address
    "username": "nerbertb",
    "password": "cisco",
}

iosv_l2_s3 = {
    "device_type": "cisco_ios",
    "host": "192.168.122.83",           # Switch: S3 IP address
    "username": "nerbertb",
    "password": "cisco",
}

iosv_l2_s4 = {
    "device_type": "cisco_ios",
    "host": "192.168.122.84",           # Switch: S4 IP address
    "username": "nerbertb",
    "password": "cisco",
}

iosv_l2_s5 = {
    "device_type": "cisco_ios",
    "host": "192.168.122.85",           # Switch: S5 IP address
    "username": "nerbertb",
    "password": "cisco",
}


iosv_l2_s6 = {
    "device_type": "cisco_ios",
    "host": "192.168.122.86",           # Switch: S6 IP address
    "username": "nerbertb",
    "password": "cisco",
}

iosv_l2 = [iosv_l2_s1, iosv_l2_s2, iosv_l2_s3, iosv_l2_s4, iosv_l2_s5, iosv_l2_s6]

for switches in iosv_l2:
	net_connect = ConnectHandler(**switches)
	for vlan_number in range (20, 31):
		print ("Creating VLAN " + str(vlan_number))
		config_commands = ['vlan ' + str(vlan_number), 'name NETMIKO_Python_VLAN_' + str(vlan_number)]
		output = net_connect.send_config_set(config_commands)
		print (output)


'''

root@NetworkAutomation-1:~# python3 netmiko_multiple_switch_config.py 
Creating VLAN 20
configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
S1(config)#vlan 20
S1(config-vlan)#name NETMIKO_Python_VLAN_20
Warning: Vlan 20 name length exceeded the recommended length of 20 characters.
S1(config-vlan)#end
S1#
Creating VLAN 21
configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
S1(config)#vlan 21
S1(config-vlan)#name NETMIKO_Python_VLAN_21
Warning: Vlan 21 name length exceeded the recommended length of 20 characters.
S1(config-vlan)#end
S1#
Creating VLAN 22
configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
S1(config)#vlan 22
S1(config-vlan)#name NETMIKO_Python_VLAN_22
Warning: Vlan 22 name length exceeded the recommended length of 20 characters.
S1(config-vlan)#end
S1#
Creating VLAN 23
configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
S1(config)#vlan 23
S1(config-vlan)#name NETMIKO_Python_VLAN_23
Warning: Vlan 23 name length exceeded the recommended length of 20 characters.
S1(config-vlan)#end
S1#
Creating VLAN 24
configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
S1(config)#vlan 24
S1(config-vlan)#name NETMIKO_Python_VLAN_24
Warning: Vlan 24 name length exceeded the recommended length of 20 characters.
S1(config-vlan)#end
S1#
Creating VLAN 25
configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
S1(config)#vlan 25
S1(config-vlan)#name NETMIKO_Python_VLAN_25
Warning: Vlan 25 name length exceeded the recommended length of 20 characters.
S1(config-vlan)#end
S1#
Creating VLAN 26
configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
S1(config)#vlan 26
S1(config-vlan)#name NETMIKO_Python_VLAN_26
Warning: Vlan 26 name length exceeded the recommended length of 20 characters.
S1(config-vlan)#end
S1#
Creating VLAN 27
configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
S1(config)#vlan 27
S1(config-vlan)#name NETMIKO_Python_VLAN_27
Warning: Vlan 27 name length exceeded the recommended length of 20 characters.
S1(config-vlan)#end
S1#
Creating VLAN 28
configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
S1(config)#vlan 28
S1(config-vlan)#name NETMIKO_Python_VLAN_28
Warning: Vlan 28 name length exceeded the recommended length of 20 characters.
S1(config-vlan)#end
S1#
Creating VLAN 29
configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
S1(config)#vlan 29
S1(config-vlan)#name NETMIKO_Python_VLAN_29
Warning: Vlan 29 name length exceeded the recommended length of 20 characters.
S1(config-vlan)#end
S1#
Creating VLAN 30
configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
S1(config)#vlan 30
S1(config-vlan)#name NETMIKO_Python_VLAN_30
Warning: Vlan 30 name length exceeded the recommended length of 20 characters.
S1(config-vlan)#end
S1#
Creating VLAN 20
configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
S2(config)#vlan 20
S2(config-vlan)#name NETMIKO_Python_VLAN_20
Warning: Vlan 20 name length exceeded the recommended length of 20 characters.
S2(config-vlan)#end
S2#
Creating VLAN 21
configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
S2(config)#vlan 21
S2(config-vlan)#name NETMIKO_Python_VLAN_21
Warning: Vlan 21 name length exceeded the recommended length of 20 characters.
S2(config-vlan)#end
S2#
Creating VLAN 22
configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
S2(config)#vlan 22
S2(config-vlan)#name NETMIKO_Python_VLAN_22
Warning: Vlan 22 name length exceeded the recommended length of 20 characters.
S2(config-vlan)#end
S2#
Creating VLAN 23
configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
S2(config)#vlan 23
S2(config-vlan)#name NETMIKO_Python_VLAN_23
Warning: Vlan 23 name length exceeded the recommended length of 20 characters.
S2(config-vlan)#end



<snipped> #Deleted some part of the result to make it shorter.



S5(config)#vlan 26
S5(config-vlan)#name NETMIKO_Python_VLAN_26
Warning: Vlan 26 name length exceeded the recommended length of 20 characters.
S5(config-vlan)#end
S5#
Creating VLAN 27
configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
S5(config)#vlan 27
S5(config-vlan)#name NETMIKO_Python_VLAN_27
Warning: Vlan 27 name length exceeded the recommended length of 20 characters.
S5(config-vlan)#end
S5#
Creating VLAN 28
configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
S5(config)#vlan 28
S5(config-vlan)#name NETMIKO_Python_VLAN_28
Warning: Vlan 28 name length exceeded the recommended length of 20 characters.
S5(config-vlan)#end
S5#
Creating VLAN 29
configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
S5(config)#vlan 29
S5(config-vlan)#name NETMIKO_Python_VLAN_29
Warning: Vlan 29 name length exceeded the recommended length of 20 characters.
S5(config-vlan)#end
S5#
Creating VLAN 30
configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
S5(config)#vlan 30
S5(config-vlan)#name NETMIKO_Python_VLAN_30
Warning: Vlan 30 name length exceeded the recommended length of 20 characters.
S5(config-vlan)#end
S5#
Creating VLAN 20
configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
S6(config)#vlan 20
S6(config-vlan)#name NETMIKO_Python_VLAN_20
Warning: Vlan 20 name length exceeded the recommended length of 20 characters.
S6(config-vlan)#end
S6#
Creating VLAN 21
configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
S6(config)#vlan 21
S6(config-vlan)#name NETMIKO_Python_VLAN_21
Warning: Vlan 21 name length exceeded the recommended length of 20 characters.
S6(config-vlan)#end
S6#
Creating VLAN 22
configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
S6(config)#vlan 22
S6(config-vlan)#name NETMIKO_Python_VLAN_22
Warning: Vlan 22 name length exceeded the recommended length of 20 characters.
S6(config-vlan)#end
S6#
Creating VLAN 23
configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
S6(config)#vlan 23
S6(config-vlan)#name NETMIKO_Python_VLAN_23
Warning: Vlan 23 name length exceeded the recommended length of 20 characters.
S6(config-vlan)#end
S6#
Creating VLAN 24
configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
S6(config)#vlan 24
S6(config-vlan)#name NETMIKO_Python_VLAN_24
Warning: Vlan 24 name length exceeded the recommended length of 20 characters.
S6(config-vlan)#end
S6#
Creating VLAN 25
configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
S6(config)#vlan 25
S6(config-vlan)#name NETMIKO_Python_VLAN_25
Warning: Vlan 25 name length exceeded the recommended length of 20 characters.
S6(config-vlan)#end
S6#
Creating VLAN 26
configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
S6(config)#vlan 26
S6(config-vlan)#name NETMIKO_Python_VLAN_26
Warning: Vlan 26 name length exceeded the recommended length of 20 characters.
S6(config-vlan)#end
S6#
Creating VLAN 27
configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
S6(config)#vlan 27
S6(config-vlan)#name NETMIKO_Python_VLAN_27
Warning: Vlan 27 name length exceeded the recommended length of 20 characters.
S6(config-vlan)#end
S6#
Creating VLAN 28
configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
S6(config)#vlan 28
S6(config-vlan)#name NETMIKO_Python_VLAN_28
Warning: Vlan 28 name length exceeded the recommended length of 20 characters.
S6(config-vlan)#end
S6#
Creating VLAN 29
configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
S6(config)#vlan 29
S6(config-vlan)#name NETMIKO_Python_VLAN_29
Warning: Vlan 29 name length exceeded the recommended length of 20 characters.
S6(config-vlan)#end
S6#
Creating VLAN 30
configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
S6(config)#vlan 30
S6(config-vlan)#name NETMIKO_Python_VLAN_30
Warning: Vlan 30 name length exceeded the recommended length of 20 characters.
S6(config-vlan)#end
S6#
root@NetworkAutomation-1:~# 


'''