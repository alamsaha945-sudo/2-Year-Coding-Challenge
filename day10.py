# smart advance management system
def cal (a,b):
    return a-b
user=input("apni ki costumer er taka joma korte chan(ha/na): ")
while user=="ha":
    costumer=input("apnar name ki? ")
    total=float(input("total wage? "))
    advanee=float(input("advance payment? "))
    payment=cal(total,advanee)
    if payment==0:
        print(f"{total}-{advanee}={payment}")
        print("sob taka porisod kora hoye geche")
    elif payment>=1:
        print("baki takar poriman",payment,"taka poya jabe")
    user=input("porer costumer er kaj korbo kina ha/na? ")        

