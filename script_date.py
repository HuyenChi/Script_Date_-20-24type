#!usr/bin/python
# -*- encoding: utf-8 -*-
import datetime as dt
from datetime import datetime
from datetime import date
MONTHS = ["january", "february", "march", "april", "may", "june","july", "august", "september","october", "november", "december"]
DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
DAY_EXTENTIONS = ["rd", "th", "st", "nd"]

a = '15 07 19'
try:
	b = datetime.strptime(a, '%d %b %Y')
except ValueError:
	try:
		b = datetime.strptime(a, '%d %b %y')
	except ValueError:
		b = datetime.strptime(a, '%d %m %y')
print(b)
b = b.strftime('%d %B %Y')
print(b)


# str_in = '16th 07 1997' 
# str_out = '16th July 1997'
# day_out = '16'
# day_ext_out = 'th'
# months_out = 'July' + '7'
# Year_out = '1997'
# lst_str = [x for x in str_in.split()]
# # Mục tiêu: nhận dạng nhiều nhất có thể các dạng ký tự nhập vào
# # Các mẫu thử
# # Có thể format theo 1 giá trị mặc định trước khi đưa vào lọc
# # Có thể sử dụng try and except để chạy các giả định khi ép str vào 1 kiểu ngày tháng định sẵn
# # Thực hiện đưa ra các giả định về cách insert ngu ngốc của bọn data entry person
# # dd/mm/yy || mm/dd/yy || yy/mm/dd ||
# # Có 4 cách phân định giữa các giá trị: '/' ',' '-' ' ', Ném nó vào if với điều kiện
# # Nếu dữ liệu đó có ký tự đặc biệt nằm trong 3 dạng: '/' ',' '-' thì sử dụng replace('-,/,,', ' ')
# print(lst_str)
print('-------------------------------------------------------------------------')
str_test = ["16-07-1997","23-07-1997", "03/08/1997", "07/11/1996", "05-06-1998","15,06,1998"]
# if "-" in str_test or "/" in str_test or "," in str_test:
# 	str_obj = str_test.replace("-"," ")
# 	str_obj = str_test.replace("-","_")
# 	str_obj = str_test.replace("/","_")
# else:
# 	print('none')
# print(str_test)
# print(str_obj)

# for x in str_test:
# 	if "-" in x or "/" in x or "," in x:
# 		x =x.replace("-"," ")
# 		x =x.replace("/"," ")
# 		x =x.replace(","," ")
# 		print(x)
# 	else:
# 		print("False")

# Format str_ext to space
def format_date(argument):
	if 'list' in str(type(argument)):
		argument = [ x.replace("-"," ") for x in argument]
		argument = [ x.replace("/"," ") for x in argument]
		argument = [ x.replace(","," ") for x in argument]
	else:
		argument = argument.replace("-"," ")
		argument = argument.replace("-","_")
		argument = argument.replace("/","_")
	return argument
str_test = format_date(str_test)
print(str_test)
str_a = format_date('16-07-1997')
print(str_a)
print('-----------------------------------------------------------------')





# # Thực hiện đưa ra các giả định về cách insert ngu ngốc của bọn data entry person
# # dd/mm/yy || mm/dd/yy || yy/mm/dd ||

#  ------------------------------------------------------------------------------
# Nếu dữ liệu được đưa vào thiếu đi năm || Có thể xác định năm bằng năm hiện tại hoặc gửi ra lỗi
#  Vấn đề thực tế: làm thế nào để xác định được khi dữ liệu là dạng đặc biệt 
# sử dụng str.lower()
# 06-07-08
# 06-07-97
# 07 - july - 07
# 07 - 07 - 2007
# Vấn đề chưa được giải quyết
# Nếu format với 3 giá trị không xác định hay 2 giá trị không xác định => tạch
# Phác thảo đầu tiên nên xét từ ngày tới tháng rồi mới tới năm
# Vì Năm mang 4 số nên có thể sử dụng len() để xác định Năm,
# Nếu Day mang giá trị đặc biệt hoặc trên 12 thì sẽ chắc chắn là ngày
# Nếu tháng mang tên tháng thì chắc chắn là tháng
# Nếu xác định được ngày hoặc tháng trước thì xác định giá trị còn lại sẽ dễ dàng
# còn nếu không thể xác định cả 2 gtri ==> rơi vào trường hợp lỗi đã được nêu ở trên
# Final ra sẽ format theo 1 nguyên tắc của thế giới
# Hoặc lấy giữ liệu của vùng và định dạng theo kiểu của vùng đó

# Có thể sử dựa vào lịch julia để xác định tính đúng đắn của dữ liệu ngày tháng được không
# Giả sử input 1 chuỗi không xác định được ngày tháng nhưng có thứ và năm
# 06 09 2019 => 06 Sep 2019 || 09 June 2019
# Friday 06 09 2019 => Friday 06 Sep 2019 

# dữ liệu xác định
# monday 1st

# Giả thuyết được đặt ra nếu Năm đưa vào chỉ là 2 chữ số: dạng định dạng yy
# Khả năng tự nhận diện 2 chữ số của %y chỉ có giới hạn là 100 năm 
# Với điểm 50 năm là lyear - 1 (2018-49 = 1969 || 2019 + 49 = 2068 )

# Nên yêu cầu data có 4 chữ số
# Hoặc khoanh vùng data với giới hạn năm cụ thể để xác định dựa trên năm hiện tại
# Vì nếu để data năm là 2 chữ số sẽ dễ xảy ra các sai số khi 
# Độ rộng năm của data lớn hơn 50 năm tính từ thời điểm hiện tại
# Tính tới tương lai hay quá khứ

# Loại bỏ trường hợp tự định dạng số năm dựa trên thứ của ngày tháng năm đó
# Khả năng: Vì mỗi 400 năm mới có 1 ngày có thứ ngày tháng trùng với thứ ngày tháng của 400 năm sau

# Đưa ra các dữ liệu với định dạng được xác định
# dd/MM/YY
# dd/mm/yy
# w/dd/mm/yy
# w/dd/mm/YY
# w/dd/MM/yy
# w/dd/MM/YY
# W/dd/mm/yy

# - 09/09/09
# - 15/09/09
# - Friday 06 09 19
# - Sat 07 July 2007
# - 07 July 07
# - July 07 07
# - 07 07 2007
# - 7th 07 07
