#!/usr/bin/python 
# -*- coding: utf-8 -*-
import socket
import struct
from datetime import date, timedelta, datetime
import random
import string
from common.util.logger import *



RANDOM_IP_POOL = ['172.168.10.222/0']

"""
生成指定长度随机字符串
"""
def get_random_str(str_len, is_number = None):

	if (isinstance(str_len, int) and str_len > 0):

		random_str = ""
		random_char_list = []

		if is_number:
			char_list = string.digits
		else:
			char_list = string.ascii_letters + string.digits

		for i in range(str_len):
			random_char = random.choice(char_list)  #随机获取一个字符
			random_char_list.append(random_char)

		random_str	= "".join(random_char_list)

		return  random_str

	else:
		raise Exception("传入参数不合法，请检查")


"""
随机生成指定范围的小数
"""
def get_random_decimals(star_value = 0, end_value = 100, precision = 1):
	if (isinstance(star_value, int) and isinstance(end_value, int) and isinstance(precision, int)):
		return round(random.uniform(star_value, end_value), precision)
	else:
		raise Exception("传入参数不合法，请检查")


"""
生成有效的手机号码
"""
def get_random_phone():

	prelist=["130", "131", "132", "133", "134", "135", "136", "137", "138", "139",
             "147", "150", "151", "152", "153", "155", "156", "157", "158", "159",
             "186", "187", "188", "189"]

	phone = random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))

	return phone


"""
返回随机的姓名
"""
def get_random_name():
	name_list = ["杰西卡·阿尔芭", "河智苑", "伊丽莎白·奥尔森", "杰森·斯坦森", "亚当·莱文", "里奥·梅西", "玛丽亚·凯莉",
	             "丹·雷诺斯", "杜阿·利帕", "约翰尼·德普", "莫妮卡·贝鲁奇", "卡梅隆·迪亚茨", "尹恩惠", "有村架纯", "华金·菲利克斯",
	             "艾莎·冈萨雷斯", "凡妮莎·柯比", "刘荷娜", "伊娃·格林", "露西·宝通", "梅丽莎·博洛纳", "李安", "艾兰·沃克", "阿黛尔", "蕾哈娜", "碧昂丝",
	             "尼古拉斯·凯奇", "威尔·史密斯"]

	return random.choice(name_list)


"""
生成有效的银行卡
"""
def get_random_bankcard_num(isSuccess = True):
	head = 621700
	middle = random.randint(10000000000, 99999999999)
	if (isSuccess):
		last2 = random.randint(3, 9)
		last1 = random.randint(4, 7)
	else:
		last2 = 8
		last1 = 0

	return str(head) + str(middle) + str(last2) + str(last1)


"""
获取地址码
"""
def get_districtcodes():

	districtcodes = []
	try:
		with open(os.path.join(config_dir, "districtcode.txt"), mode='r', encoding='utf-8') as f:
			for line in f.readlines():
				code = line.strip()[:6]
				if code:   # 排除空行
					districtcodes.append(code)
			return districtcodes
	except Exception as e:
		raise Exception("打开地址码文件失败: {}".format(e))


'''
生成ip
'''
def get_random_ip():
	str_ip = RANDOM_IP_POOL[random.randint(0, len(RANDOM_IP_POOL) - 1)]
	str_ip_addr = str_ip.split('/')[0]
	str_ip_mask = str_ip.split('/')[1]
	ip_addr = struct.unpack('>I', socket.inet_aton(str_ip_addr))[0]
	mask = 0x0
	for i in range(31, 31 - int(str_ip_mask), -1):
		mask = mask | (1 << i)
	ip_addr_min = ip_addr & (mask & 0xffffffff)
	ip_addr_max = ip_addr | (~mask & 0xffffffff)

	return socket.inet_ntoa(struct.pack('>I', random.randint(ip_addr_min, ip_addr_max)))


def get_rand_mac_address():
	Maclist = []
	for i in range(1, 7):
		RANDSTR = "".join(random.sample("0123456789abcdef", 2))
		Maclist.append(RANDSTR)
	RANDMAC = ":".join(Maclist)

	return  RANDMAC


"""
生成有效身份证号码
"""
def get_random_national_id(age_number = None, tail_number = None):

	if (isinstance(age_number, int) and age_number > 0):

		# 6位地址码
		code_list = get_districtcodes()
		id_location = code_list[random.randint(0, len(code_list)-1)]

		# 8位生日编码
		now_year = datetime.now().year  # 获取当前年份。
		if age_number is None:
			id_year = str(random.randint(now_year - 100, now_year))  # 年份项,当前年份以及前100年内的年份。
		else:
			id_year = str(now_year - int(age_number))
		id_date = date.today() + timedelta(days=random.randint(1, 366))  # 月份和日期项
		id_date = id_date.strftime("%m%d")
		id_order = str(random.randint(100, 999)) # 顺序号

		id_former = id_location + id_year + id_date + id_order  # 前17位相加

		# 验证码
		weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 权重项
		check_code = {"0": "1", "1": "0", "2": "X", "3": "9", "4": "8", "5": "7", "6": "6", "7": "5",
					  "8": "5", "9": "3", "10": "2"}  # 校验码映射
		count = 0
		for i in range(0, len(id_former)):
			count = count + int(id_former[i]) * weight[i]
		code = check_code[str(count % 11)]  # 算出校验码
		if tail_number is None or (tail_number is not None and str(tail_number) == code):  # 判断校验码是否符合预期。
			id = id_former + code
		else:  # 校验码不符合预期则重新生成，递归调用。
			id = get_random_national_id(age_number, tail_number)

		return id
	else:
		raise Exception("传入参数不合法，请检查")


"""
生成身份信息
"""
def get_random_data():
	phone = get_random_phone()
	name = get_random_name()
	national_id = get_random_national_id(age_number = 25, tail_number = "2")  # 授信和提现模型规则，3款人尾号  1-6 通过, 7-9 拒绝， X 异常。
	bank_card_num = get_random_bankcard_num()

	log.info("phone = {} name = {} national_id = {} bank_card_num = {}".format(phone, name, national_id, bank_card_num))

	return name, national_id, phone, bank_card_num





