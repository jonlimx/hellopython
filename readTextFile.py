__author__ = 'jonathanlim'

"""Read the text in file with a given name"""

fname = raw_input('File name > ')

try:
    fileobj = open(fname, 'r')

    for line in fileobj:
        print line.strip()

except IOError, e:
    print 'Failed to open file: %s' % e
