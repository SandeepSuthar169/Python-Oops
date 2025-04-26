class employee:  # initiale class
    # dunder method/ constructor 
    def __init__(self):
        print("started executing attributes or data")
        self.id = 123
        self.salary = 5000000 
        self.designation = "s_MLops_E"
        print("attributed  or data have been initiated")


    def travel(self, destination):
        print("This travel method was called manually ")
        print(f"Employee is now tracelling it {destination}")




sam = employee() #obj / instance of the class
#print(sam.id, sam.salary)
#sam.travel('vadodra')     # calling method
#sam.travel("jalor")

print(type(sam))


