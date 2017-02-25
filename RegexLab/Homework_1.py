import re

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