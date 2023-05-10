#This function creates an Equipment object with specified attributes and returns it
class Equipment:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"Name: {self.name}, Description: {self.description}"
