
sites = {
	"site_number" : 4,

	"site_info" : [ {
		"site_name" : "New York DC",
		"site_id" : "131A",
		"site_address" : "123 Blvd., New York, New York",
		"site_contact" : "new_yorkDC@example.com",
		},
		{
		"site_name" : "Ashburn DC",
		"site_id" : "132A",
		"site_address" : "456 Blvd., Ashburn, Virginia",
		"site_contact" : "ashburn_vaDC@example.com",

		},
		{
		"site_name" : "Dallas DC",
		"site_id" : "133A",
		"site_address" : "789 Blvd., Dallas, Texas",
		"site_contact" : "dallas_txDC@example.com",

		},
		{
		"site_name" : "Cleveland DC",
		"site_id" : "134A",
		"site_address" : "987 Blvd., Cleveland, Ohio",
		"site_contact" : "cleveland_ohDC@example.com",

		} 
		]
}




for info in sites["site_info"]:	#Will pull the list of site_info and place the values on info variable.
	print (info["site_contact"]) #Will print only the site contact email address.

print ("\n")
print (sites["site_info"])


