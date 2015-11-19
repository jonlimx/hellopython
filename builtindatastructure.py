# list - a list is like a array. we can put a list of data in it. And we use index to get an item.
aList = ['hello', 'my', 'name', 'is', 'Jonathan', 'Lim']
# for i in range(0, len(aList)):
#     print(aList[i])
print(aList[4])
# we can modify the item in a list.
aList[4] = 'Johnson'
print(aList[4])
print(aList)

# tuple - a tuple is a read-only list.
aTuple = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
print(aTuple[4])
# we can NOT modify the item in a tuple.
# aTuple[4] = 'Fri'
print(aTuple)

# set - unordered collections of unique elements
setA = set('hellooooo, this is michael')
setB = set('nice, i am lisa')
# get rid of duplicate items
print(setA)
# print the items both in set A and set B
print(setA & setB)
# print the items only in set A, but not in set B
print(setA - setB)
# print the items in set A and set B
print(setA | setB)

# dictionary - key value pair
aDic = {'name': 'Jonathan Lim', 'code': 'jonlimx'}
print(aDic)
print('name: {0}'.format(aDic['name']))
aDic['age'] = 27
print('age: %i' % aDic['age'])

