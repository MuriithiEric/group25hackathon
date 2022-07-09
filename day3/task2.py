#ask the user the amount of fat in grams they consume in a day
nutritionist = str(input("Please enter the number of fat in grams do you consume in a day: \n"))

#store the value int
fat = int(nutritionist)

#ask the user the amount of fat in grams they consume in a day
nutritionist2 = str(input("Please enter the number of carbs in grams do you consume in a day: \n"))
#store the value int
carbs = int(nutritionist2)

# formula to convert calories to fat and vise versa
caloriesfromfat = fat * 9
caloriesfromcarbs = carbs * 4

# prints out the result
print("You have consumed", caloriesfromfat, "calories from fat and", caloriesfromcarbs, "calories from carbs")