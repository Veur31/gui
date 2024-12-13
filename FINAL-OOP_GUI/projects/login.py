class Login:
    def __init__(self, student):
        self.student_data = student

    def login(self, idnumber):
        for student in self.student_data.allstudents:
            if idnumber == student.idnum:
               
                return student
        return None
            
