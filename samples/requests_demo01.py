
import requests

response=requests.get('http://www.hnxmxit.com/')
# print(response.json())
# print(response.apparent_encoding)
response.encoding=response.apparent_encoding
# response.encoding='utf-8'
print(response.text)
# print(response.headers)

# print(response.content.decode('utf-8'))