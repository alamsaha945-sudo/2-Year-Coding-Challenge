# Inventory And Billing system 
def dis (a):
    if a>=500:
        b=(a*15/100)
        return b
    else :
        return 0
def gst(b):
    c=(b*18/100)
    return c
money=0
product={"maggi":20,"egg":8,"bread":40,"chu":30,"sweet":300}
while True:
    try:
        customer=int(input("1.buy\n2.exit\n>>>>>"))
        if customer==1:
            for pro in product.keys():
                print(f"product {pro} rupes {product[pro]}")
            user=input("what can you buy ")
            if user in product:
                money+=product[user]
                gt= gst(money)
                money+=gt
                chake=dis(money)
                money-=chake
                print(f"apnar mot bill will gst and dicount {money}")
            else:
                print("no data")
        else:
            print("exit")
            break        
    except:
        print("worng input")            