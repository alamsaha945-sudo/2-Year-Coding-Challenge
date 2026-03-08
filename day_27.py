# Smart Student Result System 
# Logic By Saha
def chake(a):
    if a>=90:
        result=("A+")
    elif 80<=a <=89:
        result=("A")
    elif 70<=a <=79:
        result=("B")
    elif 60<=a <=69:
        result=("C")
    elif 50<=a <=59:
        result=("D")
    else:
        result=("F")
    return result
def chake1(b):
    fail_count=0
    for i in b.values():
        if i<35:
            fail_count+=1
    return fail_count
def chake2(c):
    if c==0:
        return "pass"
    elif c>2:
        return "year back"
    else:
        return "fail in that subject"
sub={}
while True:
    try:
        user=int(input("please enter the option\n1.add student\n2.subject wise result\n3.exit\n>>>> "))
        if user==1:
            num_sub=int(input("how many subject?>>>>> "))
            for i in range(num_sub):
                sub_name=input(f"enter the subject {i+1}.name:>>>>> ")
                mask=int(input(f"enter the {sub_name}:>>>>> "))
                sub[sub_name]=mask
            print("add successfully")
        elif user==2:
            print("\n------subject wise reslt------")
            for sub_name,mark in sub.items():
                stutas="pass" if mark>=35 else "fail"
                print(f"{sub_name}>>>{mark}\nstutas>>>>{stutas}>>>>grade>>>>{chake(mark)}")
            fail_count=chake1(sub)
            result=chake2(fail_count)
            print(f"final result>>>>>>{result}")
        else:
            user==3
            print("exit")
            break
    except Exception as a:
        print(a)
        print("worng input")

                

        