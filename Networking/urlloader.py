# Use urllib directly to get
import sys
import urllib

content = urllib.urlopen(sys.argv[1])

while 1:
    buf = content.read(2048)
    if not len(buf):
        break
    sys.stdout.write(buf)


