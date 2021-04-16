#This code shows how if you continue to sum the halves it never hits 1 but rather .99....
n=0
x=.5
n+=.5
print(n)
import time
while n<1:
    time.sleep(.5);
    n*=0.5
    print(n , 'half of previous')
    if n<1:
        x+=n
        print(x , "Is the Total Sum")
        continue
    if n>=1.0:
        print("breaking")
        break

