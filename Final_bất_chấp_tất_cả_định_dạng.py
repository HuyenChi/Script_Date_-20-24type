import datetime
from datetime import date
from datetime import *

a = ['08','09','2019']

MONTHS_B = ["january", "february", "march", "april", "may", "june","july", "august", "september","october", "november", "december"]
MONTHS_b = ["jan", "feb", "mar", "apr", "may", "jun","jul", "aug", "sep","oct", "nov", "dec"]
DAYS_A= ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
DAYS_a = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
DAY_EXTENTIONS = ["rd", "th", "st", "nd"]


# Func thực thi tạo date từ dữ liệu không xác định để so sánh
def suffle_format(text,lst_format,lst_none_fm_date):
	str_format = ['%a',0,0,0]

	str_format[lst_none_fm_date[0]] = ' '+lst_format[0]
	str_format[lst_none_fm_date[1]] = ' '+lst_format[1]
	str_format[str_format.index(0)] = ' %Y'

	str_format = ''.join(str_format)
	str_build = datetime.strptime(text, str_format)
	str_check = (datetime.strftime(str_build, str_format)).lower()
	str_end = datetime.strftime(str_build, '%A %d %B %Y')

	return str_check,str_end

# func check dữ liệu và định dạng dữ liệu bất kể có 4 hay 3 phần tử trong mảng data
def Check_format_date(text):

	count_min = 0
	months = -1
	format_months = '%m'
	lst_nb_under_12 = []
	dd = -1
	YY = -1
	w = -1
	str_test = (' '.join(text)).lower()

	# Vòng lặp kiểm tra chuỗi có đủ điều kiện là 1 chuỗi có ngày và tháng đều không dưới 12 hay không
	# Nếu ngày và tháng đều dưới 12 thì không thể nhận diện được
	# Vòng lặp còn xác định tháng và tuần trong tháng nếu có
	for i in text:
		if len(i) <= 2:
			if int(i) <= 12:
				count_min +=1
				lst_nb_under_12.append(text.index(i))
		elif i in MONTHS_b:
			months = MONTHS_b.index(i) +1
			count_min =0
		elif i in MONTHS_B:
			months = MONTHS_B.index(i) +1
			count_min =0
		elif i in DAYS_a or i in DAYS_A or i in DAY_EXTENTIONS:
			count_min =0
		elif i in DAYS_A:
			w = i
			format_w = '%A'
		elif i in DAYS_a:
			w = i
			format_w = '%a'
	# Begin
	#-------------------------------------------------------
	# Nếu count_min == 2 nhưng có thứ trong tuần
	# Có thể miễn cưỡng chạy 2 giả lập date để tìm ra giả lập trùng với thứ trong tuần

	if count_min == 2 and w !=-1:
		# Tạo chuỗi so sánh sử dụng func suffle_format
		# Với mỗi định dạng khác nhau sẽ đưa ra 1 kết quả khác nhau
		# Nếu kết quả nào giống với chuỗi ban đầu sẽ return 
		str_final = suffle_format(str_test,['%d','%m'],lst_nb_under_12)
		if str_final[0] == str_test:
			str_final = str_final[1]
			# print('True')		
			# print(str_final)
			return str_final
		else:
			str_final = suffle_format(str_test,['%m','%d'],lst_nb_under_12)
			if str_final[0] == str_test:
				str_final = str_final[1]
				# print('True')		
				# print(str_final)
				return str_final
			else:
				# print('Dữ liệu lỗi tùm lum đéo sửa được đâu')
				return'Dữ liệu lỗi tùm lum đéo sửa được đâu'

	# Nếu Count_min = 2 tương ứng với có dữ liệu ngày và tháng cùng không thể xác định
	# Kèm theo không có dữ liệu là thứ trong tuần
	# Sẽ dừng tại đây và báo lỗi
	if count_min == 2 and w == -1:
		return 'Dữ liệu không thể phân tích'
	# Affter
	#--------------------------------------------------------------
	# Begin
	# Vòng lặp phân tách dữ liệu trong mảng
	# Kiểm tra từng điều kiện để nhận dạng dữ liệu thuộc kiểu dữ liệu nào
	for i in text:
		# Tìm ra ngày trong tuần hoặc tháng hoặc nday_ext nhưng có 3 chữ số
		if len(i) == 3:
			if i.lower() in MONTHS_b:
				mm = i
			else:
				for ext in DAY_EXTENTIONS:
					if ext in i:
						c = i.find(ext)
						dd = i[:c]
		# Tìm ra năm hoặc day_ext 4 chữ số
		elif len(i) == 4 and YY == -1:
			try:
				YY = int(i)
				YY = str(YY)
			except ValueError:
				for ext in DAY_EXTENTIONS:
					if ext in i:
						c = i.find(ext)
						dd = i[:c]
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
		elif len(i) <=2:
			if int(i) <= 12 and months != -1:
				dd = i
			elif int(i) > 12:
				dd = i
			else:
				months = i
	# Affter
	#--------------------------------------------------------------------------------

	# Nếu tháng là số có 1 chữ số
	# Cần phải đưa về dạng 2 chữ số để tạo chuỗi so sánh với đúng format của datetime
	if months < 10:
		months = '0' + str(months)
	# Begin
	#--------------------------------------------------------------------------------
	# Sau khi có tất cả thông tin
	# Dựng lại chuỗi để so sánh với chuỗi được tạo bằng datetime
	# Mục đích kiểm tra thứ ngày tháng có trùng hợp, liên kết với nhau không

	# Kiểm tra với chuỗi có thứ trông tuần
	if w != -1:
		# Tạo ra chuỗi ngày tháng hoàn chỉnh và so sánh
		str_base = str(w) +' '+str(dd) +' '+ str(months) +' '+ str(YY)
		str_a = datetime.strptime(str_base, f'{format_w} %d {format_months} %Y')
		str_b = (datetime.strftime(str_a, f'{format_w} %d {format_months} %Y')).lower()
		str_c = (datetime.strftime(str_a, f'%A %d %B %Y'))
		if str_base == str_b:
			return str_c
		# Nếu chuỗi sai có thể thông báo là chuỗi sai hoặc đưa ra chuỗi đúng với giá trị ngày tháng
		else:
			return str_c
	# Với chuỗi không có thứ trong tuần, dựng chuỗi date theo datetime và return
	else:
		str_base = str(dd) +' '+ str(months) +' '+ str(YY)
		str_a = datetime.strptime(str_base, f'%d {format_months} %Y')
		str_b = (datetime.strftime(str_a, f'%A %d %B %Y'))
		return str_b

