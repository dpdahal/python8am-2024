x=8
y=60
z=100

if x>y:
    if x>z:
        if y>z:
            print(x,y,z)
        else:
            print(x,z,y)
    else:
        print(z,x,y)
else:
    if y>z:
        if x>z:
            print(y,x,z)
        else:
            print(y,z,x)
    else:
        print(z,y,x)


# if x>y:
#     if x>z:
#         print("x is greater")
#     else:
#         print("z is greater")

# else:
#     if y>z:
#         print("y is greater")
#     else:
#         print("z is greater")