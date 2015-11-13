__author__ = 'jonathanlim'

"""Read the text in file with a given name"""

fname = input('File name > ')

try:
    fileobj = open(fname, 'r')

    for line in fileobj:
        print(line.strip())

except IOError as e:
    print('Failed to open file: {0}'.format(e))


for index in range(1, 10):
    print('Index: {0}, I\'d love it!'.format(index))

