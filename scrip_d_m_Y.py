#!usr/bin/python3
# -*- encoding: utf-8 -*-

import datetime
from datetime import date 
from datetime import *

MONTHS_A = ["january", "february", "march", "april", "may", "june","july", "august", "september","october", "november", "december"]
MONTHS_a = ["jan", "feb", "mar", "apr", "may", "jun","jul", "aug", "sep","oct", "nov", "dec"]
DAYS_B= ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
DAYS_b = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
DAY_EXTENTIONS = ["rd", "th", "st", "nd"]

# Yêu cầu xác định dữ liệu đầu vào
# Yêu cầu dữ liệu đầu vào là dữ liệu đã được quy về sử dụng space để phân cách dd mm yy
# Yêu cầu cắt dữ liệu bằng split(' ')
# Dữ liệu khi mang đi so sánh sẽ chỉ là dữ liệu thuộc dạng [[],[],[],[]]

# Function xử lý dữ liệu dạng dd mm yy, thuộc trường hợp len(data[i]) = 3
date_in = ['1997','2nd','07']

# Phân tích:
# Có ngày và tháng đều là số
# Phương hướng:
# * Ngày đứng trước tháng
# * Tháng đứng trước ngày
# * Số nào lớn hơn 12 là ngày

def Scrip_3_dd_mm_YY(text):
	YY = -1
	dd = -1
	months = -1
	for i in text:
		# Vì định dạng ngày đặc biệt và năm sinh cùng có 4 ký tự nên phải chia ra 2 trường hợp để phân tích
		# Trường hợp nếu năm sinh đứng sau và ngày có ký tự đặc biệt đứng đầu.
		if len(i) == 3 and i not in MONTHS_a and i not in DAYS_b:
			for ext in DAY_EXTENTIONS:
				if ext in i:
					c = i.find(ext)
					dd = i[:c]
		# YY == -1 để kiểm tra xem nếu năm đứng trước, tức đã xác định năm rồi thì sẽ không chạy vòng lặp này
		elif len(i) == 4 and YY == -1:
			try:
				# YY = int(i) để xác định nếu i là 4 số nguyên - tương ứng với năm sinh => YY = năm sinh
				# Nếu i là dạng day_ext thì int(i) sẽ trả ra ValueError:
				YY = int(i)
				YY = str(YY)
			except ValueError:
				for ext in DAY_EXTENTIONS:
					if ext in i:
						c = i.find(ext)
						dd = i[:c]
		# Trường hợp nếu năm sinh đứng dầu và ngày có ký tự đặc biệt đứng sau.
		# khi YY != 1 vòng lặp trên sẽ không được chạy nên sẽ chạy tới vòng lặp này khi dd == -1
		elif len(i) == 4 and dd == -1:
			try:
				YY = int(i)
			except ValueError:
				for ext in DAY_EXTENTIONS:
					if ext in i:
						c = i.find(ext)
						dd = i[:c]
		# Nếu giá trị có 2 chữ số và số đó lớn hơn 12
		elif len(i) == 2 and int(i) > 12: 
			dd = int(i)
		elif dd != -1:
			months = i
	return dd,months,YY
data = Scrip_3_dd_mm_YY(date_in)
print(data)


