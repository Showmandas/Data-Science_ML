class Student:
     def __init__(self,name,Id):
          self.name=name
          self.Id=Id
    
     def display(self):
          print(f"Name is {self.name} and ID is {self.Id}")
     
     def empty(self):
          pass

details=Student("John","23")
details.display()