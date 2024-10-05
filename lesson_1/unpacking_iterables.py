fruit = "apple"
my_list = ["name", "Jason"]
my_tuple = ("name", "Jason")
outgoing = {
	"amount": 27.12,
	"frequency": "monthly",	
	"category": "subscription",		
}

joined_list = [*my_list, *my_tuple, *outgoing]
joined_tuple = (*my_list, *my_tuple)
joined_set = {*my_list, *my_tuple}

print(f'{joined_list = }')
print(f'{joined_tuple = }')
print(f'{joined_set = }')