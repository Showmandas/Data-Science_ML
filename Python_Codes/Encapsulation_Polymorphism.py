class Student:
    def __init__(self,name,id):
        self.__id=id
        self.name=name
    
    def get_id(self):
        print(f"Id is {self.__id}") #getter method for accessing private method

    def __init__(self, name, id,age=26):
        self.name=name
        self.id=id
        self.age=age
        


info=Student("John",43)
info.get_id()


class a:
    def display(self):
        print("This is class a")


class b:
    def display1(self):
        print("This is class b")

class c:
    def display2(self):
        print("This is class c")


obj=c()
obj.display()
obj.display1()
obj.display2()