class Student:
    def __init__(self,fullName):
        self.name=fullName
        print("Adding a name in database..")
    
s=Student("Showman")
print(s.name)