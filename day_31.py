# Sceret Massage Encoder And Decoder 

# Encode 
def encode(msg):
    result=""
    for letter in msg:
        if letter==" ":
            result+="$"
        else:
            number=ord(letter)
            number=number+5
            result+=chr(number)
    return result
# Decode 
def decode(msg):
    result=""
    for letter in msg:
        if letter=="$":
            result+=" "
        else:
            number=ord(letter)
            number=number-5
            result+=chr(number)
    return result
while True:
    try:
        user=int(input("1.Encode\n2.Decode\n3.Exit\nOption>>>>"))
        if user==1:
            us1=input("Enter encode message:>>>> ")
            en_cd=encode(us1)
            print(f"your encode message>>>> {en_cd}")
        elif user==2:
            us2=input("enter decode message:>>>> ")
            de_cd=decode(us2)
            print(f"your decode message>>>> {de_cd}")
        else:
            print("Exit")
            break
    except:
        print("____worng input____")        