#!/usr/bin/python 
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from app.base.action import Action


class HomePage(Action):

	# 首页页面元素
	sz_button = (By.ID, "com.sz:id/lmod_fhome_item_cap")
	zs_button = (By.ID, "com.sz:id/lmod_fhome_item_sin")
	jsz_button = (By.ID, "com.sz:id/lmod_fhome_item_mac")
	ysz_button = (By.ID, "com.sz:id/lmod_fhome_item_pl")
	more_button = (By.ID, "com.sz:id/id_tab_bottom_more")

	def __init__(self, driver):
		Action.__init__(self, driver)

	def click_sz(self):
		self.click_element(HomePage.sz_button)

	def click_zs(self):
		self.click_element(HomePage.zs_button)

	def click_jsz(self):
		self.click_element(HomePage.jsz_button)

	def click_ysz(self):
		self.click_element(HomePage.ysz_button)

	def click_more(self):
		self.click_element(HomePage.more_button)