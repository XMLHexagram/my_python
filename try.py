import urllib.request
import time
import requests

# 使用build_opener()是为了让python程序模仿浏览器进行访问
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]


# 专刷某个页面
print('开始刷了哦：')
tempUrl = 'https://mooc1-1.chaoxing.com/mycourse/studentstudy?chapterId=98759603&courseId=95329631&clazzid=10006650&enc=86a523aef89c06d4bf27700c9a3fdf6e'
url2 = 'https://mooc1-1.chaoxing.com/mycourse/studentstudy?chapterId=98759603&courseId=95329631&clazzid=10006650&enc=86a523aef89c06d4bf27700c9a3fdf6e'
_cookie_ = {
"Host": "i.mooc.chaoxing.com",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0",
"Accept": "text/css,*/*;q=0.1",
"Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
"Accept-Encoding": "gzip, deflate",
"Connection": "keep-alive",
"Cookie": "uname=19052220; pid=33406; _uid=104726390; uf=b2d2c93beefa90dcde9d0d2db09fc568d4368655ab00d08122a79f808f948bce4ee44e607ac55618a52e8c6364066fb9913b662843f1f4ad6d92e371d7fdf64477aa791b0b255b77fd68be96b6183b1a860518e5a4c5269d5084629c9c8e13594eba802784f70e00; _d=1570704559741; UID=104726390; vc=9EFD1B0B8B75EE06B30ED5951D1BEC76; vc2=B3093C95DDD30D97E5B1A2CC5A704B8A; vc3=Zd%2BiKR1P1BIDwlT%2FRp6hvH%2Frao%2FK2VuOKZxpSkJ%2BR4IMn49qVYD3jas1LkLXjAuDjosoILNvY2yrwRKECoP0G4rWpxW4SDWnUtTIdbTsfa2EQJdZnUCuXHz3ivcZnylG%2F9zCUxq0L2PAmcUbBVtHha2c8M%2Bf4IyiSnFhT6X29Sw%3D39b8a463a8e96362460ab49ee8431c15; DSSTASH_LOG=C_38-UN_592-US_104726390-T_1570704559744; JSESSIONID=4DDEFD4685B1FDA6D843D672964DD6CC; source=""; route=98f17f0b052079b916f022bfaec8cf55; thirdRegist=0; tl=1",
}

for j in range(300):
    try:
        # opener.open(tempUrl)
        wbdata = requests.get(tempUrl,headers=_cookie_)
        time.sleep(1)
        wbdata = requests.get(url2,headers=_cookie_)
        time.sleep(2)
        
        print('%d %s' % (j, tempUrl))
    except urllib.error.HTTPError:
        print('urllib.error.HTTPError')
        time.sleep(1)
    except urllib.error.URLError:
        print('urllib.error.URLError')
        time.sleep(1)