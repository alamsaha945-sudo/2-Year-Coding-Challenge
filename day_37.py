# Student Grading & Performance Analyzer
student={}
top_pe=[]
need_im=[]
while True:
    try:
        user=int(input("1.Add students\n2.Top performers & Nedd imporvem\n3.All students\n4.Exit\n>>>>>"))
        if user==1:
            total_sudent=int(input("Add number student number:>>>>> "))
            for i in range(total_sudent):
                name=input(f"{i+1}. num student name:>>>> ")
                if name in student:
                    print("Allredy exite")
                    continue
                else:
                    sub_1=int(input("Bengali number:>>>> "))
                    sub_2=int(input("English number:>>>> "))
                    sub_3=int(input("Math number:>>>> "))
                    student[name]=[sub_1,sub_2,sub_3]
                    print("\n>>>>>Add complete<<<<<")
        if user==2:
            for name,mark in student.items():
                average=sum(mark)/len(mark)
                if average>80:
                    top_pe=(name)
                elif average<40:
                    need_im=(name)
            print(f"Top performers:\"{top_pe}")
            print(f"Need improvement:\"{top_pe}")
        if user==3:
            for name,mark in student.items():
                print(name)
                print(mark)
        else:
            print("Exit the softower!")
            break
    except Exception as a:
        print(f"{a}:,, Worng input")   

                
                

            
            

                  
                          

                    