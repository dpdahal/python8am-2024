# file types : txt, binary
# modes : read, write, append, readwrite
# read : r, rb
# write : w, wb
# append : a, ab
# readwrite : r+, rb+
# readwrite : w+, wb+

# handle =open('filehandling/sample.txt', 'w')
# handle.write('Hello ')
# handle =open('filehandling/sample.txt', 'a')
# handle.write('Hello \n')
# handle.write('World \n')
# handle.write(str(5678))
# handle.close()


# handle =open('filehandling/sample.txt', 'a')
# name = input("Enter your name:")
# handle.write(f'Hello {name}')
# handle.write("\n")
# handle.close()

# name,email,address,phone

handle =open('filehandling/sample.txt', 'r')
print(handle.read())
print(handle.readline())
print(handle.readlines())

# for name in handle.readlines():
#     print(name)

# try:
#     with open("filehandling/sample.txt", "r") as file:
#         print(file.read())
# except Exception as e:
#     print(e)

# import os 

# if not os.path.exists("filehandling/students.txt"):
#     open("filehandling/students.txt","w")
#     print("File Created")

# title,author,price,pages,posted_by
# python,ram,500,100,ram