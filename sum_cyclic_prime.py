#using python2.7 穷尽效率低，数据大耗时多
import math  
def isPrime(num):  
    for i in range(2,int(math.sqrt(num)+1)):  
        if num%i==0:  
            return False  
    return True  
  
n=input()  
count=0  
for k in range(2,n):  
    if isPrime(k):  
        t_str=str(k)  
        t_len=len(t_str)  
        if t_len==1:  
            count+=1  
        else:  
            for t in range(1,t_len):  
                t_str=t_str[1:]+t_str[0]  
                tmp=int(t_str)  
                if not isPrime(tmp):  
                    break  
            else:  
                count+=1  
print count  
#using python 3.6 效率高些
import math  
def isPrime(num):  
    for i in range(3,int(math.sqrt(num)+1),2):  
        if not num%i:  
            return False  
    else:  
        return True  
      
n=int(input())  
numList = [2,3,5,7]  
for num in range(11,n):  
    for s in str(num):  
        if s in ['0','2','4','5','6','8']:  
            break  
    else:  
        if isPrime(num):  
            t_str=str(num)  
            t_len=len(t_str)  
            for t in range(1,t_len):  
                t_str=t_str[1:]+t_str[0]  
                tmp=int(t_str)  
                if not isPrime(tmp):  
                    break  
            else:  
                numList.append(tmp)  
  
print(len(numList))  
