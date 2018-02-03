#using python2.7
day_Sum = 1  
count = 0  
for year in range(1900,2001):  
    for month in range(1,13):  
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:  
            day = 31  
        elif month == 4 or month == 6 or month == 9 or month == 11:  
            day = 30  
        elif month == 2:  
            if(year % 400 == 0)or(year % 4 == 0 and year % 100 == 0):  
                day = 29  
            else:  
                day = 28  
        day_Sum + = day  #因为是看一个月的第一天是不是周日，所以总天数是所day再加上1，所以day_sum初始值为1的原因
        if day_Sum % 7 == 0 and year > 1900:  
            count + = 1  
print count  
#using python3.6
day_Sum = 1  
count = 0  
for year in range(1900,2001):  
    for month in range(1,13):  
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:  
            day = 31  
        elif month == 4 or month == 6 or month == 9 or month == 11:  
            day=30  
        elif month == 2:  
            if(year%400 == 0)or(year%4 == 0 and year%100 == 0):  
                day = 29  
            else:  
                day = 28  
        day_Sum += day  
        if day_Sum % 7 == 0 and year > 1900:
            count += 1 
print (count)  
