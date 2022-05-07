# coding:utf-8
import json
import unittest
from demo2 import RunMain
# from UniTest_Demo3 import TestMethod2


class TestMethod(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.runner = RunMain()

    def test1(self):  # unitest里面case定义必须为test开头，且是吗定义的数字顺序来执行的
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
        if res['status'] == 200:  # ！！！这是自己写的断言，但是unittest有自己的官方断言！看下面的例子！就是assert
            print('第一条用例通过！ヾ(@^▽^@)ノ')
        elif res['status'] == 500:
            print('服务器错误哦(*^▽^*)')
        else:
            print('i dont know wt happend ┓( ´∀` )┏')
        # globals()['tgb'] = 19971219
        # 全局变量定义，在pycharm中后面应用该变量会报红，不影响使用
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
        self.assertEqual(res['status'], 201, '第二条case验证失败！○･｀Д´･ ○')  # ！！！unitest的断言方法，assert，还有几种自行查找


# if __name__ == '__main__':
#     # unittest.main()
#     suite = unittest.TestSuite()  # 这一段的作用：创建TestSuite类的一个对象suite，将suite作为一个容器，把case，test1、test2加入suite这个容器中，然后执行。unitest.main是全部case执行
#     suite.addTest(TestMethod('test1'))
#     suite.addTest(TestMethod('test2'))
#     unittest.TextTestRunner().run(suite)
        # 但是在pycharm中没有意义，要想跳过可以用@unittest.skip，要想执行单挑用例直接，case名右键执行就完事了，甚至unittest.main也没意义，因为pycharm可以直接执行unittest┓( ´∀` )┏
