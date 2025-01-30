GRADES = ['A','B','C','D','F']  # GRADES constant to compare with entered grades

class Person:
    """Class `Person` responsible for to be inherited by classes `Students` and `Teacher`"""
    def __init__(self, name: str, age: int):
        self.__name = str(name)
        self.__age = int(age)

    def getName(self) -> str:
        return self.__name

    def __str__(self) -> str:
        return "Name: {}, Age: {}".format(self.__name, self.__age)
    
class Student(Person):
    """Class `Student` responsible for create `Student` objects and interact with `Classroom` objects"""
    def __init__(self, name: str, age: int, student_id: int, grade: str):
        super().__init__(name,age)
        self.__student_id = int(student_id)
        self.__grade = str(grade)

    def getID(self) -> int:
        return self.__student_id
    
    def getGrade(self):
        return self.__grade

    def get_details(self) -> str:
        return super().__str__() + ", Student ID: {}, Grade: {}".format(self.__student_id, self.__grade)
    
    def __str__(self) -> str:
        return self.get_details()

class Teacher(Person):
    """Class `Teacher` responsible for create `Teacher` objects and interact with `Classroom` objects"""
    def __init__(self, name: str, age: int, teacher_id: int, subject: str):
        super().__init__(name, age)
        self.__teacher_id = int(teacher_id)
        self.__subject = str(subject)

    def getID(self) -> int:
        return self.__teacher_id
    
    def getSubject(self) -> str:
        return self.__subject

    def get_details(self):
        return super().__str__() + ", Teacher ID: {}, Subject: {}".format(self.__teacher_id, self.__subject)
    
    def __str__(self):
        return self.get_details()
    
class Classroom:
    """Class `Classroom` responsible for interact with classes `Teacher` and `Student`.
    There can be assigned a teacher and added students"""
    def __init__(self, classroom_number: int):
        if (isinstance(classroom_number, int)):
            self.__room_number = int(classroom_number)
        self.__students = []
        self.__teacher = None

    def getRoomNumber(self) -> int:
        return self.__room_number
    
    def getTeacher(self) -> Teacher:
        return self.__teacher
    
    def getStudentList(self) -> list[Student]:
        return self.__students
    
    def search_students_by_grade(classroom,grade: str) -> list:
        return list(filter(lambda x: (x.getGrade() == grade), students))
    
    def assignTeacher(self, teacher: Teacher):
        self.__teacher = teacher

    def add_student(self, student: Student):
        self.__students.append(student)

# List variables to store `Student` objects, `Teacher` objects and `Classroom` objects
students : list[Student] = []
teachers : list[Teacher] = []
classrooms : list[Classroom] = []

# Functions that return boolean value to check the validation
def isFreeStudentID(student_id: int) -> bool:
    if (student_id <= 0):
        print("Student ID must be positive!")
        return False
    for student in students:
        if (student.getID() == student_id):
            print("Student is already exist!")
            return False
    return True

def isFreeTeacherID(teacher_id: int) -> bool:
    if (teacher_id <= 0):
        print("Teacher ID must be positive!")
        return False
    for teacher in teachers:
        if (teacher.getID() == teacher_id):
            print("Teacher is already exist!")
            return False
    return True

def studentExistence(student_id : int) -> Student:
    for student in students:
        if (int(student_id) == student.getID()):
            return student
    return None

# Functions that return objects value to check the existence of objects by id
def teacherExistence(teacher_id : int) -> Teacher:
    for teacher in teachers:
        if (int(teacher_id) == teacher.getID()):
            return teacher
    return None

def classroomExistence(classroomNumber : int) -> Classroom:
    for classroom in classrooms:
        if (int(classroomNumber) == classroom.getRoomNumber()):
            return classroom
    return None

