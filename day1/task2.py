/**
* int(input) - adds functionality by getting input from a user
* print() - prints output  
*/

#prompts the user to give values for the value of the wall in square feet
wall = int(input("Enter the square feet of wall to be painted: "))
price = int(input("Enter price of the paint per gallon: "))

#gets the value of the charges in dollars
charges = 20

#formulas to evaluate the values of the number of gallons, hours of labor, cost of paint, labour charges, and total cost of the job
gallons = (wall/115)
hours = ((wall/115)*8)
cost_paint = gallons * price 
labour_charge = (hours * charges)
cost = price + labour_charge
print()
print("The number of gallons of paint required is : ", gallons)
print("The hours of labor required is : ", hours)
print("The cost of paint is:$", cost_paint)
print("The labour charges are:$", labour_charge)
print("The total cost of the paint job : ", cost)
