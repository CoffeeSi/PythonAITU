import os, csv, json
# Import libraries such as  `os` for file management
#                           `csv` to work with csv files
#                           `json` to work with json files and formatting

# Constants days in months, employee fields to export and import data
MONTHS = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
EMPLOYEES_FIELD = ["ID", "Name", "Position", "Salary", "Skills", "Employment Date"]

# Employee Storage List (ESL)
employees = []

# Import employees from file to ESL
try: # Check for file existence 
    with open(r"employees.csv", 'r') as csvfile:
        read = csv.DictReader(csvfile)
        for row in read:
            employees.append(row)

# If file not found - create new one
except FileNotFoundError:
    with open("employees.csv","w") as csvfile:
        write = csv.DictWriter(csvfile, EMPLOYEES_FIELD)
        write.writeheader()
print(employees)

# Greeting and menu display
print("Welcome to the Advanced Employee Management System!")
print("Menu:\n" +
    "1. Add an employee\n" +
    "2. Search for employees\n" + 
    "3. Remove an employee\n" +
    "4. Update employee information\n" + 
    "5. Display all employees\n" +
    "6. Generate analytics\n" +
    "7. Save data to JSON\n" +
    "9. Export data to CSV\n" +
    "11. Delete a file\n" +
    "12. Exit")

