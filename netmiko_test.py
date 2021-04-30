
# TOPOLOGY USED: https://www.dropbox.com/s/dkohdba5tpe6sxd/Cisco%20Network%20Automation%20-%20Beginner.png?dl=0
# Simple scrip to send show commands to the Router / Switch

# root@NetworkAutomation-1:~# cat netmiko_test.py 


from netmiko import ConnectHandler


iosv_l2 = {
    "device_type": "cisco_ios",
    "host": "192.168.122.82",		# Switch: S2 IP address
    "username": "nerbertb",
    "password": "cisco",
}

net_connect = ConnectHandler(**iosv_l2)
output = net_connect.send_command('sho ip int br')
print (output)
output = net_connect.send_command('sho vlan br')
print (output)


'''
OUTPUT:

root@NetworkAutomation-1:~# 
root@NetworkAutomation-1:~# python3 netmiko_test.py 
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet0/0     unassigned      YES unset  up                    up      
GigabitEthernet0/1     unassigned      YES unset  up                    up      
GigabitEthernet0/2     unassigned      YES unset  up                    up      
GigabitEthernet0/3     unassigned      YES unset  up                    up      
GigabitEthernet1/0     unassigned      YES unset  up                    up      
GigabitEthernet1/1     unassigned      YES unset  up                    up      
GigabitEthernet1/2     unassigned      YES unset  down                  down    
GigabitEthernet1/3     unassigned      YES unset  down                  down    
Vlan1                  192.168.122.82  YES NVRAM  up                    up      
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
root@NetworkAutomation-1:~# 


'''