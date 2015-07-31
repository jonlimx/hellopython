__author__ = 'lin.zhongsheng'

CODEC = 'utf-16'
FILE = 'unicode_string.tmp'

hello_out = u'''Hello World. This string is encoded as UTF-16 and and saved in a local file named unicode_string.txt.
                Since it's encoded as UTF-16, we have to decoded it as UTF-16 to get the information.'''
bytes_out = hello_out.encode(CODEC)

f = open(FILE, "w")
f.write(bytes_out)
f.close()

f = open(FILE, 'r')
bytes_in = f.read()
f.close()

hello_in = bytes_in.decode(CODEC)
print hello_in
