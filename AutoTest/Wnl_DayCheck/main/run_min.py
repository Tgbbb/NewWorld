# coding:utf-8
# 结合了写的请求获取结果（实际数据）的模块、获取excel数据（用例数据）的模块，再加上对比的模块，利用循环遍历没一条用例实现接口自动化
from AutoTest.Wnl_DayCheck.base.new_runmethod import RunMethod
from AutoTest.Wnl_DayCheck.data.get_data import Get_Data
from AutoTest.Wnl_DayCheck.util.common_util import CommonUtil
# from AutoTest.Wnl_DayCheck.base.charles_requests_test import RunMethod



class RunTest():
    def __init__(self):
        self.run_method = RunMethod()  # 初始化运行requests的实例
        self.data = Get_Data('../configdata/useexm.xlsx', 0)  # 初始化获取数据的实例
        self.compare_data = CommonUtil()  # 初始化比较数据的实例

    def go_on_data(self):
        res = None
        rows_count = self.data.get_datalines()
        for i in range(1, rows_count):  # 通过循环去遍历excel里面每条用例
            url = self.data.get_url(i)
            method = self.data.get_request_type(i)
            is_run = self.data.get_is_run(i)
            data = self.data.get_json_data(i)
            header = self.data.is_header(i)
            expect = self.data.get_expect_data(i)
            goods_ID = self.data.get_goodsid(i)
            pro_URL = self.data.get_product_url(i)
            if is_run == True:
                res = self.run_method.run_main(method, url, data, header)
                if res['data']['ads'][0]['landUrl'] == '':
                    land_url = res['data']['ads'][0]['transparentButtonUrl']
                else:
                    land_url = res['data']['ads'][0]['landUrl']  # 有些产品的链接不是在landurl
                is_test_pass = self.compare_data.is_contain(goods_ID, res['data']['ads'][0]['goodsId'], pro_URL,
                                                            land_url)  # 获得每条用例的预期结果与实际结果进行对比
                # 1：产品链接错误，2：goodsid错误，3：没有问题
                if is_test_pass == 3:
                    print('第{}条暂无问题'.format(i))
                elif is_test_pass == 1:
                    print('第{}条产品链接错误，请检查'.format(i))
                elif is_test_pass == 2:
                    print('第{}条goosid错误，请检查'.format(i))
            else:
                pass


test = RunTest()
test_result = test.go_on_data()
input("输入任意字符结束：")
