
class Dog: 
    def __init__(self , name , age ):
        self.name = name
        self.age = age 
    
    def run(self): 
        print(f"The {self.name} is running")
    
    def roll_over(self):
        print(f"The {self.name} is rolling over and is {self.age} years old")
    

