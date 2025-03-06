class Employee:
    a=1 #Class Attribute
    @classmethod
    def show(cls):
        print(f"The Value of a is {cls.a}")

e = Employee()
e.a = 45 # Instance Attribute
e.show()

# By using Class Methods, It will print and use the class attribute instead of Instance Attribute

