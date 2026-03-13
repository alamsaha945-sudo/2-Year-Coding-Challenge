# Smart Student Grader
def calculate_grade(marks):
    if marks>=90:
        result="A"
    elif 70<=marks <=89:
        result="B"
    elif 50<=marks<=69:
        result="C"
    elif 35<=marks<=49:
        result="D"
    else:
        result="F"
    return result
saved_student={}
pass_student=[]
fail_student=[]
while True:
    try:
        user=int(input("1.Add student\n2.All student grade\n3.Pass student and Fail student\n4.Highest mark\n5.Search student\n6.Exit\nSelect optaion menu:>>>> "))
        if user==1:
            user=int(input("How much student add enter number:>>>>"))
            for i in range(user):
                name=input("Student name:>>>> ")
                if name in saved_student:
                    print("All redy exite!")
                else:
                    num=int(input("Enter the mark:>>> "))
                    student=saved_student[name]=num
                    print(f"Add successful:>>>{name}:{student}")
        elif user==2:
            for chake in saved_student.keys():
                num=int(saved_student[chake])
                mark=calculate_grade(num)
                print(f"{chake}:{saved_student[chake]}:{mark}")
        elif user==3:
            for name in saved_student:
                mark=saved_student[name]
                if mark>=35:
                    pass_student.append(name)
                else:
                    fail_student.append(name)
            print(f"Pass student:{pass_student}")
            print(f"Fail student:{fail_student}")
        elif user==4:
            top=(saved_student.values())
            for name in saved_student:
                if saved_student[name]==top:
                    print(f"{name}:{top}")
        elif user==5:
            user=input("What is student name:>>> ")
            if user==saved_student:
                print(f"{user}:{saved_student[user]}")
            else:
                print("No data")    
        else:
            print("Exit")
    except Exception as e:
        print(e)                                            




                
            