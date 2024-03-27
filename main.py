import Student
import Teacher

student_list = list()
teacher_list = list()

student2 = Student.Student("Ayça", "Güven", 21)
student_list.append(student2)
Student.Student.printdetails(student2)

student3 = Student.Student("Hilal", "Cebel", 21)
student_list.append(student3)
Student.Student.printdetails(student3)

student4 = Student.Student("Nisanur", "Baş", 21)
student_list.append(student4)
Student.Student.printdetails(student4)

student5 = Student.Student("Eray", "Koç", 21)
student_list.append(student5)
Student.Student.printdetails(student5)

student6 = Student.Student("Serpil Nur","Karaman", 21)
student_list.append(student6)
Student.Student.printdetails(student6)

teacher = Teacher.Teacher("İrem", "Balcı", 25, "Tester")
teacher_list.append(teacher)
Teacher.Teacher.printdetails(teacher)
