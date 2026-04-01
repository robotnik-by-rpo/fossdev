import requests
import sys

def http_conn(url,flag=None):
    res = requests.get(url)
    print(res.status_code)
    if flag is not None:
        if flag == "-j":
            try:
                print(res.json())
            except:
                print("Response doesn't have json")
        elif flag == "-t":
            print(res.text)
        else:
            print("Wrong flag")
