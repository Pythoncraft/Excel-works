import openpyxl


excel_root_files = ['‪C:\\Users\\igori\\Desktop\\Projects\\Offers.xlsx']
s = '‪C:\\Users\\igori\\Desktop\\Projects\\Offers.xlsx'
s = s.lstrip('\u202a')

values = []

for file in excel_root_files:
	workbook = openpyxl.load_workbook(s, file)
	worksheet = workbook['ANDREA PAPADOURI']
	cell_value = worksheet['E6'].value
	values.append(cell_value)

	print(cell_value)