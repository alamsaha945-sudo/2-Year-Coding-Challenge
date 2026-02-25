# Time Greeting Choice System 
import time
timestamp=time.strftime('%H:%M:%S')
t=int(time.strftime('%H'))
print(t)
if(t>=0 and t<12):
    print("good morning sir")
elif(t>=12 and t<17):
    print("good afternoon sir")
elif(t>=17 and t<0):
    print("good night sir")       