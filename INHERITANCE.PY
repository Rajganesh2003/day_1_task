class student:
    def __init__(self,name,department,mark1,mark2,mark3):
          self.name=name
          self.department=department
          self.mark1=mark1
          self.mark2=mark2
          self.mark3=mark3
class averagemark(student):
    def average(self):
        self.average=(self.mark1+self.mark2+self.mark3)/3
        print("Average:",self.average)

student1=averagemark("Rajganesh",'ECE',99,98,97)
student1.average()
