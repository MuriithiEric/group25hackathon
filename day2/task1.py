#prompts the user to ask for the number of books you have purchased this month
num = int(input("How many books have you purchased this month?")) # 


# conditionals to evaluate the value of the points that a user earns
if num == 0:
    print("You haven't earned any point.")

elif num == 1:
    print("You have earned 1 point.")    

elif num == 2:
    print("You have earned 16 points")    

elif num == 3:
    print("You have earned 32 points")   

elif num >= 4:
    print("You have earned 60 points")   

     