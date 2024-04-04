# what is loop?
# loop is a sequence of instruction that is continually repeated until a
# certain condition is reached.

# types of loop
# 1. for loop: it is used to iterate over a sequence of items.
# 2. while loop: it is used to iterate over a block of code as long as the
# 3. Nested loop: loop 

# for loop
# data=['apple','banana','cherry']

# for name in data:
#     print(name)

# range()


# for i in range(1,10,2):
#     print(i)

# users=[]
# num = int(input('Enter the number of users: '))

# for i in range(num):
#     name = input('Enter your name: ')
#     users.append(name)


# print("===========user list=========")
# for user in users:
#     print(user)


for x in range(1,4):
    print(f"================row: {x}==================")
    for a in range(1,11):
        print(a,end=" ")
    print()