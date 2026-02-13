# advanced discount system whith membership logic and opretar
costumer=int(input("apni khoto takar jinis kinehe?: "))
member=input("apni ki ei dokan er member?: ")
if costumer>=1000 and member=='yes':
    char=200
    print("apni",char,"taka char paben")
elif costumer>=1000 and member=='no':
   char=100
   print("apni",char,"char paben")
motbill=costumer-char    
print("char diye apnar mot bill",motbill,"taka")
for motbill in range(5):
       print("congratulations khub kom holo")
else:
    print("apni kono char paben na ")            
    