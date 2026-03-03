# leap year checking system
def leap(year):
    leap=False
    if year%400==0:
        leap=True
    elif year%100==0:
        leap=False
    elif year%4==0:
        leap= True
    else:
        leap=False
    return leap
while True:
    user=int(input("1.chake year\n2exit\n  "))
    if user==1:
        year=int(input("type of the year:  "))
        print(leap(year))
    else:
        print("exit")
        break                   



