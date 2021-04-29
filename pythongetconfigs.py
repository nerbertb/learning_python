# TOPOLOGY USED: https://www.dropbox.com/s/dkohdba5tpe6sxd/Cisco%20Network%20Automation%20-%20Beginner.png?dl=0
# Script for getting the configuration of multiple switches using python3 telnet library.

import getpass
import telnetlib

user = input('Enter your Switch Username: ')
password = getpass.getpass()



f = open ('myswitches')

'''
SWITCH IP ADDRESS WITH THE HOSTNAME

root@NetworkAutomation-1:~# cat /etc/hosts
127.0.1.1       NetworkAutomation-1
127.0.0.1       localhost
::1     localhost ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters

192.168.122.71 R1
192.168.122.72 S1
192.168.122.82 S2
192.168.122.83 S3
192.168.122.84 S4
192.168.122.85 S5
192.168.122.86 S6
root@NetworkAutomation-1:~# 

'''

for IP in f:
    IP = IP.strip()
    print ('Creating a backup configuration of Switch ' + (IP))
    HOST = IP
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b'Username: ')
    tn.write(user.encode('ascii') + b'\n')
    if password:
        tn.read_until(b'Password: ')
        tn.write(password.encode('ascii') + b'\n')

    tn.write(b'enable\n')		# this can be removed by configuring the user with a priviledge 15 so we can be on priveledge mode right away 
    tn.write(b'cisco\n')		# without entering the enable password.
    tn.write(b'terminal length 0\n')	#set the terminal length to 0 so we don't have to press the space bar to get the full config.
    tn.write(b'show runn\n')
    tn.write(b'exit\n')
    readoutput = tn.read_all()
    saveoutput = open ('backup_config_of_switch_' + HOST, 'w')	#will open / create a new file where
    saveoutput.write(readoutput.decode('ascii'))	#the (show runn)output that was provided on readoutput variable will be saved
    saveoutput.write('\n')			
    saveoutput.close
    print(tn.read_all().decode('ascii'))




'''

OUTPUT


root@NetworkAutomation-1:~# ls
myswitches                   pythongetconfigs.py  pythonscript2.py                test.py
pthonscript3-switch-vlan.py  pythonscript1.py     pythonscript4-config-switch.py		<-------------- Prior to running the script


root@NetworkAutomation-1:~# 
root@NetworkAutomation-1:~# python3 pythongetconfigs.py 			<--- Ran the Scrip
Enter your Switch Username: nerbertb
Password: 
Creating a backup configuration of Switch 192.168.122.72			<--- Output after running the script.

Creating a backup configuration of Switch 192.168.122.82

Creating a backup configuration of Switch 192.168.122.83

Creating a backup configuration of Switch 192.168.122.84

Creating a backup configuration of Switch 192.168.122.85

Creating a backup configuration of Switch 192.168.122.86

root@NetworkAutomation-1:~# ls
backup_config_of_switch_192.168.122.72  backup_config_of_switch_192.168.122.86  pythonscript2.py			<---------- Backup files were saved 
backup_config_of_switch_192.168.122.82  myswitches                              pythonscript4-config-switch.py
backup_config_of_switch_192.168.122.83  pthonscript3-switch-vlan.py             test.py
backup_config_of_switch_192.168.122.84  pythongetconfigs.py
backup_config_of_switch_192.168.122.85  pythonscript1.py
root@NetworkAutomation-1:~# 
root@NetworkAutomation-1:~# 
root@NetworkAutomation-1:~# 
root@NetworkAutomation-1:~# cat backup_config_of_switch_192.168.122.82

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
S2>enable
Password: 
S2#terminal length 0
S2#show runn
Building configuration...

Current configuration : 5584 bytes
!
! Last configuration change at 05:44:25 UTC Thu Apr 29 2021 by nerbertb
!
version 15.0
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
service compress-config
!
hostname S2
!
boot-start-marker
boot-end-marker
!
!
enable password cisco
!
username nerbertb password 0 cisco
no aaa new-model
!
!
!
!
!
vtp domain CISCO-vIOS
vtp mode transparent
!
!
!
ip cef
no ipv6 cef
!
!
spanning-tree mode pvst
spanning-tree extend system-id
!
vlan internal allocation policy ascending
!
vlan 2
 name Python_VLAN_2
!
vlan 3
 name Python_VLAN_3
!
vlan 4
 name Python_VLAN_4
!
vlan 5
 name Python_VLAN_5
!
vlan 6
 name Python_VLAN_6
!
vlan 7
 name Python_VLAN_7
!
vlan 8
 name Python_VLAN_8
!
vlan 9
 name Python_VLAN_9
!
vlan 10
 name Python_VLAN_10
!
vlan 100
 name VLAN100
!
vlan 200,300 
!
! 
!
!
!
!
!
!
!
!
!
!
!
interface GigabitEthernet0/0
 media-type rj45
 negotiation auto
!
interface GigabitEthernet0/1
 media-type rj45
 negotiation auto
!
interface GigabitEthernet0/2
 media-type rj45
 negotiation auto
!
interface GigabitEthernet0/3
 media-type rj45
 negotiation auto
!
interface GigabitEthernet1/0
 media-type rj45
 negotiation auto
!
interface GigabitEthernet1/1
 media-type rj45
 negotiation auto
!
interface GigabitEthernet1/2
 media-type rj45
 negotiation auto
!
interface GigabitEthernet1/3
 media-type rj45
 negotiation auto
!
interface Vlan1
 ip address 192.168.122.82 255.255.255.0
!
ip forward-protocol nd
!
no ip http server
no ip http secure-server
!
!
!
!
!
!
control-plane
!
banner exec ^C
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
**************************************************************************^C
banner incoming ^C
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
**************************************************************************^C
banner login ^C
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
**************************************************************************^C
!
line con 0
 logging synchronous
line aux 0
line vty 0 4
 logging synchronous
 login local
 transport input all
line vty 5 15
 logging synchronous
 login
!
!
end

S2#exit

root@NetworkAutomation-1:~# 


'''