# Student Result Management System(adcanced versoin)

def bouns(a):
    if a>90:
        result="A"
    elif 75<=a <=89:
        result="B"
    elif 50<=a <=74:
        result="C"
    else:
        result="F"
    return result
student={}
while True:
    print("1.Add stdent\n2.Avverge\n3.Show all student\n4.Show topper\n5.Search student\n6.Exit")
    user=int(input("please select menu optaion: "))
    if user==1:
        name=input("enter student name: ")
        mark=int(input("enter the number: "))
        if name in student:
            print("name is exting")
        else:
            nam=student[name]=mark
            print("susses",name,nam)   
    elif user==2:
        for s in student.keys():
            v=int(student[s]) 
            v2=bouns(v)
            print(v2)    
    elif user==3:
        for chake in student.keys():
            print(chake ,student[chake])
    elif user==4:
        top_mark=max(student.values())
        for name in student:
            if student[name]==top_mark:
                print(name,top_mark)
    elif user==5:
        user2=input("please enter the name:  ")
        if user2 in student:
            print(student[user2])
        else:
            print("no data")
    else:
        print("exit")
        break




        

        





                