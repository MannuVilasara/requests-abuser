import requests
from config import proxies, data, headers


def inputs(url=None, count=None,method_input=None):
    if not url:
        url = input("Enter URL: ")

    try:
        if not count:
            count = int(input("Enter the Number of Requests: "))
        if not method_input:
            method_input = int(input('Method: [1.GET,2.POST,3.PATCH,4.DELETE]: '))
        if method_input < 1 or method_input > 4:
            print("Enter Valid Method")
            inputs(url=url,count=count)
        return url,count,method_input
    except:
        print("Enter Valid Number")
        inputs(url=url,count=count,method_input=method_input)

def abuser(url, count, method_input):
    if method_input == 1:
        for i in range(count):
            response = requests.get(url,headers=headers,data=data,proxies=proxies)
            print(response.status_code)
    if method_input == 2:
        for i in range(count):
            response = requests.post(url=url,headers=headers, data=data,proxies=proxies)
            print(response.status_code)
    if method_input == 3:
        for i in range(count):
            response = requests.patch(url=url,headers=headers, data=data,proxies=proxies)
            print(response.status_code)
    if method_input == 4:
        for i in range(count):
            response = requests.delete(url=url,headers=headers,proxies=proxies)
            print(response.status_code)

url, count, method_input = inputs()
abuser(url=url,count=count,method_input=method_input)