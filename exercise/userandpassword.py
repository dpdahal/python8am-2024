users=[
    ['admin','admin002'],
    ['ram','ram123'],
]

username = input("Enter username: ")
password = input("Enter password: ")

if users[0][0]==username and users[0][1]==password:
    print("Welcome",username)
elif users[1][0]==username and users[1][1]==password:
    print("Welcome ",username)
else:
    print("Invalid username or password")