# password strenth checker
def cahke(a,has_digit,has_lower,has_upper):
  if a=="":
    result=("pls chake")
  elif len(a)<8:
    result=("weak")
  elif has_digit and has_lower and has_upper:
    result=("strong")
  else:
    result=("invalid")
  return result           
user=input("pls chake your password:   ")
has_lower=False
has_digit=False
has_space=False
has_upper=False
for i in user:
    if i.isdigit():
        has_digit=True
    if i.isupper():
        has_upper=True
    if i=="":
        has_digit=True  
    if i.islower():
        has_lower=True
    pas=cahke(user,has_digit,has_lower,has_upper) 
print(pas) 

