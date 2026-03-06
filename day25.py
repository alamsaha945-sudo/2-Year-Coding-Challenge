# Custom Error Raising 
user=int(input("enter number 5 to 9: ")) 
if user<5 or user>9:
    raise ValueError("rong input")
print("thank you")