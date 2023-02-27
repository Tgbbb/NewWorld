# coding:utf-8
from AutoTest.Wnl_DayCheck.util.opexcel import OpExcel
from AutoTest.Wnl_DayCheck.util.opjson import Opjson
# from time_test import tomorrow_timestamp
from AutoTest.Wnl_DayCheck.data.data_config import *
import chardet

import json
import xlrd
from AutoTest.Wnl_DayCheck.util import *


class Get_Data():  # file_path为文件路径，sheet_id为
    def __init__(self, file_path=None, sheet_id=None):
        self.file_path = file_path
        self.sheet_id = sheet_id
        self.oprea_excel = OpExcel(self.file_path, self.sheet_id)

    def get_is_run(self, row):  # 判断该条用例是否执行
        flag = None
        col = get_run()
        run_model = self.oprea_excel.op_data(row, col)
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag

    def is_header(self, row):
        col = get_Header()  # 判断是否有header
        header = self.oprea_excel.op_data(row, col)
        if header == 'yes':
            return header_test_data()  # 如果有header就返回header的值，正常这个值存在json文件中去读取，这里写死举个例子
        else:
            return None

    # def get_ID(self, row):  # 获取数据的id
    #     col = get_id()
    #     ID = self.file.op_data(row, col)
    #     return ID
    def get_request_type(self, row):
        col = get_Request_Type()  # 获取请求类型
        request_type = self.oprea_excel.op_data(row, col)
        return request_type

    def get_url(self, row):  # 获取url
        col = get_Url()
        url = self.oprea_excel.op_data(row, col)
        # time_data = tomorrow_timestamp()
        # url_origin = self.oprea_excel.op_data(row, col)  # 替换请求时间戳的方法
        # url = url_origin.replace('1677225246', time_data.tomorowtime())

        return url

    def get_request_body(self, row):
        col = get_Request_Data()
        data_id = self.oprea_excel.op_data(row, col)
        if data_id == '':  # 获取到data数据的关键key
            return None

        return data_id

    def get_json_data(self, row):  # 通过关键key获取json数据
        body = Opjson('../configdata/Data.json')  # 一定注意！！你传文件的路径
        request_data = body.get_jsondata(self.get_request_body(row))
        return request_data

    def get_expect_data(self, row):
        col = get_Expect()
        expect_data = self.oprea_excel.op_data(row, col)
        return expect_data

    def get_goodsid(self, row):
        col = get_case_goodsid()
        goodsid = self.oprea_excel.op_data(row, col)
        return goodsid

    def get_product_url(self, row):
        col = get_data_product_url()
        product_url = self.oprea_excel.op_data(row, col)
        return product_url

    def get_datalines(self):  # 获取数据的行数
        lines = self.oprea_excel.get_lines()
        return lines


if __name__ == '__main__':
    test = Get_Data('../configdata/useexm.xlsx', 0)
    # codeer2 = chardet.detect(codeer)  # 看下它是什么编码的
    # print(codeer2)
    # print(test.get_datalines())
    # print(test.get_json_data(1))
    # print(test.get_product_url(1))
    # print(test.get_goodsid(1))
    print(test.get_url(1))
