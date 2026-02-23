# smart atm system
def cheke(a,b):
    if 5000<=a<=5001 and b=="yes":
       result=f"{a}+{200}=",a+200
    elif 5000<=a<=5001 and b=="no":
        result=f"{a}+{100}=",a+100
    elif 0<=a<=5000:
        result=a
    else:
        result=("low balance")
    return result       
user=int(input("please type your pin number?:",))
while user==743293:
    u0=input("apnar name ki?:   ")
    u1=int(input("khoto taka tulte chan?:  "))
    u2=input("apni ki preminun custermer?:  ")
    recive=cheke(u1,u2)
    if recive!="low balance":
        for i in range(3):
            print("taka ghona hoche:")
    print(f"{u0}  apnar {recive}")
    user=int(input("abber taka tulte chaile pin din:  "))


