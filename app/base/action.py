#!/usr/bin/python 
# -*- coding: utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait
from common.util.logger import log


class Action():
	def __init__(self, driver):
		self.driver = driver

	"""
	二次封装find_element方法
	"""
	def find_element(self, locator, timeout = 30):
		try:
			element = WebDriverWait(self.driver, timeout).until(lambda x : x.find_element(*locator))
		except Exception as e:
			raise Exception("获取页面元素失败: 元素{} 异常信息{}".format(locator, e))
		return element or None


	"""
	二次封装click方法
	"""
	def click_element(self, locator):
		self.find_element(locator).click()


	"""
	二次封装inupt方法
	"""
	def input_element(self, locator, text):
		inp = self.find_element(locator)
		inp.clear()
		inp.send_keys(text)

	"""
	获取屏幕分辨率
	"""
	def get_resolution(self):
		resolution = self.driver.get_window_size()
		width = resolution["width"]
		heigh = resolution["height"]

		return width, heigh

	"""
	获得控件大小
	"""
	def get_control_size(self, locator):
		control_size = self.find_element(locator).size

		width = control_size["width"]
		height = control_size["height"]

		return width, height

	"""
	获得控件开始坐标
	"""
	def get_control_start_location(self, locator):
		start_location = self.find_element(locator).location
		start_loc_x = start_location["x"]
		start_loc_y = start_location["y"]

		return start_loc_x, start_loc_y


	"""
	获得控件滑动坐标
	"""
	def get_control_location(self, locator):
		start_location_x, start_location_y = self.get_control_start_location(locator)
		width, height = self.get_control_size(locator)

		return start_location_x, start_location_y, width, height

	"""
	向上滑动，包含控件滑动。
	"""
	def swipe_up(self, width, height, start_location_x = 0, start_location_y = 0, t = 500, n = 1):

		x1 = float(width * 0.5) + float(start_location_x)
		y1 = float(height * 0.75) + float(start_location_y)
		y2 = float(height * 0.25) + float(start_location_y)

		for i in range(n):
			self.driver.swipe(x1, y1, x1, y2, t)


	"""
	向下滑动
	"""
	def swipe_down(self, t = 500, n = 1):
		width, height = self.get_resolution()

		x1 = width * 0.5
		y1 = height * 0.25
		y2 = height * 0.75

		for i in range(n):
			self.driver.swipe(x1, y1, x1, y2, t)

	"""
	向左滑动
	"""
	def swipe_left(self, t = 500, n = 1):
		width, height = self.get_resolution()

		x1 = width * 0.75
		x2 = width * 0.25
		y1 = height * 0.5

		for i in range(n):
			self.driver.swipe(x1, y1, x2, y1, t)

	"""
	向右滑动
	"""
	def swipe_right(self, t = 500, n = 1):
		width, height = self.get_resolution()

		x1 = width * 0.25
		x2 = width * 0.75
		y1 = height * 0.5

		for i in range(n):
			self.driver.swipe(x1, y1, x2, y1, t)