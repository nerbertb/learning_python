# TOPOLOGY USED: https://www.dropbox.com/s/dkohdba5tpe6sxd/Cisco%20Network%20Automation%20-%20Beginner.png?dl=0


import getpass
import telnetlib

user = input('Enter your Switch Username: ')
password = getpass.getpass()



f = open ('myswitches')


''''
TEXT File created with IP Addresses of the Switches:

root@NetworkAutomation-1:~# cat myswitches 
192.168.122.72
192.168.122.82
192.168.122.83
192.168.122.84
192.168.122.85
192.168.122.86
root@NetworkAutomation-1:~# 

'''

for IP in f:
    IP = IP.strip()
    print ('Configuring Switch ' + (IP))
    HOST = IP
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b'Username: ')
    tn.write(user.encode('ascii') + b'\n')
    if password:
        tn.read_until(b'Password: ')
        tn.write(password.encode('ascii') + b'\n')

    tn.write(b'enable\n')
    tn.write(b'cisco\n')		# Will have to properly config this to remove the enable password
    tn.write(b'config t\n')
    for n in range (2,11):
        tn.write(b'vlan ' + str(n).encode('ascii') + b'\n')
        tn.write(b'name Python_VLAN_' + str(n).encode('ascii') + b'\n')
    tn.write(b'end\n')
    tn.write(b'exit\n')
    print(tn.read_all().decode('ascii'))


'''

OUTPUT When we run the script:


root@NetworkAutomation-1:~# python3 pythonscript4-config-switch.py 
Enter your Switch Username: nerbertb
Password: 
Configuring Switch 192.168.122.72

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

Configuring Switch 192.168.122.82

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
S2#config t
Enter configuration commands, one per line.  End with CNTL/Z.
S2(config)#vlan 2
S2(config-vlan)#name Python_VLAN_2
S2(config-vlan)#vlan 3
S2(config-vlan)#name Python_VLAN_3
S2(config-vlan)#vlan 4
S2(config-vlan)#name Python_VLAN_4
S2(config-vlan)#vlan 5
S2(config-vlan)#name Python_VLAN_5
S2(config-vlan)#vlan 6
S2(config-vlan)#name Python_VLAN_6
S2(config-vlan)#vlan 7
S2(config-vlan)#name Python_VLAN_7
S2(config-vlan)#vlan 8
S2(config-vlan)#name Python_VLAN_8
S2(config-vlan)#vlan 9
S2(config-vlan)#name Python_VLAN_9
S2(config-vlan)#vlan 10
S2(config-vlan)#name Python_VLAN_10
S2(config-vlan)#end
S2#exit

Configuring Switch 192.168.122.83

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
S3>enable
Password: 
S3#config t
Enter configuration commands, one per line.  End with CNTL/Z.
S3(config)#vlan 2
S3(config-vlan)#name Python_VLAN_2
S3(config-vlan)#vlan 3
S3(config-vlan)#name Python_VLAN_3
S3(config-vlan)#vlan 4
S3(config-vlan)#name Python_VLAN_4
S3(config-vlan)#vlan 5
S3(config-vlan)#name Python_VLAN_5
S3(config-vlan)#vlan 6
S3(config-vlan)#name Python_VLAN_6
S3(config-vlan)#vlan 7
S3(config-vlan)#name Python_VLAN_7
S3(config-vlan)#vlan 8
S3(config-vlan)#name Python_VLAN_8
S3(config-vlan)#vlan 9
S3(config-vlan)#name Python_VLAN_9
S3(config-vlan)#vlan 10
S3(config-vlan)#name Python_VLAN_10
S3(config-vlan)#end
S3#exit

Configuring Switch 192.168.122.84

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
S4>enable
Password: 
S4#config t
Enter configuration commands, one per line.  End with CNTL/Z.
S4(config)#vlan 2
S4(config-vlan)#name Python_VLAN_2
S4(config-vlan)#vlan 3
S4(config-vlan)#name Python_VLAN_3
S4(config-vlan)#vlan 4
S4(config-vlan)#name Python_VLAN_4
S4(config-vlan)#vlan 5
S4(config-vlan)#name Python_VLAN_5
S4(config-vlan)#vlan 6
S4(config-vlan)#name Python_VLAN_6
S4(config-vlan)#vlan 7
S4(config-vlan)#name Python_VLAN_7
S4(config-vlan)#vlan 8
S4(config-vlan)#name Python_VLAN_8
S4(config-vlan)#vlan 9
S4(config-vlan)#name Python_VLAN_9
S4(config-vlan)#vlan 10
S4(config-vlan)#name Python_VLAN_10
S4(config-vlan)#end
S4#exit

Configuring Switch 192.168.122.85

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
S5>enable
Password: 
S5#config t
Enter configuration commands, one per line.  End with CNTL/Z.
S5(config)#vlan 2
S5(config-vlan)#name Python_VLAN_2
S5(config-vlan)#vlan 3
S5(config-vlan)#name Python_VLAN_3
S5(config-vlan)#vlan 4
S5(config-vlan)#name Python_VLAN_4
S5(config-vlan)#vlan 5
S5(config-vlan)#name Python_VLAN_5
S5(config-vlan)#vlan 6
S5(config-vlan)#name Python_VLAN_6
S5(config-vlan)#vlan 7
S5(config-vlan)#name Python_VLAN_7
S5(config-vlan)#vlan 8
S5(config-vlan)#name Python_VLAN_8
S5(config-vlan)#vlan 9
S5(config-vlan)#name Python_VLAN_9
S5(config-vlan)#vlan 10
S5(config-vlan)#name Python_VLAN_10
S5(config-vlan)#end
S5#exit

Configuring Switch 192.168.122.86

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
S6>enable
Password: 
S6#config t
Enter configuration commands, one per line.  End with CNTL/Z.
S6(config)#vlan 2
S6(config-vlan)#name Python_VLAN_2
S6(config-vlan)#vlan 3
S6(config-vlan)#name Python_VLAN_3
S6(config-vlan)#vlan 4
S6(config-vlan)#name Python_VLAN_4
S6(config-vlan)#vlan 5
S6(config-vlan)#name Python_VLAN_5
S6(config-vlan)#vlan 6
S6(config-vlan)#name Python_VLAN_6
S6(config-vlan)#vlan 7
S6(config-vlan)#name Python_VLAN_7
S6(config-vlan)#vlan 8
S6(config-vlan)#name Python_VLAN_8
S6(config-vlan)#vlan 9
S6(config-vlan)#name Python_VLAN_9
S6(config-vlan)#vlan 10
S6(config-vlan)#name Python_VLAN_10
S6(config-vlan)#end
S6#exit

root@NetworkAutomation-1:~# 

'''


