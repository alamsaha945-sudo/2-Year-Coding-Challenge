# Kg and Pound Calaultar
while True:
    user=int(input("1.Chake (kg and Lbs)\n2.Exit\nSelect the option:>>>>> "))
    try:
        weight=int(input("Weight:>>>> "))
        unit= input("(L)bs or (K)g: Please enter the option:>>>> ")
        if unit.upper()=="K":
            convart=weight*0.45
            print(f"You are {convart} Kg")
        elif unit.upper()=="L":
            convart=weight//0.45
            print(f"You are {convart} Lbs")
        else:
            print("Exit")
            break    
    except Exception as a:
        print(a)
        print("___Right input____")
           
