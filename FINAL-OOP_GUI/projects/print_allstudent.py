class Print_allstudent:
    def __init__(self, student):
        self.student_data = student
    
    def printStudentInfo(self):
        stu = ""
        for student in self.student_data.allstudents:
            stu += f"{student}\n\n"
        return stu
        
