/**
* used datetime library to get the exact date and time
* used strftime() method to return a string representing date and time
* used the ternary operator != 
*/

#datetime library used to manipulate time events

from datetime import datetime 
from datetime import date
date = date.today()
day = datetime.today().strftime('%A')[0:3] #truncates, gives a range

#password stored in a variable
password = 'eric' 
#commands to open and close the door are stored in a variable
optionone = 'open' 
optiontwo = 'close'
optionthree = 'quit'
pwd = str(input("Please enter a password: \n"))

while (pwd != password):
    #password validation
    print("Please enter the correct password")  
    pwd = str(input("Please enter a password: \n"))
else:
    print("Correct password")

door = str(input("Would indicate if you would like to OPEN or CLOSE the door? Alternatively, you can indicate if you'd like to QUIT \n"))

#condition is displayed when the user opens the door
if door == optionone:

    #datetime function prints the exact time the door was opened or closed
    print("Door was last opened at: ", datetime.now().strftime('%Y-%m-%d %H:%M:%S')) 

#condition is closeded when the user opens the door    
elif door == optiontwo:
    print("The door is now locked", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

elif door == optionthree:
    print("This process has been terminated.")

else:
    print("Invalid input")



