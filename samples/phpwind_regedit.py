
import requests
import re

#1,进入注册页面

hosts='http://47.107.178.45'
session=requests.session()

params_info={
    'm':'u',
    'c':'register'
}

res01=session.get(url=hosts+'/phpwind/index.php',
                  params=params_info
                    )

body=res01.content.decode('utf-8')
tokenid=re.findall('name="csrf_token" value="(.+?)"',body)[0]
# print(tokenid)

#注册用户密码
params_info={
    'm':'u',
    'c':'register',
    'a':'dorun'
}

url_encode_data={
    'username':'test6669',
    'password':'123456',
    'repassword':'123456',
    'email':'test6669@qq.com',
    'csrf_token':tokenid
}

res02=session.post(url=hosts+'/phpwind/index.php',
                   params=params_info,
                   data=url_encode_data
                    )

print(res02.content.decode('utf-8'))


