class Student:
    def __init__(self,firstName,lastName,phone):
        self.firstName=firstName
        self.lastName=lastName
        self.phone=phone
    def display(self):
        print "First Name:",self.firstName
        print "Last Name:",self.lastName
        print "Phone:",self.phone

class Grade(Student):
	class Grade(Student):
    def __init__(self,firstName,lastName,phone,score):
		Student.__init__(self,firstName,lastName,phone) #Ye old style hai //agar upper Student(object) hota to yaha new 
		self.score = score								#style use karte super(childclassName,self).__init__(args)
    
    def calculate(self):
		if self.score<40:
			return "D"  
		elif 40<=self.score<60:
			return "B"
		elif 60<=self.score<75:
			return "A"
		elif 75<=self.score<90:
			return "E"
		elif 90<=self.score<=100:
			return "O"

firstName=raw_input().strip()
lastName=raw_input().strip()
phone=int(raw_input())
score=int(raw_input())
stu=Grade(firstName,lastName,phone,score)
stu.display()
print "Grade:",stu.calculate()