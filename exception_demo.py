

import requests
from requests.exceptions import RequestException


# res=requests.get(url='http://googele.com.hk/')
# print(res.status_code)

try:
    num_list=[1,2,3,4,5]
    print(num_list[6])
except IndexError as e:

    print('索引错误')
except Exception as e:
    print('系统错误')   #已知的可能会发生的异常写前面，不能确认的原因异常写在最后

print('hello')