class Student:
    def __init__(self,name,student_no,course):
        self.name=name 
        self.student_no=student_no
        self.course=course
    
    def study (self):
        print(f'{self.name} studies')
    def details (self):
        print(f'{self.name} student number{self.student_no} studies {self.course}')
    def eats (self):
        print(f'{self.name} eats ')
    def sleeps (self):
        print(f'{self.name} sleeps')
        
#object 1
student1=Student('jack','st1','Computer_science')
print(student1.name)

#object 2 
student2=Student('jane','st2','computer_engineering')
student2.details()