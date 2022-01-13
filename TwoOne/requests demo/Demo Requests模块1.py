import requests

data= {
    'first': 'true',
    'pn': '1',
    'kd': 'python'

}
headers = {
    'Referer': 'https://www.lagou.com/jobs/list_python/p-city_5?&cl=false&fromSearch=true&labelWords=&suginput=&isSchoolJob=1',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36 OPR/63.0.3368.107 (Edition B2)',
    'Cookie':'privacyPolicyPopup=false; user_trace_token=20190920230530-7bf37157-4e27-4cd8-928f-ab86e8a324ad; _ga=GA1.2.1943003979.1568991931; LGUID=20190920230531-170f307c-dbb8-11e9-9452-525400f775ce; JSESSIONID=ABAAABAAAGFABEFC906D44066EFFF73292A2B8FF06FB011; WEBTJ-ID=20190920230551-16d4f353c8c1da-0dd8a75b40b34e-63282275-1327104-16d4f353c8d490; index_location_city=%E5%85%A8%E5%9B%BD; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1568991931,1570951709,1570951715; _gid=GA1.2.1860448251.1570951715; LGSID=20191013152836-11c0f6ce-ed8b-11e9-a582-5254005c3644; PRE_UTM=; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DRq47aUb2Yw8vhLMXaT6au-n68a_Y56keTq11XeqZas3%26wd%3D%26eqid%3Dc206065e00173e14000000065da2d21a; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; sajssdk_2015_cross_new_user=1; TG-TRACK-CODE=search_code; X_MIDDLE_TOKEN=d3e4db633620a8e372e79dc7ae9dcbd8; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216dc404f7d3187-0f576820c597e2-78730b2a-1327104-16dc404f7d6470%22%2C%22%24device_id%22%3A%2216dc404f7d3187-0f576820c597e2-78730b2a-1327104-16dc404f7d6470%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; gate_login_token=b21ef2026f40f3d2874b54d93f06003e091bbb4edc1d01a900f931adfbeec183; LG_HAS_LOGIN=1; _putrc=BB4D452E5D8E22DA123F89F2B170EADC; login=true; hasDeliver=0; unick=%E6%8B%89%E5%8B%BE%E7%94%A8%E6%88%B77120; X_HTTP_TOKEN=3c8ae41aae39566292925907511595b9b5fe732120; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1570952928; LGRID=20191013154849-e4ff9c55-ed8d-11e9-9acb-525400f775ce; SEARCH_ID=a066babbf2ec4735a3629ad33d17d7c0'
}

response = requests.post('https://www.lagou.com/jobs/positionAjax.json?city=%E9%87%8D%E5%BA%86&needAddtionalResult=false&isSchoolJob=1',data = data,headers=headers)
print(response.text)
