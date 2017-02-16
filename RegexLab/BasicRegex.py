import re

def test_match_search(rexmatchobj, matchmethod='match'):
    if rexmatchobj is not None:
        print(rexmatchobj.group())
    else:
        print('Failed to ' + matchmethod + ' .')


def test_findall(result):
    if len(result) == 0:
        print('Failed to find')
    else:
        for item in result:  # result is list as always
            print(item)


# Complete Match
m = re.match(r'foo', 'food on the table')
test_match_search(m)

# match VS search
# match: to match a string against the pattern from the beginning
# search: to match a string against the pattern from anywhere of the string
m = re.match(r'foo', 'I like seafood.')
test_match_search(m)

m = re.search(r'foo', 'I like seafood')
test_match_search(m, 'search')

# match multiple strings
m = re.match(r'bat|bet|bit', 'bat')
test_match_search(m)
m = re.match(r'bat|bet|bit', 'bet')
test_match_search(m)
m = re.match(r'bat|bet|bit', 'bit')
test_match_search(m)

# match any one single character except '\n'
m = re.match(r'.end', 'bend')
test_match_search(m)
m = re.match(r'.end', '\nend')
test_match_search(m)

# match character set
m = re.match(r'[hw][eo][lr][l][od]', 'hello')
test_match_search(m)
m = re.match(r'[hw][eo][lr][l][od]', 'world')
test_match_search(m)

# match a sub group
m = re.match(r'\w+@\w+\.com', 'hello@abc.com')
test_match_search(m)
m = re.match(r'\w+@\w+\.com', 'hello@abc.efg.com')
test_match_search(m)
m = re.match(r'\w+@(\w+\.)?\w+\.com', 'hello@abc.efg.com')
test_match_search(m)

# group and groups
# group: return the whole match which group(n) returns the N sub group when there it is
# groups: return None if there is NO sub groups, otherwise return the tuple of sub groups
m = re.match(r'(\d\d\d)-(\w\d\w)', '123-o5g')
print(m.group())
print(m.group(1))
print(m.group(2))
print(m.groups())

# search the boundary. This is usually use in search, cuz match always starts to match from the beginning.
m = re.search(r'^The', 'The end.')
test_match_search(m, 'search')
m = re.search(r'^The', 'end. The')
test_match_search(m, 'search')
m = re.search(r'\bThe', 'bit The dog')
test_match_search(m)
m = re.search(r'\BThe', 'bitThe dog')
test_match_search(m)

# findall - always returns a list.
# 1. If the pattern is a normal one or a single sub group, then return a list of matched strings
# 2. If the pattern contains several sub groups, then return a list of tuples of matched sub groups
s = 'This and that and This'

result = re.findall(r'(Th\w+) and (Th\w+).+', s, re.I)
test_findall(result)
result = re.findall(r'(Th\w+)', s, re.I)
test_findall(result)
result = re.findall(r'(\d\d\d)-(\w\w\w)', '123-dfr-456-ert')
test_findall(result)