#default constructor Example

class student():
    def __init__(self):
        self.student_name='Rajganesh'
        self.student_Age=19
        self.student_mark=100
        print("Student Name:",self.student_name,"\nStudent Age:",self.student_Age,"\nself.student Mark",self.student_mark)
student=student()


#parameterized constructor Example

class student():
    def __init__(self,name,age,mark):
        self.student_name=name
        self.student_Age=age
        self.student_mark=mark
        print("Student Name:",self.student_name,"\nStudent Age:",self.student_Age,"\nself.student Mark",self.student_mark)
student=student('Rajganesh',19,100)


"""
default method no argument passed
it has only one argument that is self 
"""
