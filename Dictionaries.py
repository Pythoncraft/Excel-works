customer = { #defining dicstionary
	'Email': 'johnsmith@gmail', #dont forget the commas at the end
	'Phone': 9405822,
	'is_verified': True
}
customer['Email'] = 'john.smith@gmail' #update the name
customer['birthdate'] = 'October 10, 1986' # add value to the dictionay
print(customer['Email'])
print(customer.get('bieth'))
print(customer['birthdate'])