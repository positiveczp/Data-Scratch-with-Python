#-*-coding:utf-8-*-
# xlrd & xlwt_module test

import xlrd
import xlwt
from xlutils.copy import copy

#========xlrd=======================
#打开excel
data = xlrd.open_workbook('test.xlsx')
#查看文件中包含sheet的名称
data.sheet_names()
#通过索引或名称得到工作表
table1 = data.sheets()[0]
table2 = data.sheet_by_index(1)
table3 = data.sheet_by_name(u'three')
#获取行数和列数
ncols = table1.ncols
nrows = table1.nrows
#获取整行和整列的值，返回列表
table1.row_values(0)
table1.col_values(0)
#循环行，返回每行值得列表
for rownum in range(table1.nrows):
    table1.row_values(rownum)
#单元格
cell_A1 = table1.cell(0,0).value
cell_C3 = table1.cell(2,2).value
#分别使用行列索引
cell_A1 = table1.row(0)[0].value
cell_A2 = table1.col(1)[0].value
#简单的写入
row = 0
col = 0
#0-empty 1-string 2-number 3-date 4-boolean 5-error
ctype = 1
value = 'chenziping'
#扩展的格式化，默认是0
xf = 0
table1.put_cell(row,col,ctype,value,xf)
table1.cell(0,0)
table1.cell(0,0).value

#========xlwt=======================
#新建一个excel文件
file = xlwt.Workbook()
#新建一个sheet
table = file.add_sheet('czp1',cell_overwrite_ok=True)
#写入数据table.write(行，列，data)
table.write(0,0,'test')
#保存文件
file.save('test2.xls')
#初始化样式，并为样式创建字体
style = xlwt.XFStyle()
font = xlwt.Font()
font.name = 'Times New Roman'
font.bold = True
#为样式设置字体
style.font = font
#使用样式
table.write(0,1,'test',style)
#写完保存
file.save('test2.xls')

#=======xlutils===========================
rb = xlrd.open_workbook('test2.xls')
wb = copy(rb)
#通过get_sheet()获取的sheet有write()方法
ws = wb.get_sheet(0)
ws.write(0,0,'changed')
wb.save('test2.xls')









