#!/usr/bin/env python
#encoding:utf-8
#@author:k
#@file:read_excel.py
#@time:2020/12/28   15:43 下午

import os
import xlrd


excel_path=os.path.join(os.path.dirname(__file__),'data/test_data.xlsx')
print(excel_path)

wb=xlrd.open_workbook(excel_path)       #创建工作b
sheet=wb.sheet_by_name('Sheet1')    #创建表各对象
# cell_value=sheet.cell_value(0,0)    #直接取值，行列下标从0开始，row col
# print(cell_value)
# cell_value=sheet.cell_value(1,0)
# print(cell_value)
# cell_value=sheet.cell_value(2,0)    #对于合并的左上首个单元格回返回真实值
# print(cell_value)

#2,0,3,0,4,0学习python编程

#处理方式：xlrd
print(sheet.merged_cells)#返回一个列表 起始行，结束行，起始列，起始列

merged=sheet.merged_cells

#逻辑：凡是在merged_Calls属性内的单元格，它的值都幺登与左上角首格单元值
row_index=4;col_index=0

for (rlow,rhigh,clow,chigh)in merged:   #遍历表格中所有合并单元格位置信息
    if(row_index>=rlow and row_index<rhigh):    #行坐标判断
        if(col_index>=clow and col_index<chigh):    #列坐标判断
            #如果满足条件，就把合并单元格第一个位置的值赋给其它合并单元格
            cell_value=sheet.cell_value(rlow,clow)
# print(cell_value)


def get_merged_cell_value01(row_index,col_index):
    #只能完成合并单元格的数据获取
    cell_value=None
    for (rlow, rhigh, clow, chigh) in merged:
        if (row_index >= rlow and row_index < rhigh):
            if (col_index >= clow and col_index < chigh):
                cell_value=sheet.cell_value(rlow,clow)
    return cell_value

print(get_merged_cell_value01(3,0))


def get_merged_cell_value02(row_index,col_index):
    #既能获取普通单元格书籍，又能获取合并单元格的数据
    cell_value=None
    for (rlow, rhigh, clow, chigh) in merged:
        if (row_index >= rlow and row_index < rhigh):
            if (col_index >= clow and col_index < chigh):
                cell_value=sheet.cell_value(rlow,clow)
                break;  #防止循环进行判断出现值覆盖的情况
            else:
                cell_value = sheet.cell_value(row_index,col_index)
        else:
            cell_value = sheet.cell_value(row_index, col_index)
    return cell_value

print(get_merged_cell_value02(4,0))

for i in range(1,9):
    print(get_merged_cell_value02(i,0))