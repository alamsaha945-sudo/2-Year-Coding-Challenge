# clothing store inventory logic: 
oders=["shirt","pant","panjabi","frock","koti"]
mot_kaj=5
for i in range(1,mot_kaj+1):
    type=oders[i-1]
    print(f"{i}:{type}")
    if type=="panjabi"or type =="koti":
        print("dam porbe 500 taka")
    else:
        print("dam porbe 200 taka")
    if i==3:
       print("lunch er time hoye geche")

print("aj ke mot kajer sonka:",len(oders))
print("ami softwere engere hobo")       
