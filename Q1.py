#Write a Python program to create a person class. Include attributes like name,
#country and date of birth. Implement a method to determine the person's age.

import datetime
from datetime import date

class Person():
    def __init__(self,name,country,date_r,current,age):
        self.name=name
        self.country=country
        self.date_r=date_r
        self.current=current
        self.age=age
    def age_cal(self):
        if self.current < date_r:
            print("Invalid dob")
        else:
            self.age=self.current-self.date_r
    def display(self):
        print(f"\n|      User Details     |\n\nName of User:{self.name}\nCountry of User:{self.country}\nAge of User:{self.age}")
        
name=input("Enter your name:")
country=input("Enter your country:")
y,m,d=[int(i) for i in input("Enter your Date of Birth(eg:yyyy-mm-dd):").split("-")]
date_r=datetime.date(y, m, d)
current=date.today()
current=date.year(current)
age=0
obj=Person(name,country,date_r,current,age)
obj.age_cal()
obj.display()