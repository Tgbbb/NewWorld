# coding:utf-8
import json
import unittest
from demo2 import RunMain


class TestMethod(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.runner = RunMain()
    def test1(self):
        url = 'https://c.51wnl-cq.com/contentapi/api4.4.0/UserFback/UploadMsg'
        data = {'deviceId': 'ceba49ff223e6af516c629f3a02b7a2d',
                'msgContent': '自动化测试',
                'av': '6.2.6',
                'osVer': '8.1.0',
                'msgImg': '',
                'msgType': '0',
                'appId': 'wnl_android'}
        headers = {'method': 'POST',
                   'authority': 'c.51wnl-cq.com',
                   'scheme': 'https',
                   'path': '/contentapi/api4.4.0/UserFback/UploadMsg',
                   'content-length': '128',
                   'accept': 'application/json, text/plain, */*',
                   'origin': 'https://mobile.51wnl-cq.com',
                   'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; 16th Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.159 Mobile Safari/537.36 ylna/1.0(mixad;kwtp;jrttsp;jrtttpsnf;gdtpl;jrttmr;ylad;jrttmsn;jrttmsp;mixpad;kwsn;ylspad;jrtt;kwsp;jrtttpsn;kw;xg;xmad;baidusp;jrtttp;xm;jdsp;xmsn;gdtsn;baidu;gdtv2;xmsp;gdtsp;jrttm;baidusn;jdad;)  wnlver/6002006 wnl 6.2.6',
                   'content-type': 'application/x-www-form-urlencoded',
                   'referer': 'https://mobile.51wnl-cq.com/feedback/?pushToken=AsxMhEO8ouBZlH-15f-hiHTvMmSEL_sebeqWQBpm-IVr&osver=8.1.0&appver=6.2.6&deviceType=16th&deviceId=ceba49ff223e6af516c629f3a02b7a2d&userId=qq20210611102810514&versioncode=6002006',
                   'accept-encoding': 'gzip, deflate',
                   'accept-language	': 'zh-CN,en-US;q=0.9',
                   'x-requested-with': 'com.youloft.calendar'

                   }
        print('这个是第一条测试case')
        res = self.runner.run_main('POST', url, headers, data)
        if res['status'] == 200:  # 这是自己写的断言，但是unittest有自己的官方断言！看下面的例子！就是assert
            print('第一条用例通过！ヾ(@^▽^@)ノ')
        elif res['status'] == 500:
            print('服务器错误哦(*^▽^*)')
        else:
            print('i dont know wt happend ┓( ´∀` )┏')
    def test2(self):
        url = 'https://c.51wnl-cq.com/contentapi/api4.4.0/UserFback/UploadMsg'
        data = {'deviceId': 'ceba49ff223e6af516c629f3a02b7a2d',
                'msgContent': '测试推送',
                'av': '6.2.6',
                'osVer': '8.1.0',
                'msgImg': '',
                'msgType': '0',
                'appId': 'wnl_android'}
        headers = {'method': 'POST',
                   'authority': 'c.51wnl-cq.com',
                   'scheme': 'https',
                   'path': '/contentapi/api4.4.0/UserFback/UploadMsg',
                   'content-length': '128',
                   'accept': 'application/json, text/plain, */*',
                   'origin': 'https://mobile.51wnl-cq.com',
                   'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; 16th Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.159 Mobile Safari/537.36 ylna/1.0(mixad;kwtp;jrttsp;jrtttpsnf;gdtpl;jrttmr;ylad;jrttmsn;jrttmsp;mixpad;kwsn;ylspad;jrtt;kwsp;jrtttpsn;kw;xg;xmad;baidusp;jrtttp;xm;jdsp;xmsn;gdtsn;baidu;gdtv2;xmsp;gdtsp;jrttm;baidusn;jdad;)  wnlver/6002006 wnl 6.2.6',
                   'content-type': 'application/x-www-form-urlencoded',
                   'referer': 'https://mobile.51wnl-cq.com/feedback/?pushToken=AsxMhEO8ouBZlH-15f-hiHTvMmSEL_sebeqWQBpm-IVr&osver=8.1.0&appver=6.2.6&deviceType=16th&deviceId=ceba49ff223e6af516c629f3a02b7a2d&userId=qq20210611102810514&versioncode=6002006',
                   'accept-encoding': 'gzip, deflate',
                   'accept-language	': 'zh-CN,en-US;q=0.9',
                   'x-requested-with': 'com.youloft.calendar'

                   }
        print('这个是第二条测试case')
        res = self.runner.run_main('POST', url, headers, data)
        self.assertEqual(res['status'], 201, '第二条case验证失败！○･｀Д´･ ○')



if __name__ == '__main__':
    unittest.main()
