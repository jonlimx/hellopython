import re
from random import choice, randrange
from string import ascii_lowercase as lc
from sys import maxsize
from time import ctime

# 1. 择一匹配符的使用
pattern = r'[bh][aiu]t'
result = re.match(pattern, 'bat')
print(result.group())
result = re.match(pattern, 'hut')
print(result.group())

# 2. 匹配单个空格分隔的任意单词对
pattern = r'([A-Za-z]+) ([A-Za-z]+)'
result = re.match(pattern, 'Hello World')
print(result.groups())

# 3. 匹配单个逗号和单个空白符分隔的单词和字母
pattern = r'([A-Za-z]+), ([A-Za-z])'
result =re.match(pattern, 'Jonathan, Lim')
print(result.groups())

# 4. Python标识符
pattern = r'[_A-Za-z][_A-Za-z0-9]+'
result = re.findall(pattern, '_helo __hello _ 34 34_naming naming naming____')
print(result)

# 6 - 匹配以www.开始，以.com|.net|.edu结尾的网址
pattern = r'www\.([A-Za-z0-9]+\.)+(com|net|edu|cn)'
result = re.match(pattern, 'www.baidu.com')
print(result.group())
result = re.match(pattern, 'www.upc.edn.cn')
print(result.group())

# 13 - 根据类型字符串吗，提取类型。类型可以通过type()来获取，python2中，类型字符串的格式为<type 'xxx'>；Python3中，类型字符串的格式为<class 'xxx'>
pattern = r'''<(type|class) '(\w+)'>'''
result = re.match(pattern, str(type('')))
print(result.group(2))

# 14 - 匹配月份
pattern = r'0?[1-9]$|1[0-2]$'
result = re.match(pattern, '03')
print(result.group())
result = re.match(pattern, '12')
print(result.group())

# 15 - 处理信用卡号码。美国信用卡是由15或者16位数字组成。格式可以是：4-6-5或者是4-4-4-4
pattern = r'\d{4}-\d{6}-\d{5}|(\d{4}-){3}\d{4}'
result = re.match(pattern, '4345-456278-34234')
print(result.group())
result = re.match(pattern, '4345-6278-3423-9909')
print(result.group())

# 16 - 为gendata.py更新代码，使得结果输出到redata.txt上
tlds = ('com', 'edu', 'net', 'org', 'gov')
with open('redata.txt', 'at') as file:
    for i in range(randrange(5, 11)):
        dtint = randrange(maxsize)  # pick date (seconds from 'epoch')
        dtstr = ctime(dtint)  # date string
        llen = randrange(4, 8)  # login is shorter
        login = ''.join(choice(lc) for j in range(llen))
        dlen = randrange(llen, 13)  # domain is longer
        dom = ''.join(choice(lc) for j in range(llen))
        print('%s::%s@%s.%s::%d-%d-%d' % (dtstr, login, dom, choice(tlds), dtint, llen, dlen), file=file)
