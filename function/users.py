# users=[
#     {'username':"admin","password":"admin002"},
#     {'username':"ram","password":"ram002"},
#     {'username':"shyam","password":"shyam002"}
# ]

# def login(username,password):
#     for user in users:
#         if user['username'] == username and user['password'] == password:
#             print("Login successful")
#             return
#     print("Login failed")

# uname = input("Enter username: ")
# pwd = input("Enter password: ")
# login(uname,pwd)

numbers=[
    [34,56,78,90,78],
    [45,67,89,23,45],
    [23,45,67,89,90]
]

def even_number():
    for number in numbers:
        for num in number:
            if num%2==0:
                print(num)

even_number()

def result(name,eng,mat,nep,sic,cp):
    pass



# users=[
#     {'name':"ram",'gender':'male','status':True},
#     {'name':'sita','gender':'female','status':False},
#     {'name':'laxmi','gender':'female','status':True},
#      {'name':'hari','gender':'male','status':True},
#       {'name':'rama','gender':'female','status':True},

# ]


# total_user=0
# total_male_user=0
# total_female_user=0
# total_active_user=0
# total_inactive_user=0
# total_active_male=0
# total_inactive_male=0
# total_active_female=0
# total_inactive_female=0