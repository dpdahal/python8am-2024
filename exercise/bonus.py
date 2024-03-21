print("===========Nepal Telecom================")
print("1. NTC to NTC (Rs:2.5)")
print("2. NTC to Ncell (Rs:3.5)")
print("3. Ncell to NTC (Rs:4.5)")
print("4. Ncell to Ncell (Rs:5.5)")

option = int(input("Enter your choice:"))

if option==1:
    call_duration = int(input("Enter the call duration:"))
    if call_duration>1 and call_duration<10:
        print(f"Your bonus ",2.5)
    elif call_duration>10 and call_duration<20:
        print(f"Your bonus ",5)
    elif call_duration>20 and call_duration<30:
        print(f"Your bonus ",7.5)

elif option==2:
    pass

elif option==3:
    pass

elif option==4:
    pass

else:
    print("Invalid choice")
    exit()