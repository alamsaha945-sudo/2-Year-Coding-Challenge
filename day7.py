# multi customer orders tracker
def final_bill(a,b):
   motbill=a+b
   return motbill
user=input("apni ki nuton costumer oder chan(ha/na):")
while user=="ha":
   costumer_name=input("apnar nam ki")
   total_posak=int(input("khota jama banaben"))
   bill=0
   for i in range(total_posak):
    posak_name=input("posak er name ki")
    rate=int(input("ater dam khoto"))
    bill=final_bill(rate,bill)
   if bill>5000:
    mot=bill*0.95
    print("apanar char diye mot bill",mot)
   else:
    print("apni kono char paben na")
   user=input("aro oders ache?ha/na:")   


