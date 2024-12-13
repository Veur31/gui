from student import *
class AddStudent:
    def __init__(self, student):
        self.student_data = student
    def add_student(self, student):
        self.student_data.allstudents.append(student)
        with open("projects/student.txt", "a") as f:
            student_list =f"{student.getName()},{student.getAge()},{student.getIDNum()},{student.getEmail()},{student.getPhoneNum()}"
            f.write(f"{student_list} \n")

    def save(self,name, age, idnum, email, phone):
        new_stu = Studentinfo()
        new_stu.setFirstname(name)
        new_stu.setAge(age)
        new_stu.setIDNum(idnum)
        new_stu.setEmail(email)
        new_stu.setPhoneNum(phone)
        self.add_student(new_stu)
        return f"Student {new_stu.getName()}, added successfully"



        