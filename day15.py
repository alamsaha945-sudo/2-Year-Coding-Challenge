# simple student result analyser
def chake(j):
    if j>=90:
        mask=("grade A")
    elif 75<=j<=89:
        mask=("grade B")
    elif 50<=j<=74:
        mask=("grade C")
    elif 35<=j<=49:
        mask=("grade D")
    else:
        mask=("fail")
    return mask
total=[]
user=input("what is your name?: ")
for i in range(5):
    user2=int(input("pls subimt your five subject number?; "))
    total.append(user2)
average=sum(total)/len(total)
grade=chake(average)
print("Name:",user)
print("Total mark:",sum(total))
print("average:",average)
print(grade)

                       