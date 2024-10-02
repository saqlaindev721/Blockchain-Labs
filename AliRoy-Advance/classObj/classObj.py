class Person:
    name = "Haider"
    occupation = "Software Developer "
    networth = 22
    
    def info(self):
        print(f"{self.name} is a {self.occupation}")
    
a = Person()
    a.name = "ali"
    a.occupation = "Accountant"
    print(a.name, a.occupation)