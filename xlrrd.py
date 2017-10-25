import xlrd
workbook = xlrd.open_workbook('/home/keertmak/login.xlsx')
worksheet = workbook.sheet_by_name('Sheet1')
for current_row in range(worksheet.nrows):
	fname_text = worksheet.row(current_row)[0]
	lname_text = worksheet.row(current_row)[1]
	age= worksheet.row(current_row)[2]
	print fname_text, lname_text, age
