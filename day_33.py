# List Comprehensions
result=[]
try:
    a=int(input())
    b=int(input())
    c=int(input())
    n=int(input())
    for i in range(a+1):
        for j in range(b+1):
            for k in range(c+1):
                if i+j+k != n:
                    result.append([i,j,k])
                    print(result)
except Exception as e:
    print(e)                     