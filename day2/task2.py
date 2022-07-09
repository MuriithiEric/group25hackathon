career = ["You may want to consider a career as a MECHANIC", "You may want to explore a career as a MUSICIAN", "You may want to consider a career in PROGRAMMING", "You may want to purse a career in NURSING"] # career list

advice = ["Mechanics require good technical knowledge of automotive engines", "Musicians must practice excellent voice control", "Programmers must have excellent knowledge of fundamental programming concepts", "Nurses are genuine, caring person"] # advice list

questions = ["Would you be satisfied with this choice?", "Definitely consider if it a rewarding career.", "Who else do you know in this profession?", "Always consider how marketable this career is"] # questions list

qualities = ["Handy", "Musically Inclined", "Problem Solver", "Caring"] # qualities list

print("Which qualities best describe you: Handy, Musically Inclined, Problem Solver, Caring") # print statement

choice = str(input("Out of this list, please tell us which qualities best describe you: Handy, Musically Inclined, Problem Solver, Caring? ")) # input statement

if choice == qualities[0]: # if statement
    print(advice[0]) # these programs are used to print the advice,questions, and career list
    print(questions[0])
    print(career[0])

elif choice == qualities[1]: # if statement
    print(advice[1]) # these programs are used to print the advice,questions, and career list
    print(questions[1])  
    print(career[1])

elif choice == qualities[2]:
    print(advice[2])
    print(questions[2])  
    print(career[2])

elif choice == qualities[3]:
    print(advice[3])
    print(questions[3])      
    print(career[3])

else: # alternate result afte
    print("You need to input a valid career from the list!")    

