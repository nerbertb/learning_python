# TOPOLOGY USED: https://www.dropbox.com/s/dkohdba5tpe6sxd/Cisco%20Network%20Automation%20-%20Beginner.png?dl=0

# Almost same outputs / commands on my TELNET AUTOMATION USING TELNETLIB: pythonscript4-config-switch.py

# root@NetworkAutomation-1:~# cat netmiko_configure_switch.py 
from netmiko import ConnectHandler


iosv_l2 = {
    "device_type": "cisco_ios",
    "host": "192.168.122.83",           # Switch: S3 IP address
    "username": "nerbertb",
    "password": "cisco",
}

net_connect = ConnectHandler(**iosv_l2)
output = net_connect.send_command('sho ip int br')
print (output)
output = net_connect.send_command('sho vlan br')
print (output)

config_commands =  [ 'int loop 0', 'ip address  2.2.2.2 255.255.255.0']
output = net_connect.send_config_set(config_commands)
print (output)


for vlan_number in range (20, 31):
    print ("Creating VLAN " + str(vlan_number))
    config_commands = ['vlan ' + str(vlan_number), 'name NETMIKO_Python_VLAN_' + str(vlan_number)]
    output = net_connect.send_config_set(config_commands)
    print (output)

'''

OUTPUT:

root@NetworkAutomation-1:~# python3 netmiko_configure_switch.py 


Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet0/0     unassigned      YES unset  up                    up      
GigabitEthernet0/1     unassigned      YES unset  up                    up      
GigabitEthernet0/2     unassigned      YES unset  up                    up      
GigabitEthernet0/3     unassigned      YES unset  up                    up      
GigabitEthernet1/0     unassigned      YES unset  up                    up      
GigabitEthernet1/1     unassigned      YES unset  up                    up      
GigabitEthernet1/2     unassigned      YES unset  down                  down    
GigabitEthernet1/3     unassigned      YES unset  down                  down    
Vlan1                  192.168.122.83  YES NVRAM  up                    up      
VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Gi1/2, Gi1/3
2    Python_VLAN_2                    active    
3    Python_VLAN_3                    active    
4    Python_VLAN_4                    active    
5    Python_VLAN_5                    active    
6    Python_VLAN_6                    active    
7    Python_VLAN_7                    active    
8    Python_VLAN_8                    active    
9    Python_VLAN_9                    active    
10   Python_VLAN_10                   active    
100  VLAN100                          active    
200  VLAN0200                         active    
300  VLAN0300                         active    
1002 fddi-default                     act/unsup 
1003 trcrf-default                    act/unsup 
1004 fddinet-default                  act/unsup 
1005 trbrf-default                    act/unsup 
configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
S3(config)#int loop 0
S3(config-if)#ip address  2.2.2.2 255.255.255.0
S3(config-if)#end
S3#
Creating VLAN 20
configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
S3(config)#vlan 20
S3(config-vlan)#name NETMIKO_Python_VLAN_20
Warning: Vlan 20 name length exceeded the recommended length of 20 characters.
S3(config-vlan)#end
S3#
Creating VLAN 21
configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
S3(config)#vlan 21
S3(config-vlan)#name NETMIKO_Python_VLAN_21
Warning: Vlan 21 name length exceeded the recommended length of 20 characters.
S3(config-vlan)#end
S3#
Creating VLAN 22
configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
S3(config)#vlan 22
S3(config-vlan)#name NETMIKO_Python_VLAN_22
Warning: Vlan 22 name length exceeded the recommended length of 20 characters.
S3(config-vlan)#end
S3#
Creating VLAN 23
configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
S3(config)#vlan 23
S3(config-vlan)#name NETMIKO_Python_VLAN_23
Warning: Vlan 23 name length exceeded the recommended length of 20 characters.
S3(config-vlan)#end
S3#
Creating VLAN 24
configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
S3(config)#vlan 24
S3(config-vlan)#name NETMIKO_Python_VLAN_24
Warning: Vlan 24 name length exceeded the recommended length of 20 characters.
S3(config-vlan)#end
S3#
Creating VLAN 25
configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
S3(config)#vlan 25
S3(config-vlan)#name NETMIKO_Python_VLAN_25
Warning: Vlan 25 name length exceeded the recommended length of 20 characters.
S3(config-vlan)#end
S3#
Creating VLAN 26
configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
S3(config)#vlan 26
S3(config-vlan)#name NETMIKO_Python_VLAN_26
Warning: Vlan 26 name length exceeded the recommended length of 20 characters.
S3(config-vlan)#end
S3#
Creating VLAN 27
configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
S3(config)#vlan 27
S3(config-vlan)#name NETMIKO_Python_VLAN_27
Warning: Vlan 27 name length exceeded the recommended length of 20 characters.
S3(config-vlan)#end
S3#
Creating VLAN 28
configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
S3(config)#vlan 28
S3(config-vlan)#name NETMIKO_Python_VLAN_28
Warning: Vlan 28 name length exceeded the recommended length of 20 characters.
S3(config-vlan)#end
S3#
Creating VLAN 29
configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
S3(config)#vlan 29
S3(config-vlan)#name NETMIKO_Python_VLAN_29
Warning: Vlan 29 name length exceeded the recommended length of 20 characters.
S3(config-vlan)#end
S3#
Creating VLAN 30
configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
S3(config)#vlan 30
S3(config-vlan)#name NETMIKO_Python_VLAN_30
Warning: Vlan 30 name length exceeded the recommended length of 20 characters.
S3(config-vlan)#end
S3#
root@NetworkAutomation-1:~#
'''