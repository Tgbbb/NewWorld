# coding:utf-8
import sys

sys.path.append("C:/Users/Administrator/PycharmProjects/NewWorld/AutoTest/ImoocInterface")
from AutoTest.ImoocInterface.base.new_runmethod import RunMethod
from AutoTest.ImoocInterface.data.get_data import Get_Data
# from AutoTest.ImoocInterface.base.charles_requests_test import RunMethod
from AutoTest.ImoocInterface.util.opexcel import OpExcel


class RunTest():
    def __init__(self):
        self.run_method = RunMethod()
        self.data = Get_Data('../configdata/useexm.xlsx', 0)

    def go_on_data(self):
        res = None
        result = []
        rows_count = self.data.get_datalines()
        for i in range(1, rows_count):
            url = self.data.get_url(i)
            method = self.data.get_request_type(i)
            is_run = self.data.get_is_run(i)
            data = self.data.get_json_data(i)
            header = self.data.is_header(i)
            if is_run == True:
                res = self.run_method.run_main(method, url, data, header)
            else:
                pass
        return res


if __name__ == '__main__':
    test = RunTest()
    res = test.go_on_data()
    print(res)
