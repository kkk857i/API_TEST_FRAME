
import re


#newdream

str1="newdream,come on!"

pattrrn=re.compile(r"(\w+),(\w+) (\w+)(?P<sign>.*)") #加了原生字符串

result1=re.match(pattrrn,str1)  #匹配以什么开头
print(result1.string)
print(result1.re)
print(result1.pos)
print(result1.endpos)
print(result1.lastindex)
print('~~~~~~~~~~~~~~~~~')
print(result1.group())
print(result1.groups())
print(result1.groupdict())
print(result1.start())
print(result1.end())
print(result1.span())
print(result1.expand(r"\2,\3,\1,\4"))