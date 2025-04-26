# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         print(f"{self.name} make a sound")    


# class Dog(Animal):
#   #  def __init__(self):
#    #     self.behaviour = "friendly"
#     def speak(self):
#         print(f"{self.name} barks... and he is very ")         

# animal = Animal("generic animal")
# animal.speak()       

# dog = Dog("buddy")
# dog.speak()




# super
class Animal:
    def __init__(self):
        self.name = "Buddy"

    def speak(self):
        print(f"{self.name} make a sound.") 

class Dog(Animal):
    def __init__(self, breed):
        super().__init__()         
        self.breed = breed

    def speak(self):
        super().speak()
        print(f"{self.name} barks. it is a {self.breed}") 


dog = Dog('germen chapad') 
dog.speak()