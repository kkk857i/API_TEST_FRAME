
#用requests完成发帖

import requests
import re
from collections import OrderedDict

hosts='http://47.107.178.45'

session=requests.session()  #创建一个session对象


#01进入首页
res01=session.get(url=hosts+'/phpwind/')
# print(res01.content.decode('utf-8'))
body01=res01.content.decode('utf-8')
token_id=re.findall('name="csrf_token" value="(.+?)"/>',body01)[0];
# print(token_id)

#02,输入用户名密码登陆
get_params={
    'm':'u',
    'c':'login',
    'a':'dologin'
}
form_data={
    'username':'test_k',
    'password':'123456',
    'csrf_token':token_id,
    'csrf_token':token_id
}
headers_info={
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With':'XMLHttpRequest',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.9'
}

res02=session.post(url=hosts+'/phpwind/index.php',
                    params=get_params,
                    data=form_data,
                    headers=headers_info
                    )
body02=res02.content.decode('utf-8')
login_id=re.findall('_statu=(.+?)"',body02)[0];
# print(login_id)

#3.登陆之后的授权
get_params={
    'm': 'u',
    'c': 'login',
    'a': 'welcome',
    '_statu':login_id
}

res03=session.get(url=hosts+'/phpwind/index.php',
                  params=get_params
                  )
# print(res03.content.decode('utf-8'))

#4.发帖
get_params={
    'c':'post',
    'a':'doadd',
    '_json':1,
    'fid':80
}
headers_info={
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With':'XMLHttpRequest',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    # 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.9'
}
mul_form_data = OrderedDict(
    [
        ("atc_title", (None, 'P1P699911')),
        ("atc_content", (None, 'hello,P1P601')),
        ('pid', (None, '')),
        ('tid', (None, '')),
        ('special', (None, 'default')),
        ('reply_notice', (None, '1')),
        ('csrf_token', (None, token_id))
     ]
)

rese04=session.post(url=hosts+'/phpwind/index.php',
                    headers=headers_info,
                    params=get_params,
                    files=mul_form_data
                    )
print(rese04.content.decode('utf-8'))