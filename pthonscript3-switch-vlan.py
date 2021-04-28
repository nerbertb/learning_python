import getpass
import telnetlib

HOST = "192.168.122.72"		#VLAN 1 IP Address of the Switch
user = input("Enter your Switch Username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.write(b"cisco\n")		#default enable password I placed.
tn.write(b"config t\n")

for n in range (2,11):
    tn.write(b"vlan " + str(n).encode('ascii') + b"\n")		#This will write the VLAN + the number placed on the for loop range
    tn.write(b"name Python_VLAN_" + str(n).encode('ascii') + b"\n")

tn.write(b"end\n")
tn.write(b"exit\n")
print(tn.read_all().decode('ascii'))


#OUTPUT SHOWN ONCE SCRIPT IS RUN.

'''
root@NetworkAutomation-1:~# python3 pthonscript3-switch-vlan.py 
Enter your Switch Username: nerbertb
Password: 

**************************************************************************
* IOSv - Cisco Systems Confidential                                      *
*                                                                        *
* This software is provided as is without warranty for internal          *
* development and testing purposes only under the terms of the Cisco     *
* Early Field Trial agreement.  Under no circumstances may this software *
* be used for production purposes or deployed in a production            *
* environment.                                                           *
*                                                                        *
* By using the software, you agree to abide by the terms and conditions  *
* of the Cisco Early Field Trial Agreement as well as the terms and      *
* conditions of the Cisco End User License Agreement at                  *
* http://www.cisco.com/go/eula                                           *
*                                                                        *
* Unauthorized use or distribution of this software is expressly         *
* Prohibited.                                                            *
**************************************************************************
S1>enable
Password: 
S1#config t
Enter configuration commands, one per line.  End with CNTL/Z.
S1(config)#vlan 2
S1(config-vlan)#name Python_VLAN_2
S1(config-vlan)#vlan 3
S1(config-vlan)#name Python_VLAN_3
S1(config-vlan)#vlan 4
S1(config-vlan)#name Python_VLAN_4
S1(config-vlan)#vlan 5
S1(config-vlan)#name Python_VLAN_5
S1(config-vlan)#vlan 6
S1(config-vlan)#name Python_VLAN_6
S1(config-vlan)#vlan 7
S1(config-vlan)#name Python_VLAN_7
S1(config-vlan)#vlan 8
S1(config-vlan)#name Python_VLAN_8
S1(config-vlan)#vlan 9
S1(config-vlan)#name Python_VLAN_9
S1(config-vlan)#vlan 10
S1(config-vlan)#name Python_VLAN_10
S1(config-vlan)#end
S1#exit

root@NetworkAutomation-1:~# 

'''