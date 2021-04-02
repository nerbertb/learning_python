


item =  [{
	"hostname" : "router1",
	"ip-address" : "192.168.1.2",
	"subnet-mask" : "255.255.255.0",
	"bgp-status" : "Established",
	"ipv6-enabled" : False,

},

{
	"hostname" : "router2",
	"ip-address" : "192.168.1.3",
	"subnet-mask" : "255.255.255.0",
	"bgp-status" : "Established",
	"ipv6-enabled" : False,

}

]

for each in item:
	for x, y in each.items():
		print (x,y, "\n")
	
