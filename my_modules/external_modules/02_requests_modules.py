import requests
import json


r = requests.get('https://api.github.com/users/asimkhan17790')

print(r.status_code)

# print(r.json())

res_json = r.json()

# print(res_json[0]['id'])
# print(res_json[0]['actor']['login'])

if (r.status_code == 200):
    print("Username details found:", res_json['login'])
else:
    print("User not found...")

# Writing response to a file
with open("response.txt", "w") as f:
    f.write(r.text)

# response_post = requests.post('https://httpbin.org/post', data={'key': 'value'})
