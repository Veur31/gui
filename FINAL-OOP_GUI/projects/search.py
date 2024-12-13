class Search:
    def __init__(self, student):
        self.student_data = student

    def search_student(self, searchword):
        for x in self.student_data.allstudents:
            if x.idnum == searchword:
                return f"\nStudent found. Greetings!\n{x}!"
        return "Error Student not found."
    def verify(self, searchword):
        for x in self.student_data.allstudents:
            if x.idnum == searchword:
                print(f"Welcome {x.getName()}")
                return x.getIDNum()
        return False
        
