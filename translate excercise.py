phone = input('Phone: ')
numbers = { #defining dictionary
	'1': 'one', #dont forget the commas at the end
	'2': 'two',
	'3': 'three',
	'4': 'four', 
	'5': 'five',
}
phone_number = ''
for x in phone:
	numbers.get(x)
	phone_number = phone_number + ' ' + numbers.get(x, '!!') # added '!' value not to have 'NONE error'
print(phone_number)
