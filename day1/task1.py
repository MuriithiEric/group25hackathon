/**
* Bus Fare Challenge – Task One (Day 1)
* date.today() - prints the current days date
*/

from datetime import datetime  # imports third party libraries to manipulate time
from datetime import date

#initializes the date object 
date = date.today() 

#truncates, gives a range of the day upto the third letter
day = datetime.today().strftime('%A')[0,3] 

#prints out the date in date as a string
print('Date: ', date) 
print('Day: ', day) 

#conditions to evaluate bus fare according to the day
if day == 'Sat':
    print('Fare: 60')
elif day == 'Sun':
    print('Fare: 80')
else:
    print('Fare: 100')        
