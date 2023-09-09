class Person: 
    attributes = "sining"
    name = "jana"
    age = 17

    def is_adult(self):
     if self.age >18:
        print("you have too much responsibilites")
     else:
        print("lucky")

    

first_person = Person()
print(first_person.name)
print(first_person.age)


first_person.is_adult()

def __init__ (self,name,age):
     self.name = name
     self.age = age
class Person: 
    def __init__ (self,name,age):
     self.name = name
     self.age = age

    def adult(self):
       print(f"my name is{self.name} and i am {self.age}years")

