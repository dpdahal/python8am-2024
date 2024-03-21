nep =int(input("Enter nepali marks: "))
eng =int(input("Enter english marks: "))
math =int(input("Enter math marks: "))
sci =int(input("Enter science marks: "))
soc =int(input("Enter social marks: "))
total = nep+eng+math+sci+soc
per = total/5
print("Total marks: ",total)
print("Percentage: ",per)
if per>35 and per<45:
    print("C grade")
elif per>45 and per<60:
    print("B grade")
elif per>60 and per<75:
    print("A grade")
elif per>75 and per<100:
    print("A+ grade")
else:
    print("Fail")