while True:
    # Always asking for command
    cmd = str(input("Your choice: "))   # Use str for convenience, no need in try-except
    if (cmd.isnumeric()):               # If command is not a number it won't work
        match (cmd):                    # Switch-case for commands 
            case '1': # Add an employee
                # Input ID
                try:
                    idEmployee = int(input("Enter employee ID: "))
                    for employee in employees:
                        if (str(idEmployee) in str(employee["ID"])):
                            raise
                except:
                    print("Employee ID is incorrect or alreay in the list!")
                    continue
                # Input Name
                name = str(input("Enter employee name: "))
                # Input Position
                position = str(input("Enter employee position: "))
                # Input Salary
                try:
                    salary = int(input("Enter employee salary: "))
                    if (salary < 0): raise
                except:
                    print("Incorrect salary")
                    continue
                # Input skills
                skills = str(input("Enter skills (comma-separated): "))
                skills = ",".join([x.strip() for x in skills.split(',')])
                # Input date
                try:
                    date = str(input("Enter employment date (YYYY-MM-DD): "))
                    date_ = list(map(int, date.split("-")))

                    # Date validation 
                    if (len(date_) == 3):
                        if not (1900 <= date_[0] <= 2099 and 0 <= date_[1] <= 12 and 0 <= date_[2] <= MONTHS[date_[1]-1]):
                            raise
                        else:
                            year = str(date_[0])
                            if (0 <= date_[1] <= 9):
                                month = '0' + str(date_[1])
                            else:
                                month = str(date_[1])
                            if (0 <= date_[2] <= 9):
                                day = '0' + str(date_[2])
                            else:
                                day = str(date_[2])
                    date = '-'.join([year,month,day])
                except:
                    print("Incorrect date")
                    continue

                # Add an employee in the ESL
                EmployeeList = {"ID":idEmployee, "Name":name, "Position":position, 
                                "Salary":salary, "Skills":skills, 
                                "Employment Date":date}
                employees.append(EmployeeList)
                print("Employee added successfully!")

            case '2': # Search for employees
                searchby = str(input("Search by (id/name/skills): ")).strip().lower()
                # Search by ID
                if (searchby == "id"):
                    try:
                        idEmployee = int(input("Enter employee ID: "))
                    except:
                        print("Employee ID is incorrect!")
                        continue
                    for i in range(len(employees)):
                        if (str(idEmployee) == str(employees[i]["ID"])):
                            for field in EMPLOYEES_FIELD:
                                print("{}: {}".format(field, employees[i][field]), end=', ')
                            print()
                # Search by name
                elif (searchby == "name"):
                    nameEmployee = str(input("Enter employee's name: "))
                    n = 1   # Counter lines
                    for i in range(len(employees)):
                        if (nameEmployee.strip().lower() in str(employees[i]["Name"]).lower()):
                            print("{}".format(n), end=". ")
                            n += 1
                            for field in EMPLOYEES_FIELD:
                                print("{}: {}".format(field, employees[i][field]), end=', ')
                            print()
                # Search by skills
                elif (searchby == "skills" or searchby == "skill"):
                    skillEmployee = str(input("Enter employee's skill: "))
                    n = 1   # Counter lines
                    for i in range(len(employees)):
                        if (skillEmployee.strip().lower() in str(employees[i]["Skills"]).lower()):
                            print("{}".format(n), end=". ")
                            n += 1
                            for field in EMPLOYEES_FIELD:
                                print("{}: {}".format(field, employees[i][field]), end=', ')
                            print()

            case '3': # Remove an employee from the list
                try:
                    idEmployee = int(input("Enter employee ID to remove: "))
                    if (len(employees) == 0): 
                        print("Employee ID is not in the list!")
                    for i in range(len(employees)):
                        if (str(idEmployee) in employees[i]["ID"]):
                            employees.pop(i)
                            print("Employee has been removed successfully!")
                            break
                except:
                    print("Employee ID is incorrect or not in the list!")
                    continue
            
            case '4': # Update employee information
                updating = str(input("Update (salary/skills): ")).strip().lower()
                # Update employee's salary
                if (updating == "salary"):
                    try:
                        idEmployee = int(input("Enter employee ID to update salary: "))
                    except:
                        print("Employee ID is incorrect!")
                        continue
                    index = -1  # Employee index 
                    for i in range(len(employees)):
                        if (str(idEmployee) == str(employees[i]["ID"])):
                            index = i
                            for field in EMPLOYEES_FIELD:
                                print("{}: {}".format(field, employees[i][field]), end=', ')
                            print()
                    if (index == -1):
                        print("Employee ID is not in the list!")
                    try:
                        newSalary = int(input("Enter new salary: "))
                    except:
                        print("Salary is incorrect!")
                        continue
                    employees[index]["Salary"] = newSalary
                    print("Salary updated successfully!")

                # Update employee's skills
                if (updating == "skills"):
                    try:
                        idEmployee = int(input("Enter employee ID to update skill: "))
                    except:
                        print("Employee ID is incorrect!")
                        continue
                    index = -1
                    for i in range(len(employees)):
                        if (str(idEmployee) == str(employees[i]["ID"])):
                            index = i
                            for field in EMPLOYEES_FIELD:
                                print("{}: {}".format(field, employees[i][field]), end=', ')
                            print()
                    if (index == -1):
                        print("Employee ID is not in the list!")
                    skillQuery = str(input("add or remove (default add): ")).strip().lower()

                    # Remove employee's skill
                    if (skillQuery == "remove" or skillQuery == '-'):
                        remSkill = str(input("Enter skill to remove: ")).strip().lower()
                        for i in range(len(employees)):
                            skills = employees[index]["Skills"]
                            skillList = [x.strip().lower() for x in skills.split(',')]
                            if (remSkill in skillList):
                                indSkill = skillList.index(remSkill)
                                skillList.pop(indSkill)
                                employees[index]["Skills"] = ','.join(skillList)
                                print("Skill removed successfully!")
                            else:
                                print("Skill is not in the list!")
                                continue

                    # Add a skill to an employee
                    elif (skillQuery == "add" or skillQuery == '+' or skillQuery == ''):
                        newSkill = str(input("Enter skill to add: "))
                        employees[index]["Skills"] += ',{}'.format(newSkill)
                        print("Skill added successfully!")
                    else:
                        print("Invalid command!")
                        continue
            case '5':   # Display all employees 
                # Filtering and sorting params
                filtering = str(input("Filter by position (leave blank for all): ")).lower().strip()
                sorting = str(input("Sort by (salary/employment_date/none): ")).lower().strip()
                
                # Sort by salary
                if (sorting == "salary"):
                    sorti = str(input("ascending/descending(default desc): ")).lower().strip()
                    asc = False
                    if (sorti == "asc" or sorti == "ascending"): asc = True
                    sortedEmployees = sorted(employees, reverse=asc,
                                            key=lambda salary: int(salary["Salary"]))
                    
                # Sort by employment date
                elif (sorting.lower().strip() == "employment_date"):
                    sortedEmployees = sorted(employees, reverse=True,
                                            key=lambda date: int("".join(date["Employment Date"].split('-'))))
                # Do not sort
                elif (sorting.lower().strip() == "" or sorting.lower().strip() == "none"):
                    sortedEmployees = employees
                else:
                    print("There is no such sort key")
                    continue
                n = 1   # Lines counter

                # Display employees with sorting above
                print("Employees: ")
                for i in range(len(employees)):
                    if (filtering == employees[i]["Position"].lower() or 
                        filtering in employees[i]["Skills"].lower() or
                        filtering == ""):
                        print("{}.".format(n), end=' ')
                        n += 1
                        for field in EMPLOYEES_FIELD:
                            print("{}: {}".format(field, sortedEmployees[i][field]), end=', ')
                        print()

            case '6':   # Generate analytics 
                # Calculate total payroll and average salary
                total = 0
                for employee in employees:
                    total += int(employee['Salary'])
                average = total // len(employees)

                # Sort by salary to take first(Lowest) and last(Highest)
                sortedEmployees = sorted(employees, key=lambda salary: int(salary["Salary"]))

                # Calculate Highest and Lowest salary and names
                highestName = sortedEmployees[len(employees)-1]["Name"]
                highest = sortedEmployees[len(employees)-1]["Salary"]
                lowestName = sortedEmployees[0]["Name"]
                lowest = sortedEmployees[0]["Salary"]

                # Represent analitics
                print("-  Total Payroll: ${:,}".format(total))
                print("-  Average Salary: ${:,}".format(average))
                print("-  Highest Salary: {} (${:,})".format(highestName, int(highest)))
                print("-  Lowest Salary: {} (${:,})".format(lowestName, int(lowest)))
                
            case '7':   # Save data to JSON
                with open(r"employees.json", "w") as jsonfile:
                    write = jsonfile.write(json.dumps(employees,indent=4))
                    print("Data successfully saved to JSON!")
            case '9':   # Export changes to CSV file
                with open(r"employees.csv", "w",newline='') as csvfile:        
                    # Use newline='' to prevent making spacelines in csv file  
                    write = csv.DictWriter(csvfile, EMPLOYEES_FIELD,quotechar="\"")
                    write.writeheader()
                    write.writerows(employees)
                print("Data successfully exported to CSV!")
            case '11':  # Delete a file 
                try:
                    os.remove('./employees.csv')
                    print("File has been deleted!")
                except FileNotFoundError:
                    print("File not found, add an employee to create a file")
                    continue
            case '12':  # Exit
                print("Thank you for using the Employee Management System. Goodbye!")
                break
            case _:     # Neither of above
                print("Unknown command!")
    else:
        print("Unknown command!")