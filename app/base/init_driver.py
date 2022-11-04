#!/usr/bin/python 
# -*- coding: utf-8 -*-
import os

from appium import webdriver
from common.util.logger import log, files_package_dir


def init_driver():
	# 1.添加配置，创建DesiredCapabilities对象
	desired_caps = {}

	# 设备名称
	desired_caps["deviceName"] = "91QEBPL6AUCS"

	# 操作系统名称
	desired_caps["platformName"] = "Android"

	# 安装包
	desired_caps["app"] = os.path.join(files_package_dir, "demo.apk")  # appium 新版本不需要设置appPackage、appActivity等参数。

	# # 操作系统版本,即手机系统版本号。
	# desired_caps["platformVersion"] = "5.1"

	# # 应用包名
	# desired_caps["appPackage"] = "com.sz"
	#
	# # 被测试应用的入口activity
	# desired_caps["appActivity"] = "com.sz.view.common.activity.sys.StartActivity"

	# 2.创建驱动...URL是appium的固定地址；指定appium通讯的地址，将相对应的配置传入到驱动里边。
	driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

	log.info("驱动创建成功")

	# 返回驱动对象driver
	return driver


if __name__ == "__main__":
	driver = init_driver()
	driver.quit()
