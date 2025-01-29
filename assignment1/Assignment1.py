#Greeting
print("Welcome to the Student Grading System!")

flag = True
while (flag):
    #Ask for student name
    name = str(input("Enter student name: "))

    #Ask for his test scores
    while True:
        try:
            score1 = int(input("Enter score for Test 1 (0-100): "))
            score2 = int(input("Enter score for Test 2 (0-100): "))
            score3 = int(input("Enter score for Test 3 (0-100): "))
        except:
            continue
        #Check scores are between 0 to 100
        if (0 <= score1 <= 100 and 0 <= score2 <= 100 and 0 <= score3 <= 100):
            break

    #Print name of a student and his scores
    print("\nCalculating results...")
    print("Student: {}".format(name))
    print("Test Scores: {}, {}, {}".format(score1, score2, score3))

    #Calculate average grade
    avg = float((score1+score2+score3)/3)
    avg = round(avg, 2)
    print("Average Score: {}".format(avg))

    #Assign a grade by average grade
    grade = ""
    if (0 < avg < 60): grade = "F"
    elif (60 <= avg < 70): grade = "D"
    elif (70 <= avg < 80): grade = "C"
    elif (80 <= avg < 90): grade = "B"
    elif (90 <= avg <= 100): grade = "A"
    print("Grade: {}".format(grade))

    #Ask for continue, if yes - it will start again, if no - it will end the program
    #If nothig - it will ask again
    while True:
        answer = input("\nDo you want to enter another student's details? (yes/no): ")
        if (answer.strip().lower() == "yes"):
            break
        elif (answer.strip().lower() == "no"):
            print("\nThank you for using the Student Grading System. Goodbye!")
            flag = False
            break