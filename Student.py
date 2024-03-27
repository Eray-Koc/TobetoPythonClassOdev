class Student:

    def __init__(self, name, surname, age) -> None:
        self.name = name
        self.surname = surname
        self.age = age
    
    def printdetails(self):
        print(f"Ad : {self.name} \n Soyad : {self.surname} \n Yaş : {str(self.age)}")