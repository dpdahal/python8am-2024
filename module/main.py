# what is module?
# module is a file containing python definitions and statements. The file name is the module name with the suffix .py appended.

# type of module
# 1. Built-in module
# 2. User-defined module

# import calculator

# print(dir(calculator))
# print(calculator.name)
# print(calculator.brand)
# print(calculator.add(3,4))
# print(calculator.info())

# from calculator import add
# from calculator import *
# from product import *
# from calculator import add
# from product import add as total
# print(add(3,4))
# print(total())

# import result.students as s

# from result import students

# from result import *

# print(students.mark())
# print(users.get())

# import datetime

# print(dir(datetime))

# print(datetime.datetime.now())

# time delta
# today = datetime.datetime.now()
# jan 1971 = datetime.datetime(1971,1,1)

# jobs=[
#     {'title':"python developer","exp_date":"2020-01-01"},
#     {'title':"java developer","exp_date":"2025-01-01"},
#     {'title':"Php developer","exp_date":"2023-05-01"},
# ]

# for job in jobs:
#     exp_date = job['exp_date']
#     exp_date = datetime.datetime.strptime(exp_date,"%Y-%m-%d")
#     today = datetime.datetime.now()
#     if exp_date < today:
#         print(f"{job['title']} is expired",today-exp_date)
#     else:
#         print(f"{job['title']} is not expired",exp_date-today)


# join_date ="2020-01-01"
# join_date=datetime.datetime.strptime(join_date,"%Y-%m-%d")
# old_year=datetime.datetime(2020,1,1)
# new_year=datetime.datetime.now()
# print(new_year-old_year)
# print(datetime.datetime.now())
# print(dir(datetime.datetime))
# print(datetime.MAXYEAR)
# print(datetime.MINYEAR)

import os
import sys
# print(sys.version_info)
# print(sys.argv)
# print(dir(os))
# print(dir(sys))
# print(os.getcwd())

# os.makedirs("module/example")
# os.rmdir("module/example")

# if os.path.exists("result"):
#     print("Folder is already exists")
# else:
#     os.makedirs("result")