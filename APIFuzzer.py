import requests
import sys

def fuzzer():

    for word in sys.stdin:
        res = requests.get(url=f"http://10.10.11.161/{word}")
        if res.status_code == 404:
            fuzzer()
        else: 
            data = res.json()
            print(data)
            print(res.status_code)
            print(word)

fuzzer()
