print("=======Student Result=============")
num = int(input("Enter the number of students: "))
students_marks = []
for x in range(1, num+1):
    print(f"=========Student: {x}=============")
    for mark in range(1):
        nep =int(input("Enter nep mark: "))
        eng =int(input("Enter eng mark: "))
        math =int(input("Enter math mark: "))
        sci =int(input("Enter sci mark: "))
        com =int(input("Enter com mark: "))
        total = nep + eng + math + sci + com
        students_marks.append(total)

print("=======Result=============")
student_num=1
print("S.n\t Total\t Percentage\t Grade")
for total in students_marks:
    per = total/5
    grade = ""
    if per>35 and per<45:
        grade = "C grade"
    elif per>45 and per<60:
        grade = "B grade"
    elif per>60 and per<75:
        grade = "A grade"
    elif per>75 and per<100:
        grade= "A+ grade"
    else:
        grade = "Fail"
    
    print(f"{student_num}\t {total}\t {per}\t {grade}")
    student_num+=1