class Studentinfo:
    def __init__(self):
        self.allstudents = []
    
    def setFirstname (self, name):
        self.name = name

    def setAge(self, age):
        self.age = age
    
    def setIDNum(self, idnum):
        self.idnum = idnum

    def setEmail(self, email):
        self.email = email
    
    def setPhoneNum(self, phone):
        self.phone = phone

    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    def getIDNum(self):
        return self.idnum

    def getEmail(self):
        return self.email
    
    def getPhoneNum(self):
        return self.phone
    
    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nID Number: {self.idnum}\nEmail: {self.email}\nPhone: {self.phone}"
    

    def read(self):
        with open("projects/student.txt", "r") as f:
            read = f.readlines()
       
            for i in read[0:]:
                load = Studentinfo()
                line_strip = i.strip().split(",")
                if len(line_strip) == 5:
                    load.setFirstname(line_strip[0])
                    load.setAge(line_strip[1])
                    load.setIDNum(line_strip[2])
                    load.setEmail(line_strip[3])
                    load.setPhoneNum(line_strip[4])
                    self.allstudents.append(load)




