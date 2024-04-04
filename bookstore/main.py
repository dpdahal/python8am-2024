import os

if not os.path.exists('bookstore/books.txt'):
    fObj = open('bookstore/books.txt', 'w')
    fObj.close()


if not os.path.exists('bookstore/users.txt'):
    fObj = open('bookstore/users.txt', 'w')
    fObj.close()



def register():
    username = input('Enter username: ')
    username=username.strip()
    if username in open('bookstore/users.txt').read():
        print('User already exists')
        exit()
    password = input('Enter password: ')
    password=password.strip()
    with open('bookstore/users.txt', 'a') as fObj:
        fObj.write(f'username:{username}, password:{password}\n')
    print('User registered successfully')
    exit()

def login():
    username = input('Enter username: ')
    username=username.strip()
    password = input('Enter password: ')
    password=password.strip()
    with open('bookstore/users.txt') as fObj:
        users = fObj.readlines()
    for user in users:
        if f'username:{username}, password:{password}\n' == user:
            print('Login successful')
            break
    else:
        print('Login failed')
        exit()

login()