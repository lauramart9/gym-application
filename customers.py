
#This function creates a Customer object with specified attributes and returns it.
class Customers:
    def __init__(self, name, age, gender, email, password):
        self.name = name
        self.age = age
        self.gender = gender
        self.email = email
        self.password = password

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Email: {self.email}"
