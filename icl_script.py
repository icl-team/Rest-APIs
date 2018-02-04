#importing req
import requests

#Link in (backend assignment link)
icltest_link = "https://jsonplaceholder.typicode.com/users"

#Get Request
resp = requests.get(icltest_link)

post_list = resp.json()

few_post = post_list[0:-1]
print("ICL Project Test : ")
for post in few_post:

    print("ID: ", post['id'])

    print("NAME: ", post['name'])

    print("UserName: ", post['username'])

    print("Address: ", post['address'])

    print("Email: ", post['email'])

    print()