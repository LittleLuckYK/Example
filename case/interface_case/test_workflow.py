#!/usr/bin/python 
# -*- coding: utf-8 -*-
import pytest
import allure
from case.interface_case.sz_base_runner import  SZBaseRunner
from common.assertion.assertion import Assertion
from data.finance_data.sz_user_test_data import SZUserTestData




# @pytest.mark.skip(reason="no way of currently testing this")
@pytest.mark.sz
@allure.feature("登陆功能")
class TestWorkFlow(SZBaseRunner):

	def test_case_workflow(self, preare_data_sz):

		# 获取基础数据
		name, national_id, phone, bank_card_num, req_sn, portal_login_token = preare_data_sz

		# 登录,获取token。
		rsp = self.user_info.login_by_password(SZUserTestData.login_by_password_test_data(phone, self.password, self.sms_type))
		user_login_token = Assertion.get_app_login_token(rsp)







if __name__ == "__main__":
	pytest.main()




