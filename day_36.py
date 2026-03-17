# Number Gussing Game.
import random
gauss=[1,2,3,4,5,6,7,8,9]
guss=random.choice(gauss)
procec=0
while procec<3:
    user=int(input("Guss the number:>>>> "))
    procec+=1
    if user==guss:
        print("You are win!")
        break
else:
    print("You failed")


