#!/usr/bin/python 
# -*- coding: utf-8 -*-
import allure
import pytest
import redis

from common.util.logger import log
from common.util.random_data import get_random_data
import re


@allure.feature("测试功能")
class TestDemo:
	@allure.story("测试用例1")
	def test_case_001(self):
		log.info("测试用例001")

		r = redis.Redis(host = "172.31.1.13",  port = 6379, decode_responses = True)
		key = "uw:rate:30H:1016651:guarantee:null:api"
		log.info(r.get(key))


	@allure.story("测试用例2")
	def test_case_002(self, preare):
		name, national_id, phone, bank_card_num = preare
		log.info("测试用例002")
		log.info(name)

	# @pytest.mark.skip(reason="no way of currently testing this")
	@pytest.mark.parametrize("var", [(1, 2, 3)])
	@allure.story("测试用例3")
	def test_case_003(self, var):
		for index in var:
			log.info("测试用例003 {}".format(index))











if __name__ == "__main__":
	pytest.main()