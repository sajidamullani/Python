vendors=["Cisco","HP","Nortel","Avaya","Juniper"]
for each_vendors in vendors:
	print(each_vendors)
else:
	print("The end of the list has been reached")
	
for element_index in range(len(vendors)):
	print(vendors[element_index])
	
for index,element in enumerate(vendors):
	print(index,element)
my_string="Cisco"
for letter in my_string:
	print(letter)
	print(letter*2)
	print(letter*3)
