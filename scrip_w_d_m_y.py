#! usr/bin/python3
# -*- encoding: utf-8 -*-

import datetime
from datetime import date
from datetime import *
import script_a_A_b_B_ext
# Giải quyết vấn đề khi có thêm thứ trong tuần 

data_in = ['Sun','09','29th','2019']
# phân tích:
# Str có 3 ký tự mặc 

def Scrip_4_w_dd_mm_YY(text):
	w = -1
	dd = -1
	months = -1
	YY = -1
	for i in text:
		# Tìm ra ngày trong tuần hoặc tháng hoặc nday_ext nhưng có 3 chữ số
		if len(i) == 3:
			if i.lower() in script_a_A_b_B_ext.MONTHS_a:
				mm = i
			elif i.lower() in script_a_A_b_B_ext.DAYS_b:
				w = i
			else:
				for ext in script_a_A_b_B_ext.DAY_EXTENTIONS:
					if ext in i:
						c = i.find(ext)
						dd = i[:c]
		# Tìm ra năm hoặc day_ext 4 chữ số
		elif len(i) == 4 and YY == -1:
			try:
				YY = int(i)
				YY = str(YY)
			except ValueError:
				for ext in script_a_A_b_B_ext.DAY_EXTENTIONS:
					if ext in i:
						c = i.find(ext)
						dd = i[:c]
		# khi YY != 1 vòng lặp trên sẽ không được chạy nên sẽ chạy tới vòng lặp này khi dd == -1
		elif len(i) == 4 and dd == -1:
			try:
				YY = int(i)
			except ValueError:
				for ext in script_a_A_b_B_ext.DAY_EXTENTIONS:
					if ext in i:
						c = i.find(ext)
						dd = i[:c]
		# Nếu giá trị có 2 chữ số và số đó lớn hơn 12
		elif len(i) == 2 and int(i) > 12: 
			dd = int(i)
		# Xác định tháng nếu đã xác định được ngày
		elif dd != -1:
			months = i

	return w, dd, months, YY

# Vấn đề: Nếu tháng nằm trước ngày thì phải xác định ra sao
# Chỉ cần có thứ và ngày hoặc tháng là đủ xác định hay chưa
# Cố thể phải sử dụng lại func kiểm tra:
# Nếu có phần tử có thể nhận dạng là Months => là ngày
# Nếu có phần tử có thể nhận dạng là day_ext => là months

str_a = Scrip_4_w_dd_mm_YY(data_in)
print(str_a)
