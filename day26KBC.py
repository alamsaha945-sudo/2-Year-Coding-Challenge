# KBC game project
# creadeted by saha
qu=[
    [
        "A. what is the capital of france?","1.berlin","2.madird","3.paris","4.rome",3
    ],
    [
        "B. which language is primaraily used for web development?","1.python","2.html","3.java","4.c++",2
    ],
    [
        "C. what is 5+7","1.14","2.16","3.12","4.15",3
    ],
    [ 
        "D. who developed python?","1.dennis retchie","2.elon musk","3.jemes goling","4.guido van rossom",4
    ],
    [ 
        "E. which data type is used to store multiple velu?","1.int","2.flot","3.list","4.str",3
    ],
    [ 
        "F. what dose cpu starnd for?","1.central process","2.centarl processing unit","3.central power unit ","4.centarl cull added",2
    ],
    [ 
        "G. which symbol is used for comments in python?","1.//","2.*","3.#","4++",3
    ],
    [ 
        "H. which company developed in windows?","1.apple","2.goegle","3.microsoft","4.ibm",3
    ],
    [ 
        "I. what is the squares root of 81?","1,7","2.9","3.10","4.6",2
    ],
    [ 
        "J. which keyword is used to define a fuction in python","1.def","2.func","3.function","4.define",1
    ],
    [ 
        "K. what is the output of 2*8?","1.12","2.14","3.18","4.16",4
    ],
    [
        "L. which loop is used when the number of iterations is knows?","1.while","2.do_while","3.for","4.loop",3
    ],
    [ 
        "M. which operator is used for equality chake?","1.=","2.==","3.===","4.!=",2
    ],
    [ 
        "N. which is the largest ocean on earth?","1.indian","2.pacific","3.arctic","4.gonga",2
    ],
    [ 
        "O. which data structure use key and value pairs?","1.list","2.tuples","3.dictonary","4.set",3
    ],
    [ 
        "P. what dose ram stand for?","1.random access memory","2.read access memory","3.run access memory","4.rapid access module",1
    ],
    [
        "Q. which method is used to add an element to a list?","1.append()","2.add()","3.push()","4.insert()",1
    ],
    


]
level=[1000,2000,3000,5000,10000,20000,30000,50000,80000,100000,230000,500000,1000000,2500000,5000000,10000000]
money=0
try:
    for i in range(0,len(qu)):
        question=qu[i]
        print(f"\n\n{question[0]}")
        print(f"{question[1]}\n{question[2]}\n{question[3]}\n{question[4]}")
        print(f"question for Rs.{level[i]}")
        user=int(input("enter your anewer or 0 to quite:>>>>>> "))
        if user==0:
            money=level[i-1]
            break
        if user==question[-1]:
            print(f"right anewer you have won Rs{level[i]}")
            if i==2:
                money=3000
            elif i==5:
                money=20000
            elif i==8:
                money=80000
            elif i==10:
                money=230000
            elif i==15:
                money=1000000
            elif i==18:
                money=5000000
            elif i==20:
                money=10000000
        else:
            print(f"worng answer right ans is{question[-1]}")
            break
    print(f"your take home money is {money}")
except:
    print("worng input")                                              

