import requests
import json
response = requests.get("https://gateway.stockx.com/public/v1/browse?limit=50",headers={'x-api-key':'B1sR9t386d6UVO6aI7KRf91gLaUywqEK1TLBGsXv'})
print(response)
a = response.json()

dic = {}
dic["Records"] = []
for i in a['Products']:
    name = (i['shortDescription'])

    dic["Records"].append({
            "keywords": name,
            "limit": 100,
            "print_urls": "true"
        })
z =json.dumps(dic)
file = open("config.json","w")
file.write(z)