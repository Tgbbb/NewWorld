# coding:utf-8
import requests
from w3lib import http

from AutoTest.ImoocInterface.data.data_config import *

http.verify = False
charles_proxies = {
    "http": "http://192.168.3.21:8888",
    "https":"http://192.168.3.21:8888"
            }


class RunMethod():
    def post_main(self, url, data, header=None):
        res = None
        if header != None:
            res = requests.post(url=url, data=data, headers=header).json()
        else:
            res = requests.post(url=url, data=data).json()
        return res

    def get_main(self, url, data=None, header=None):
        res = None
        if header != None:
            res = requests.get(url=url, data=data, headers=header).json()
        else:
            res = requests.get(url=url, data=data).json()
        return res

    def run_main(self, method, url, data=None, header=None):
        res = None
        if method == 'post':
            res = self.post_main(url, data, header)
        else:
            res = self.get_main(url, data, header)
        return res


if __name__ == '__main__':
    test = RunMethod()
    res = test.run_main('post', 'https://c.51wnl-cq.com/contentapi/api4.4.0/UserFback/UploadMsg')
    print(res)
