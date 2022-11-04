#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from app.base.action import Action
from common.service.notification_service import NotificationService


class RegisterPage(Action):

	# 注册页面元素
	account_login_button = (By.ID, "com.sz:id/login_account_layout")  # 账户登录按钮
	new_user_register_button = (By.ID, "com.sz:id/login_regist_layout")  # 新用户注册按钮
	phone_edit = (By.ID, "com.sz:id/login_regist_phone_edit")  # 手机号码输入框
	verify_code_edit = (By.ID, "com.sz:id/login_regist_verify_code_edt")  # 图形验证码输入框
	verify_code_img_button = (By.ID, "com.sz:id/login_regist_verify_code_img")  # 图形验证码按钮
	sms_code_edit = (By.ID, "com.sz:id/login_regist_sms_edit")  # 短信验证码输入框
	send_sms_button = (By.ID, "com.sz:id/login_regist_getsms_btn")  # 获取验证码按钮
	register_button = (By.ID, "com.sz:id/login_commit_btn")  # 立即注册按钮
	protocol_button = (By.ID, "com.sz:id/login_checkbox")  # 勾选协议按钮

	def __init__(self, driver):
		Action.__init__(self, driver)

	def click_account_login(self):
		self.click_element(RegisterPage.account_login_button)

	def click_new_user_register(self):
		self.click_element(RegisterPage.new_user_register_button)

	def input_phone(self, phone):
		self.input_element(RegisterPage.phone_edit, phone)

	def click_verify_code(self):
		self.click_element(RegisterPage.verify_code_img_button)

	def input_verify_code(self, verify_code):
		self.input_element(RegisterPage.verify_code_edit, verify_code)

	def click_send_sms(self):
		self.click_element(RegisterPage.send_sms_button)

	def input_sms_code(self, sms_code):
		self.input_element(RegisterPage.sms_code_edit, sms_code)

	def click_register(self):
		self.click_element(RegisterPage.register_button)

	def click_protocol(self):
		self.click_element(RegisterPage.protocol_button)


	"""
	注册流程
	"""
	def register(self, phone, verify_code):
		self.input_phone(phone)
		self.input_verify_code(verify_code)
		self.click_protocol()
		self.click_send_sms()
		sms_code = NotificationService().get_sms_code(phone)  # 获取数据库中的验证码
		self.input_sms_code(sms_code)
		self.click_register()
