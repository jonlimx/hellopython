from urllib import request, parse

# Base URL being accessed
url = 'http://172.31.100.91/Survey'

# Dictionary of query parameters (if any)
parms = {'magicOn': 'true', 'team': 'WATS'}

# Encode the query string
querystring = parse.urlencode(parms)

# Extra headers
headers = {'User-agent': 'none/ofyourbusiness', 'Spam': 'Eggs'}

# Make http call - Option #1
# Make a GET request and read the response
u = request.urlopen(url + '?' + querystring)
resp = u.read()

# Make http call - Option #2
req = request.Request(url, querystring.encode('ascii'), headers=headers)
u = request.urlopen(req)
resp1 = u.read()

if __name__ == '__main__':
    print(resp)
    print('=================')
    print(resp1)
