#!usr/bin/python
# -*- encoding: utf-8 -*- 

import datetime
from datetime import date
from datetime import *


MONTHS_A = ["january", "february", "march", "april", "may", "june","july", "august", "september","october", "november", "december"]
MONTHS_a = ["jan", "feb", "mar", "apr", "may", "jun","jul", "aug", "sep","oct", "nov", "dec"]
DAYS_B= ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
DAYS_b = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
DAY_EXTENTIONS = ["rd", "th", "st", "nd"]


# Xác định từng định dạng ngày tháng:
# Xác định dữ liệu đủ 3 dạng dd/mm/yy nhưng khác nhau về định dạng của tháng và ngày
data_in = '16 July 97'

# d + m + y
	# Begin
# try: 
# 	str_a = datetime.strptime(data_in, '%d %m %Y')
# except ValueError:
# 	try:
# 		str_a = datetime.strptime(data_in, '%d %m %y')	
# 	except: 
# 		try:
# 			str_a = datetime.strptime(data_in, '%m %d %y')	
# 		except:
# 				str_a = datetime.strptime(data_in, '%m %d %Y')
	#End

# d + b + y
# Phân biệt nếu có tháng là %b or %B
	# Begin
# try: 
# 	str_a = datetime.strptime(data_in, '%d %b %Y')
# except ValueError:
# 	try:
# 		str_a = datetime.strptime(data_in, '%d %b %y')	
# 	except: 
# 		try:
# 			str_a = datetime.strptime(data_in, '%m %b %y')	
# 		except:
# 			try:
# 				str_a = datetime.strptime(data_in, '%m %b %Y')
# 			except:
# 				try: 
# 					str_a = datetime.strptime(data_in, '%d %B %Y')
# 				except ValueError:
# 					try:
# 						str_a = datetime.strptime(data_in, '%d %B %y')	
# 					except: 
# 						try:
# 							str_a = datetime.strptime(data_in, '%B %d %y')	
# 						except:
# 								str_a = datetime.strptime(data_in, '%B %d %Y')
	# End
# print(datetime.strftime(str_a, '%d %B %Y'))

# w + d + m + y = 3*2*2*2 = 24 try except

a = 'wed 4th 09 2019'
a = [x for x in a.split(' ')]
print(a[1][:1])
b = 'th' in a[1]
c = ''
print(b)

# Vòng lặp tìm day_ext
for ext in DAY_EXTENTIONS:
	if ext in a[1]:
		c = a[1].find(ext)
		c = a[1][:c]
# -----------

months = -1
day = -1
day_of_week = -1

# Vòng lặp lấy các giá trị trong chuỗi
for i in a:
	if i in MONTHS_a:
		months = MONTHS_a.index(i) +1
	elif i in MONTHS_A:
		months = MONTHS_A.index(i) + 1
	elif i  in DAYS_b:
		day_of_week = DAYS_b.index(i)

	else:
		for ext in DAY_EXTENTIONS:
			if ext in i:
				day = i.find(ext)
				day = i[:day]
