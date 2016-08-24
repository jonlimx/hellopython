from urllib import request


def download_site(url):
    headers = {'User-agent': 'none/ofyourbusiness', 'Spam': 'Eggs'}
    req = request.Request(url, headers=headers)
    try:
        resp = request.urlopen(req)
        html = resp.read()
        print("==========Content==========")
        print(html)
        print("==========URL==========")
        print(resp.geturl())
        print("==========Response Info==========")
        print(resp.info())
    except request.URLError as ex:
        if hasattr(ex, 'code'):
            print(ex.code)
        elif hasattr(ex, 'reason'):
            print(ex.reason)

if __name__ == '__main__':
    none_exist = 'http://www.notfoundsite.com'
    not_found = 'https://jonlimx.github.io/notfound'
    my_site = 'https://jonlimx.github.io'
    download_site(none_exist)
    download_site(not_found)
    download_site(my_site)
