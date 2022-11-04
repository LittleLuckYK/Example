#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from app.base.action import Action
from common.util.logger import log


class LoginPage(Action):

	# 登录页面元素
	account_login_button = (By.ID, "com.sz:id/login_account_layout")  # 账户登录按钮
	new_user_register_button = (By.ID, "com.sz:id/login_regist_layout")  # 新用户注册按钮
	phone_edit = (By.ID, "com.sz:id/login_account_phone_edit")  # 手机号码输入框
	password_edit = (By.ID, "com.sz:id/login_account_pwd_edit")  # 登录密码输入框
	verify_code_edit = (By.ID, "com.sz:id/login_verify_code_edt")  # 图形验证码输入框
	verify_code_img_button = (By.ID, "com.sz:id/login_verify_code_img")  # 图形验证码按钮
	login_button = (By.ID, "com.sz:id/login_commit_btn")  # 登录按钮
	forget_password_button = (By.ID, "com.sz:id/login_forget_password_text")  # 忘记密码按钮

	def __init__(self, driver):
		Action.__init__(self, driver)

	def click_account_login(self):
		self.click_element(LoginPage.account_login_button)

	def click_new_user_register(self):
		self.click_element(LoginPage.new_user_register_button)

	def click_verify_code(self):
		self.click_element(LoginPage.verify_code_img_button)

	def input_phone(self, phone):
		self.input_element(LoginPage.phone_edit, phone)

	def input_password(self, password):
		self.input_element(LoginPage.password_edit, password)

	def input_verify_code(self, verify_code):
		self.input_element(LoginPage.verify_code_edit, verify_code)

	def click_login(self):
		self.click_element(LoginPage.login_button)

	def click_forget_password(self):
		self.click_element(LoginPage.forget_password_button)


	"""
	登录流程
	"""
	def login_account(self, phone, password, verify_code):
		self.input_phone(phone)
		self.input_password(password)
		self.input_verify_code(verify_code)
		self.click_login()

		log.info("登录成功")
