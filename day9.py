#calculeter
def cal(a,b,c):
   if b =="+":
      result= a+c
   elif b =="-":
      result= a-c
   elif b =="*":
      result= a*c
   elif b =="/":
      result= a/c
   else:
      print("no data!")
   return f"{a}{b}{c}={result}"
user= input("apni ki calculet korte chan(ha/na):")
while user=="ha": 
   x=int(input("your first number: "))
   y=input("tumi ki korte chu?: ")      
   z=int(input("your second number: "))
   output=cal(x,y,z) 
   print("your answer is",output)
   user= input("apni ki aro calculet korte chan?ha/na:")  