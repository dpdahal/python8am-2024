# what is function?
# function is a block of code which only runs when it is called.
# types of function:
# 1. Built-in function: len, print, input, range, etc.
# 2. User-defined function: function defined by the user.

# Example of user-defined function:

# def info():
#     print("Hello, World!")

# info()
# info()

# print()
# len()

# function with parameter:

# def user(name,age):
#     print("Hello, " + name, "your age is", age)

# user('ram',20)

# def add(x,y):
#     print(x + y)

# add(10,20)

# optional parameter:

# def student(name,age=0):
#     print(name)
#     print(age)
# student('ram')


# funcction accepting any number of arguments:
# *args: it is used to pass a non-keyworded, variable-length argument list.
# **kwargs: it is used to pass a keyworded, variable-length argument list.
# def student(*name,**data):
#     print(name)
#     print(data)

# # student(["ram","sita","gita","hari"])
# student("ram","sita","gita","hari",name='hari',age=20,address='katm')


#  function return value

# def add(x,y):
#     a = x+y
#     return a


# print(add(10,20))


# def add_sub(x,y):
#     sm = x+y
#     sb = x-y
#     return [sm,sb]

# print(add_sub(10,20))


# function scope
# local scope
# global scope

# x=10

# def test():
#     a =20
#     print(x)

# test()


# a=5

# def test():
#     # c = a+610
#     # a=500
#     global a
#     a=a+650
#     print(a)

# test()
# print(a)


# a = lambda x,y: x+y
# print(a(100,20))

# def a(x,y):
#     return x+y


# def add(x,y):
#     return x+y

# a = add
# print(a(5,7))



# def fac(n):
#     if n==1:
#         return 1
#     else:
#         return n*fac(n-1)
    
# print(fac(5))
# 5-1 = 4 = 20
# 4-1 = 3 = 60
# 3-1 = 2 = 120
# 2-1 = 1 = 120

# def insert():
#     """
#     insert function used to insert data
#     """
#     # code to insert data
#     return "inserted"

# print(insert.__doc__)

# nested function
# function decorator


# def add(x,y):
#     # print(x+y)
#     return x+y


# def my_rep(data,time):
#     print(data*time)


# my_rep('hello',5)
# my_rep('5',5)


# def add(x,y):
#     return x+y
#     a = x+y


# def total():
#     print(add(10,20))

# total()

# module