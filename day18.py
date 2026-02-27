# mini bank syetem(logic+recuran mix)
balnce=0
def cahke(a):
    if a=="deposit":
        return balnce + user2
    elif a=="whitdraw":
        if user2<=balnce:
           return balnce-user2
        else:
           return balnce      
    elif a=="chake balance":
        return balnce
user=input("apnar ki bank e kichu dorkar(ha/na): ")
while user=="ha":     
    menu=(1,2,3)
    user=int(input("menu optaion\n1.depjit\n2.whitdraw\n3.ckake balance\n  ")) 
    if user==menu[0]:
      result="deposit"
    elif user==menu[1]:
       result="whitdraw"
    elif user== menu[2]:
       result="chake balance"
    if result=="deposit" or result=="whitdraw":
       user2=int(input(f"pls subbimet {result} money:  "))
    else:
       user2   
    balnce=cahke(result)
    print("current balance",balnce)
    user=input("aro kichu korte chan(ha/na):   ")

