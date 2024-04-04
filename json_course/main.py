# import json

# data={
#     'name':'ram',
#     'address':"kathmandu",
# }
# # dic convert into json
# new_data = json.dumps(data)
# print(new_data)
# # json convert into dic
# d_data =json.loads(new_data)
# print(d_data)


# import requests

# # url ="https://jsonplaceholder.typicode.com/users"
# url="https://jsonplaceholder.typicode.com/posts"

# response = requests.get(url)
# data = response.json()
# for x in data:
#     print(x['title'])
# # print(data)

# print(response)
# print(dir(response))