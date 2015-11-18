# string to remain as is. String escape is ignored.
string11 = r'Hello, \nWorld!!!'

# string escape still works in this case.
string12 = '''Hello, \nWorld!!!'''

print(string11)
print()
print(string12)

# easy way to repeat strings
print('10 times of hello\n'*10)

# sub string
# 1. string index - index is started from 0. string1[n]
# 2. string slice - slice string from index n to index m-1. string2[n:m]

parentstring = "This-is parent string, please don't slice me!"
# slice from index 2 to index 4. Result: is "
print(parentstring[2:5])
print()

# slice from index 2 to the end.
print(parentstring[2:])
print()

# slice from the beginning to index 4. Result: This-is
print(parentstring[:5])
print()

