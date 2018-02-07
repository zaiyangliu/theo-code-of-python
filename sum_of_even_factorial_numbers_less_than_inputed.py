#python 3.6
def fib(num):
    sum = 0
    p1 = 1
    p2 = 1
    i = 1
    result = 0
    while result < num:
        if i >= 1:
            if result % 2 == 0:
                sum += result
            result = p1 + p2
            p1,p2 = p2, p1 + p2
    print(sum)
num = int(input("please input an positive integer\n"))
print("the sum of the even factorial numbers less than the number you input\n")
fib(num)
#python 3.6 using recursion
def fib(n):  
    if n == 0 or n == 1:  
        return 1  
    else:  
        return fib(n - 1) + fib(n - 2)  
   
sum = 0  
i = 0  
num =  int(input())  
while fib(i) < num:  
    if fib(i) % 2 == 0:  
        sum += fib(i)  
    i += 1  
print (sum)  
