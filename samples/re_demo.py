
import re


#newdream

# str1="come on! newdream"
# str2="china1usa2german3english"

pattern0=re.compile(r"(\w+),(\w+) (\w+)(?P<sign>.*)") #加了原生字符串
pattern1=re.compile(r"come (\w+)!")
pattern2=re.compile(r"\d")

# result0=re.match(pattern1,str1)   #匹配以什么开头
# result1=re.search(pattern1,str1)#   扫描整个string查找匹配
# result2=re.split(pattern2,str2) #以数字切割
# result2=re.findall(pattern2,str2)   #搜索string，以列表的形式返回全部能匹配的子串
# result2=re.finditer(pattern2,str2)  #返回的式迭代器
# for r in result2:
    # print(r.group())
# print(result2)


# print(result1.string)
# print(result1.re)
# print(result1.pos)
# print(result1.endpos)
# print(result1.lastindex)
# print('~~~~~~~~~~~~~~~~~')
# print(result1.group())
# print(result1.groups())
# print(result1.groupdict())
# print(result1.start())
# print(result1.end())
# print(result1.span())
# print(result1.expand(r"\1"))

str3='summer hot ~~'
pattern3=re.compile(r"(\w+) (\w+)")
# str3=re.sub(pattern3,r"\2 \1",str3)
# str3=re.sub(pattern3,r"hello",str3)
# print(str3)

# result=re.match(pattern3,str3)
# print(result.group(1).title())

def fun(m):
    return m.group(1).title() + ' ' + m.group(2).title()

str3=re.sub(pattern3,fun,str3)
print(str3[-4])

str5=re.subn(pattern3,r"\2 \1",str3)
print(str5)

#写法二
str2="china1usa2german3english"
v_list=re.split(r"\d",str2)
print(v_list)
