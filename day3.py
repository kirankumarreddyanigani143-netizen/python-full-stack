class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.course = "PFSD"
        
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print(self.name, "is studying PFSD")


s1 = Student("Kiran", 21)

s1.display()


