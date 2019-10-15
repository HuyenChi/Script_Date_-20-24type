#!usr/bin/python
# -*- encoding: utf-8 -*- 

import datetime
from datetime import date
from datetime import *

# Xác định từng định dạng ngày tháng:
# Xác định dữ liệu đủ 3 dạng dd/mm/yy nhưng khác nhau về định dạng của tháng và ngày
data_in = '5 4 sep 2019'
str_a = datetime.strptime(data_in, '%w %d %b %Y')
print(str_a)
print(datetime.strftime(str_a, '%A %d %B %Y'))
	