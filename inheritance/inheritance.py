class Parent():
    """ This is a parent class to learn how to use inheritance of classes"""

    def __init__(self, last_name, eye_color):
        print("Parent Contructor Called")
        self.last_name = last_name
        self.eye_color = eye_color
    
    def show_info(self):
        print("Last Name: " + self.last_name)
        print("Eye Color: " + self.eye_color)

class Child(Parent):
    """ This is a child class"""

    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child Contructor Called")
        super().__init__(last_name, eye_color)
        self.number_of_toys = number_of_toys
    
    def show_info(self):
        print("Child Last Name: " + self.last_name)
        print("Child Eye Color: " + self.eye_color)
        print("Child Number of Toys: " + str(self.number_of_toys))

print(Parent.__doc__)
print(Parent.__name__)
print(Parent.__module__)

billy_cyrus = Parent("Cyrus", "blue")
print(billy_cyrus.last_name)

billy_cyrus.show_info()

miley_cyrus = Child("Cyrus", "Blue", 3)
print(miley_cyrus.last_name)
print(miley_cyrus.number_of_toys)

miley_cyrus.show_info()