''' 
From Switch : S2
Debug Telnet was enabled to see the automation doing the job.

S2#debug telnet 
Incoming Telnet debugging is on
S2#
*Apr 29 05:44:21.056: Telnet2: 1 1 251 1
*Apr 29 05:44:21.057: TCP2: Telnet sent WILL ECHO (1)
*Apr 29 05:44:21.057: Telnet2: 2 2 251 3
*Apr 29 05:44:21.057: TCP2: Telnet sent WILL SUPPRESS-GA (3)
*Apr 29 05:44:21.057: Telnet2: 80000 80000 253 24
*Apr 29 05:44:21.057: TCP2: Telnet sent DO TTY-TYPE (24)
*Apr 29 05:44:21.057: Telnet2: 10000000 10000000 253 31
*Apr 29 05:44:21.057: TCP2: Telnet sent DO WINDOW-SIZE (31)
*Apr 29 05:44:21.063: TCP2: Telnet received DONT ECHO (1)
*Apr 29 05:44:21.063: TCP2: Telnet sent WONT ECHO (1)
*Apr 29 05:44:21.065: TCP2: Telnet received DONT SUPPRESS-GA (3)
*Apr 29 05:44:21.065: TCP2: Telnet sent WONT SUPPRESS-GA (3)
S2#
*Apr 29 05:44:21.066: TCP2: Telnet received WONT TTY-TYPE (24)
*Apr 29 05:44:21.066: TCP2: Telnet sent DONT TTY-TYPE (24)
*Apr 29 05:44:21.066: TCP2: Telnet received WONT WINDOW-SIZE (31)
*Apr 29 05:44:21.066: TCP2: Telnet sent DONT WINDOW-SIZE (31)
*Apr 29 05:44:21.081: TCP2: Telnet received DONT ECHO (1)
*Apr 29 05:44:21.081: TCP2: Telnet received DONT SUPPRESS-GA (3)
*Apr 29 05:44:21.081: TCP2: Telnet received WONT TTY-TYPE (24)
*Apr 29 05:44:21.081: TCP2: Telnet received WONT WINDOW-SIZE (31)
S2#
*Apr 29 05:44:25.075: %SYS-5-CONFIG_I: Configured from console by nerbertb on vty0 (192.168.122.217)
S2#



-- Did a Show vlan brief to check the VLANS created.

S2#show vlan br

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
S2#

'''

