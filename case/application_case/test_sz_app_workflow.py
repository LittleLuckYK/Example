#!/usr/bin/python 
# -*- coding: utf-8 -*-
import time


from app.pages.page_common.home_page import HomePage
from app.pages.page_common.login_page import LoginPage
from app.pages.page_common.register_page import RegisterPage
from app.pages.page_common.set_password_page import SetPasswordPage
from app.pages.page_common.start_page import StartPage
from case.interface_case.sz_base_runner import SZBaseRunner



class TestSZAppWorkFlow(SZBaseRunner):
	def test_sz_app_workflow(self, base_data, portal_login_token, driver):

		# 获取基础数据
		name, national_id, phone, bank_card_num = base_data

		# 启动页
		StartPage(driver).click_agree()  # 点击启动页同意按钮

		# 新用户注册
		HomePage(driver).click_more()  # 点击更多按钮
		LoginPage(driver).click_new_user_register()  # 点击新用户注册按钮
		RegisterPage(driver).register(phone, self.verification_code)  # 注册
		SetPasswordPage(driver).set_password(self.password)  # 设置密码





if __name__ == "__main__":
	pass
