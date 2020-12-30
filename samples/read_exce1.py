#!/usr/bin/env python
#encoding:utf-8
#@author:k
#@file:read_excel.py
#@time:2020/12/28   15:43 下午

import os
import xlrd
from common.excel_utils import ExcelUtils

excel_path=os.path.join(os.path.dirname(__file__),'data/test_data.xlsx')
excelUtils = ExcelUtils(excel_path, 'Sheet1')
# print(excelUtils.get_merged_cell_value(4, 0))
# print(excelUtils.get_row_count())
sheet_list=[]
for row in range(1,excelUtils.get_row_count()):   #
    row_dict={}
    row_dict['事件']=excelUtils.get_merged_cell_value(row,0)
    row_dict['步骤序号'] = excelUtils.get_merged_cell_value(row, 1)
    row_dict['步骤情况'] = excelUtils.get_merged_cell_value(row, 2)
    row_dict['完成情况'] = excelUtils.get_merged_cell_value(row, 3)
    sheet_list.append(row_dict)

# for row in sheet_list:
#     print(row)


all_data_list=[]
first_row=excelUtils.sheet.row(0)
# print(first_row)
for row in range(1,excelUtils.get_row_count()):
    row_dict = {}
    for col in range(0, excelUtils.get_col_count()):
        row_dict[first_row[col].value]=excelUtils.get_merged_cell_value(row,col)
    all_data_list.append(row_dict)

for row in all_data_list:
    print(row)