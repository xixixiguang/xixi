#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from xlrd import open_workbook # xlrd用于读取xld
import xlwt  # 用于写入xls
def readExcel(path, row):
    workbook = open_workbook(path.decode("utf-8"))  # 打开xls文件
    sheet_name= workbook.sheet_names()  # 打印所有sheet名称，是个列表
    sheet = workbook.sheet_by_index(0)  # 根据sheet索引读取sheet中的所有内容
    sheet1= workbook.sheet_by_name('Sheet1')  # 根据sheet名称读取sheet中的所有内容
    print(sheet.name, sheet.nrows, sheet.ncols)  # sheet的名称、行数、列数
    return sheet.row_values(row)

for row in range(0, 20):
    print(row, readExcel(r"D:/slp/这是.xls", row))
    for i in readExcel(r"D:/slp/这是.xls", row):
        print i

