#! usr/bin/python3
#-*- encoding: utf-8 -*-

# Check day_of_week to confirm data date or months is true

import datetime
from datetime import *

str_date = 'Friday 06 09 19'

# Hypothesis 1:
# format chuỗi đó và chuyển vào 1 biến để so sánh
# Có thể sử dụng Try except để thực hiện các Hypothesis khác nhau || Sử dụng 1 func
# Với mục đích nếu chuỗi gốc với chuỗi sau nhận dạng giống nhau => True

# Sử dụng ngày trong tuần để xác định tính đúng đắn của ngày tháng
# Nếu sử dụng ngày trong tuần như 1 node để
# Sử dụng một biến thứ 3 khi chạy vòng lặp xác định để ghi lại thứ tự và cách định dạng của dữ liệu đã được xác định trước
# VD: 'w d a y' khi chạy  vòng lặp sẽ được gán với các giá trị đã được định sẵn tạo ra out put
# '%w %d %a %y' để đối chiếu lại lần cuối với giá trị đầu vào

# Điều gì xảy ra nếu kết quả trả ra vẫn là lỗi
# Trường hợp này có thể được sử đụng dể thực hiện các try catch với dữ liêu thuộc dạng không xác định 



str_a = datetime.strptime(str_date, '%A %d %m %y')
str_b = datetime.strptime(str_date, '%A %m %d %y')
print(datetime.strftime(str_a, '%A %d %m %Y'))
print(datetime.strftime(str_b, '%A %m %d %Y'))
str_final = ''
if datetime.strftime(str_a, '%A %d %m %Y') == str_date:
	str_final = str_a
elif datetime.strftime(str_b, '%A %m %d %Y') == str_date :
	str_final = str_b
else:
	str_final = 'Không thể nhận diện được ngày tháng'
print(str_final)