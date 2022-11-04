#!/usr/bin/python 
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from app.base.action import Action


class StartPage(Action):

	# 启动页弹框元素
	agree_button = (By.ID, "com.sz:id/txt_ldp_ok")  # 同意按钮
	disagree_button = (By.ID, "com.sz:id/txt_ldp_cancel")  # 不同意按钮

	def __init__(self, driver):
		Action.__init__(self, driver)

	# 点击同意
	def click_agree(self):
		self.click_element(StartPage.agree_button)

	# 点击不同意
	def click_disagree(self):
		self.click_element(StartPage.disagree_button)