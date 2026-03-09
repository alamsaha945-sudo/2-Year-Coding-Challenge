# Python Enumerate Logic
mark=[29,49,56,34,69,76]
index=0
for marks in mark:
    print(marks)
    if index==3:
        print("saha")
    index+=1   
for co,marks in enumerate(mark):
    print(marks)
    if co==3:
        print("saha")