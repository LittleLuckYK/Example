#!/usr/bin/python 
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from app.base.action import Action
from common.util.logger import log


class SetPasswordPage(Action):

	# 设置密码页面元素
	password_edit = (By.ID, "com.sz:id/setting_password_edit1")
	password_again_edit = (By.ID, "com.sz:id/setting_password_edit2")
	hide_or_see_button = (By.ID, "com.sz:id/setting_password_hideorsee_btn")
	setting_done_button = (By.ID, "com.sz:id/setting_password_btn")


	def __init__(self, driver):
		Action.__init__(self, driver)

	def input_password(self, password):
		self.input_element(SetPasswordPage.password_edit, password)

	def input_password_again(self, password):
		self.input_element(SetPasswordPage.password_again_edit, password)

	def click_setting_done(self):
		self.click_element(SetPasswordPage.setting_done_button)

	def set_password(self, password):
		self.input_password(password)
		self.input_password_again(password)
		self.click_setting_done()

		log.info("设置密码完成")