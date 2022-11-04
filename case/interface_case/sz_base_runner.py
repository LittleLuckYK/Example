#!/usr/bin/python 
# -*- coding: utf-8 -*-
import decimal

from case.interface_case.base_runner import BaseRunner
from common.enums.system_enum import SmsTypeEnum
from interface.finance.sz_user_interface import SZUserInterface


class SZBaseRunner(BaseRunner):

	# 公共配置
	verification_code = "ABC" # App通用验证码
	sms_type = str(SmsTypeEnum.REGISTER.value)
	password = "123456" # App登录密码

	# 项目
	user_info = SZUserInterface()