# Main code
if __name__ == "__main__":
    print("Welcome to the Mini School Management System!")
    print("Menu:\n" +
        "   1. Add a student\n" +
        "   2. Add a teacher\n" +
        "   3. Assign teacher to a classroom\n" +
        "   4. Add student to a classroom\n" +
        "   5. Display classroom information\n" +
        "   6. Search for students by grade\n" +
        "   7. Exit\n")
    
    while True:
        cmd = str(input("Enter your choice: "))
        match (cmd):
            case '1':   # 1. Add a student
                name = str(input("Enter student name: ")).strip()
                if (len(name) == 0):
                    print("Name cannot be empty!")
                    continue

                age = str(input("Enter age: "))
                if (not age.isnumeric()):
                    print("Age must be an integer!")
                    continue

                student_id = str(input("Enter student ID: "))
                if (student_id.isnumeric()):
                    if (not isFreeStudentID(int(student_id))):
                        continue
                else:
                    print("Student ID is not an integer!")
                    continue

                grade = str(input("Enter grade: ")).upper().strip()
                if (not grade in GRADES):
                    print("There is no such grade!")
                    continue

                students.append(Student(name, int(age), int(student_id), grade))
                print("Student \"{}\" added successfully!".format(name))

            case '2':   # 2. Add a teacher
                name = str(input("Enter teacher name: ")).strip()
                if (len(name) == 0):
                    print("Name cannot be empty!")
                    continue
                
                age = str(input("Enter age: "))
                if (not age.isnumeric()):
                    print("Age must be an integer!")
                    continue

                teacher_id = str(input("Enter teacher ID: "))
                if (teacher_id.isnumeric()):
                    if (not isFreeTeacherID(int(teacher_id))):
                        continue
                else:
                    print("Teacher ID must be an integer!")

                subject = str(input("Enter subject: ")).strip()
                if (len(subject) == 0):
                    print("Subject must be entered!")

                teachers.append(Teacher(name, int(age), int(teacher_id), subject))
                print("Teacher \"{}\" added successfully!".format(name))

            case '3':   # 3. Assign teacher to a classroom
                classroom_number = str(input("Enter classroom number: "))
                if (not classroom_number.isnumeric()):
                    print("Classroom number must be an integer!")
                    continue
                if (classroomExistence(classroom_number) != None):
                    classroom = classroomExistence(classroom_number)
                else:
                    classroom = Classroom(int(classroom_number))
                teacher_id = str(input("Enter teacher ID to assign: "))
                if (not teacher_id.isnumeric()):
                    print("Teacher ID must be an integer!")
                    continue
                if (teacherExistence(teacher_id) != None):
                    teacher = teacherExistence(teacher_id)
                    classroom.assignTeacher(teacher)
                    classrooms.append(classroom)
                    print("Teacher \"{}\" assigned to classroom {} successfully!".format(teacher.getName(), classroom.getRoomNumber()))
                else:
                    print("Teacher does not exist!")
                    continue

            case '4':   # 4. Add student to a classroom
                classroom_number = str(input("Enter classroom number: "))
                if (not classroom_number.isnumeric()):
                    print("Classroom number must be an integer!")
                    continue
                if (classroomExistence(classroom_number) != None):
                    classroom = classroomExistence(classroom_number)
                else:
                    classroom = Classroom(classroom_number)

                student_id = str(input("Enter student ID to assign: "))
                if (not student_id.isnumeric()):
                    print("Student ID must be an integer!")
                    continue
                if (studentExistence(student_id) != None):
                    student = studentExistence(student_id)
                    classroom.add_student(student)
                    classrooms.append(classroom)
                    print("Student \"{}\" added to classroom {} successfully!".format(student.getName(), classroom.getRoomNumber()))
                else:
                    print("Student does not exist!")

            case '5':   # 5. Display classroom information
                classroom_number = str(input("Enter classroom number: "))
                if (not classroom_number.isnumeric()):
                    print("Classroom number must be an integer!")
                    continue
                if (classroomExistence(classroom_number) != None):
                    classroom = classroomExistence(classroom_number)
                    teacher = classroom.getTeacher()
                    student_list = classroom.getStudentList()
                    print("Classroom {}:".format(str(classroom.getRoomNumber())))
                    if (teacher != None):
                        print("Teacher: {}, Subject: {}".format(teacher.getName(),teacher.getSubject()))
                    if (len(student_list) > 0):
                        print("Students: ")
                        for i in range(len(student_list)):
                            print("{}. {} (ID: {})".format(i+1, student_list[i].getName(), student_list[i].getID()))
                else:
                    print("Classroom does not exist!")
                    continue
                
            case '6':   # 6. Search for students by grade
                classroom_number = str(input("Enter classroom number: "))
                if (not classroom_number.isnumeric()):
                    print("Classroom number must be an integer!")
                    continue
                if (classroomExistence(classroom_number) != None):
                    classroom = classroomExistence(classroom_number)

                    grade = str(input("Enter grade to search for: ")).upper().strip()
                    if (not grade in GRADES):
                        print("There is no such grade!")
                        continue
                    student_list = classroom.search_students_by_grade(grade)
                    
                    if (len(student_list) > 0):
                        print("Students with grade {} in classroom {}:".format(grade, str(classroom.getRoomNumber())))
                        for i in range(len(student_list)):
                            print("{}. {} (ID: {})".format(i+1, student_list[i].getName(), student_list[i].getID()))
                    else:
                        print("Nothing found!")
                else:
                    print("Classroom does not exist!")
                    continue
            case '7':   # 7. Exit
                break
            case '_':
                print("Invalid command!")