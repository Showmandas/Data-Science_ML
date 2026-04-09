#Single Inheritance
class Person:
    def info(self):
        print("This is a person")
    def extra_info():
        print("This is parent class")

class Person_2(Person):
    def info_2(self):
        print("This is another person info")
    def extra_info():
        print("This is child class")


personInfo=Person_2()
personInfo.info()
personInfo.info_2()



#Multilevel Inheritance
class Student:
    def StudInfo(self):
        print("This is Student_1")
     
    def studentClass():
        print("This is parent class Of Student")


class Student_2(Student):
    def studInfo_2(self):
        print("This is another another info")
    #method overriding
    def studentClass():
        print("This is child class Of Student")


class Student_3(Student_2):
    def studInfo_3(self):
        print("This is the combination of two student details")

StudentInfo=Student_3()
StudentInfo.StudInfo()
StudentInfo.studInfo_2()
StudentInfo.studInfo_3()


#Hierarchical 
class Teacher:
    def TInfo(self):
        print("This is Teacher no 1 info")
    
    def teacherClass():
        print("This is parent class Of Teacher")


class Student_1(Teacher):
    def studInfo(self):
        print("This is Student info")
    #method overriding
    def teacherClass():
        print("This is child class Of Teacher")


class Student2(Student_1):
    def studInfo2(self):
        print("This is another student info")


info_1=Student_1()
info_2=Student2()
info_1.TInfo()
info_1.studInfo()
info_2.TInfo()
info_2.studInfo2()