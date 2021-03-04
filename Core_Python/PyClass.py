class Human:

    def __init__(self, z):
        self.address = z

    def print_address(self):
        print(self.address)
        

class Student(Human):
    
    def __init__(self, x, y, z):
        Human.__init__(self, z)
        self.name = x
        self.roll = y
    
    def print_name(self):
        print(self.name)
    
    def print_roll(self):
        print(self.roll)



obj = Student("Kuntal", 10, "Kolkata")
print(type(obj))
obj.print_name()
obj.print_roll()
obj.print_address()
