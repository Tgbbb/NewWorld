import requests
import json

class RunMain:

    def __init__(self, method, url, headers, data):
        self.res = self.run_main(method, url, headers, data)

    def send_post(self, url, headers, data):
        res = requests.post(url=url, data=data, headers=headers)
        return res.json()

    def send_get(self, url, headers, data):
        res = requests.get(url=url, data=data, headers=headers)
        return res.json()

    def run_main(self, method, url, headers = None, data = None): # 这里data = None，如果是get请求，参数在链接里这种情况就可以适用
        res = None
        if method == 'GET':
            res = self.send_get(url, headers, data)
        elif method == 'POST':
            res = self.send_post(url, headers, data)
        else:
            print('请输入正确的请求方法！')
        return res
if __name__ == '__main__': 
    # get请求'https://r.51wnl-cq.com/api/RemindWindow/GetRemindWindow?userType=0&sign=82AB43C27F1292F1317563F24B92BF2F&uid=qq20210611102810514&bd=com.youloft.calendar&chn2=10010&oudid=b97c5240e65b3528&imsi=460115569587813&mac=02%253A00%253A00%253A00%253A00%253A00&imei1=866778031111036&model=16th&lang=zh&dpi=3.0&brand=Meizu&height=2160&hmscorever=&cc=CN&ov=8.1.0&idfa=b97c5240e65b3528&chn=10010-0&ppi=480&carrier=2&av=6.2.8&hwappstorever=&width=1080&imei=86677803111102&did=0bebb3adea64fe0b5ea3ecbdfabd7d55&cid=Youloft_Android&userid=qq20210611102810514&deviceid=0bebb3adea64fe0b5ea3ecbdfabd7d55&city=101060101&nt=0&t=1649917817&v=1.0&tkn=D0513B7CEF494E82AEAFDFF7B2183ECF&signtimestamp=1649917817&citycode=101060101&autoCityCode=101040700&calculate=0&strategy=1002&bsid=5be162691000001499126993&utkn=AsxMhEO8ouBZlH-15f-hiHTvMmSEL_sebeqWQBpm-IVr&lng=0&lon=0&lat=0&logintoken=19764988d594484fbb289a31a6b06cff&calendarType=basics&authtime=1649917817&authsign=9e9e05030a7e977372f44e2ea4f96b51&product=meizu_16th_CN&vaid=&clienttime=1649917817712'
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
    run = RunMain('POST', url, headers, data)
    print(run.res)
    # 小tips，关于函数return的值，你不去执行函数！函数就不会返回值，那个值你就不能调用！很简单的东西！记住哦！
    # run = RunMain()
    # print(run.run_main('POST', url, headers, data))
