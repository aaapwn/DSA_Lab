"""Student"""
class Student:
    def __init__(self, id, name, gpa):
        self.id = id
        self.name = name
        self.gpa = gpa

    def getID(self):
        return self.id
    
    def getName(self):
        return self.name
    
    def getGpa(self):
        return self.gpa
    
    def printDetail(self):
        print("ID: " + str(self.id))
        print("Name: " + self.name)
        print("GPA: " + str(self.gpa))
