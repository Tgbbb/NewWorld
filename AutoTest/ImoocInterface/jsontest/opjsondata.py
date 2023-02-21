# coding:utf-8
from AutoTest.ImoocInterface.util.opjson import Opjson
from AutoTest.ImoocInterface.util.opexcel import OpExcel
from AutoTest.ImoocInterface.data.data_config import *
class opqq():
    def abc(self):
        tgb = Opjson('../configdata/Data.json')
        data = tgb.get_jsondata("commonbody")

        return data
tgb = opqq()
print(tgb.abc())