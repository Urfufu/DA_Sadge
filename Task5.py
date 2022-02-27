import requests

class Task5:
    web = 'http://192.168.50.58/algenius'
    req = requests.get(web)
    print("Status codee: ")
    print("\t*",  req.status_code)

    h = requests.head(web)
    print("Header: ")
    print("*************")
    for x in h.headers:
        print("\t", x,":", h.headers[x])
    print("*************")
    headers = {
        "User-Agent": "Mobile"
    }
    web2 = 'http://httpbin.org/headers'
    rh = requests.get(web2, headers=headers)
    print(rh.text)