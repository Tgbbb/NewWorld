# coding:utf-8
#封装操作excel的包
import xlrd
import xlwt
import sys


# data = xlrd.open_workbook('../configdata/useexm.xlsx')
# tables = data.sheets()[0]
# print(tables.nrows)
# print(tables.cell_value(1, 1))


class OpExcel():
    def __init__(self, file_path=None, sheet_id=None):
        if file_path:  # if直接加个变量名,判断这个变量是否有值
            self.file_path = file_path
            self.sheet_id = sheet_id
            self.data_tales = self.get_data()
        else:  # 如果没值，赋予一个默认值
            self.file_path = '../configdata/useexm_test.xlsx'
            self.sheet_id = 0

    def get_data(self):
        data = xlrd.open_workbook(self.file_path)
        data_tables = data.sheets()[self.sheet_id]
        return data_tables

    # 获取单元格行数
    def get_lines(self):
        return self.data_tales.nrows

    def op_data(self, row=0, col=0):  # 同一个类中直接调用其他函数
        return self.data_tales.cell_value(row, col)


if __name__ == '__main__':
    # opera = OpExcel('../configdata/useexm.xlsx', 0)
    # data_tables = opera.get_data()
    # data_tables1 = opera.op_data()
    # print(data_tables1)
    # print(data_tables.cell_value(1, 1))
    opra = OpExcel('../configdata/useexm_test.xlsx', 0)
    # opra.op_data(1, 1)
    # print(opra.get_lines())
    print(opra.op_data(1, 1))
