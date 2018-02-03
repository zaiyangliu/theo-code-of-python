#using python2.7
import math
n = int(raw_input())
sum = 0
 
for tmp in xrange(2, n):
    for i in xrange(2, int(math.sqrt(tmp)+ 1) ):
        if tmp % i == 0 :
            break
    else:
        sum += tmp
print sum


#using python3.6
import math
n = int(input())
sum = 0
 
for tmp in range(2, n):
    for i in range(2, int(math.sqrt(tmp)+ 1) ):
        if tmp % i == 0 :
            break
    else:
        sum += tmp
print (sum)
