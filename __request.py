import requests
import json


result  =  requests.get("https://jsonplaceholder.typicode.com/")
result = json.loads(result.text)
for i in result():
    print(i["title"])

