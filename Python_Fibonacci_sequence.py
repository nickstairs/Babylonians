#Fibonacci Sequence Program
def fib(n):
     
    a = 0
    b = 1

    if n < 0:
        print("n value cannot be negative, please enter a valid value") #if n is negative
    elif n == 1:
        print(a)

    else:
        print(a)
        print(b)

        for i in range(2,n): # 2 elements are printed so 0 and 1 are already occupied now from index 2 start
        
            c = a + b #we are trying to shift values of a&b from 0,1 to 1,1 then 1,2 then 2,3 and so on
            a = b #shift values from a,b
            b = c
            print(c)
fib(15)
