# mini grocery store:
def cal(a,b):
  return a*b
dokan_dar=input("apni ki system k on korrar jonno redy(ha/na)?: ")
while dokan_dar=="ha":
    chal=50
    dal=30
    alu=30
    user_1=input("apnar name ki?: ")
    product=input("apni ki neben(chal/ dal / alu)?: ")
    wieght=int(input("koto kg jinis naben?: "))
    total_bill=(0) 
    if product=="chal":
        total_bill=cal(chal,wieght)
        print(total_bill)
    elif product=="dal":
        total_bill=cal(dal,wieght) 
    elif product=="alu":
        total_bill=cal(alu,wieght)
        print(f"thankyou {user_1} apnar mot bill {total_bill} taka")
    if total_bill>=100:
       new_bill=total_bill-10
       print(f"{user_1} tomar {new_bill} taka hoyeche")
    elif total_bill<100:
        print(f"{user_1} apni kono discount paben na")
    else:
       print("no data")
    dokan_dar=input("\napni ki r kaj korben ha/na?: ")
    print("system off")
        