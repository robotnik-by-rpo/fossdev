import requests
import sys

def http_conn(url,flag=None):
    res = requests.get(url)
    print(res.status_code)
    if flag is not None:
        if flag == "-j":
            print(res.json())
        elif flag == "-t":
            print(res.text)
        else:
            print("Wrong flag")
