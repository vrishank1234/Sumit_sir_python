# 10. Create three classes, “Person,” “Employee,” and “Student.” Use multiple
# inheritance to create a class “PersonInfo” that inherits from both “Employee” and
# “Student.” Add attributes and methods specific to each class.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Employee:
    def __init__(self, employee_id, department):
        self.employee_id = employee_id
        self.department = department

    def display_employee(self):
        print(f"Employee ID: {self.employee_id}, Department: {self.department}")

    def working(self):
        print("Employee is working.")


class Student:
    def __init__(self, student_id, major):
        self.student_id = student_id
        self.major = major

    def display_student(self):
        print(f"Student ID: {self.student_id}, Major: {self.major}")

    def studying(self):
        print("Student is studying.")


class PersonInfo(Employee, Student):
    def __init__(self, name, age, employee_id, department, student_id, major):
        Employee.__init__(self, employee_id, department)
        Student.__init__(self, student_id, major)
        Person.__init__(self, name, age)

    def display_person(self):

        self.display_employee()
        self.display_student()


def main():
    person_info = PersonInfo("Prem Thakare", 19, "BTCs02", "B.Tech", "E15", "Computer Science")

    person_info.display_person()
    person_info.working()
    person_info.studying()

if __name__=="__main__":
    main()