b = Check_format_date(a)
print(b)
# Dựa vào thứ trong để định dạng gần đúng nhất giá trị ngày tháng có trong mảng

# Phác thảo: 
# Hypothesis 1: Cả 2 dữ liệu tháng và năm đều không thể xác định
# Chọn số thứ nhất làm tháng số thứ 2 làm ngày và duyệt như bình thường
# Nếu không thì đổi ngược lại
# Nếu sai báo lỗi

# Vì đã có vị trí của 2 số dưới 12, có vị trí của w tìm vị trí của năm.








# str_test = ['sun','09', '08', '2019']
# str_test = (' '.join(str_test)).lower()
# lst_nb_under = [1,2]
# # lst_format = ['%d','%m']

# def suffle_format(text,lst_format,lst_none_fm_date):
# 	str_format = ['%a',0,0,0]

# 	str_format[lst_none_fm_date[0]] = ' '+lst_format[0]
# 	str_format[lst_none_fm_date[1]] = ' '+lst_format[1]
# 	str_format[str_format.index(0)] = ' %Y'

# 	str_format = ''.join(str_format)
# 	str_build = datetime.strptime(text, str_format)
# 	str_check = (datetime.strftime(str_build, str_format)).lower()
# 	str_end = datetime.strftime(str_build, '%A %d %B %Y')

# 	return str_check,str_end


# str_final = suffle_format(str_test,['%d','%m'],lst_nb_under)
# if str_final[0] == str_test:
# 	str_final = str_final[1]
# 	# print('True')		
# 	# print(str_final)
# 	return str_final
# else:
# 	str_final = suffle_format(str_test,['%m','%d'],lst_nb_under)
# 	if str_final[0] == str_test:
# 		str_final = str_final[1]
# 		# print('True')		
# 		# print(str_final)
# 		return str_final
# 	else:
# 		# print('Dữ liệu lỗi tùm lum đéo sửa được đâu')
# 		return'Dữ liệu lỗi tùm lum đéo sửa được đâu'

