#!/usr/bin/python 
# -*- coding: utf-8 -*-
import xlrd
import xlwt

from common.util.logger import log

"""
读取excel
"""
def read_excel(source_file_path):
	try:
		data = xlrd.open_workbook(source_file_path)
	except Exception as e:
		raise Exception("打开({})文件失败。{}".format(source_file_path, e))

	table = data.sheet_by_index(0)
	data_rows = []

	for row_num in range(table.nrows):
		if row_num > 0:
			data_rows.append(table.row_values(row_num))

	return data_rows


"""
解密excel
"""
def read_write_excel(souce_file, target_file):

	log.info("Decode excel souce_file = {}, target_file = {}".format(souce_file, target_file))

	wb = xlrd.open_workbook(filename=souce_file)

	workbook = xlwt.Workbook(encoding="ascii")
	worksheet = workbook.add_sheet("Sheet")

	table = wb.sheet_by_index(0)
	for i in range(table.nrows):
		for j in range(table.ncols):
			worksheet.write(i, j, str(table.cell(i, j).value))
	workbook.save(target_file)


