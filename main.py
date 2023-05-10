#importing  modules that contain classes and functions  used in the program

from customers import Customers
from trainers import Trainers
from equipments import Equipment
from exercise_plans import ExercisePlan
from subscriptions import Subscription
#importing module to interact with the operating system for  reading and writing files.
import os

#defining empty lists to store data fore GMS
def read_data():
    customers = []
    trainers = []
    equipments = []
    exercise_plans = []
    subscriptions = []

# reading customers.txt file and creating  instances of class Customers

    with open("customers.txt", "r") as file:
# iterating over each line in th file, and  removing any  whitespace
# splitting the line into a list values by comma
        for line in file:
            data = line.strip().split(",")
            customer = Customers(data[0], int(data[1]), data[2], data[3], data[4])
            #appending new `Customers` object  to the `customers` list
            customers.append(customer)

# Reading trainers.txt file and creating instances of class Trainers
    with open("trainers.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            trainer = Trainers(data[0], int(data[1]), data[2], data[3], data[4])
            trainers.append(trainer)

# Reading equipments.txt file and creating instances of Equipment class
    with open("equipments.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            equipment = Equipment(data[0], data[1])
            equipments.append(equipment)

# # Reading exercisePlans.txt file and creating instances of class ExercisePlan

# Iterating over each `Trainers` object in `trainers` list,  checking if its name matches the firs value in data list.
# If found a match, assigning Trainers object to 'trainer'  exiting the loop

    with open("exercisePlans.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            trainer = None
            for t in trainers:
                if t.name == data[0]:
                    trainer = t
                    break
            equipment = None
            for e in equipments:
                if e.name == data[1]:
                    equipment = e
                    break
            exercise_plan = ExercisePlan(trainer, equipment, int(data[2]))
            exercise_plans.append(exercise_plan)

# Reading subscriptions.txt file and creating instances of  class Subscription
    with open("subscriptions.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            customer = None
            for c in customers:
                if c.name == data[0]:
                    customer = c
                    break
            trainer = None
            for t in trainers:
                if t.name == data[1]:
                    trainer = t
                    break
            exercise_plan = None
            for e in exercise_plans:
                if e.trainer == trainer and e.equipment.name == data[2]:
                    exercise_plan = e
                    break
            subscription = Subscription(customer, trainer, exercise_plan, data[3], data[4])
            subscriptions.append(subscription)

    return customers, trainers, equipments, exercise_plans, subscriptions
 # Writing customers  data to customers.txt file
def add_customer(customers):
    with open("customers.txt", "w") as file:
        for customer in customers:
            file.write(f"{customer.name},{customer.age},{customer.gender},{customer.email},{customer.password}\n")\

def del_customer(name):
    with open("customers.txt", "r") as file:
        lines = file.readlines()
    with open("customers.txt", "w") as file:
        for line in lines:
            if not line.startswith(name):
                file.write(line)
    print(f"{name} has been deleted from customers")


def add_trainer(trainers):
 # Writing trainers data to trainers.txt file
    with open("trainers.txt", "w") as file:
        for trainer in trainers:
            file.write(f"{trainer.name},{trainer.age},{trainer.gender},{trainer.email},{trainer.password}\n")

def del_trainer(name):
    with open("trainers.txt", "r") as file:
        lines = file.readlines()
    with open("trainers.txt", "w") as file:
        for line in lines:
            if not line.startswith(name):
                file.write(line)
    print(f"{name} has been deleted from trainers")

def add_equipments(equipments):
# Writing equipments data to equipments.txt file
    with open("equipments.txt", "w") as file:
        for equipment in equipments:
            file.write(f"{equipment.name},{equipment.description}\n")

def del_equipments(name):
    with open("equipments.txt", "r") as file:
        lines = file.readlines()
    with open("equipments.txt", "w") as file:
        for line in lines:
            if not line.startswith(name):
                file.write(line)
    print(f"{name} has been deleted from equipments")

def add_exercisePlans(exercisePlans):
# Writing exercise plans data to exercisePlans.txt file
    with open("exercisePlans.txt", "w") as file:
        for exercise_plan in exercisePlans:
            file.write(f"{exercise_plan.trainer},{exercise_plan.equipment},{exercise_plan.duration}\n")

def del_exercisePlans(name):
    with open("exercisePlans.txt", "r") as file:
        lines = file.readlines()
    with open("exercisePlans.txt", "w") as file:
        for line in lines:
            if not line.startswith(name):
                file.write(line)
    print(f"{name} has been deleted from exercisePlans")

#Deleting  an existing `subscription` object from the `subscriptions` list
def add_subscriptions(subscriptions):
# Writing subscriptions data to subscriptions.txt file
    with open("subscriptions.txt", "w") as file:
        for subscription in subscriptions:
            file.write(f"{subscription.customer.name},{subscription.trainer.name},{subscription.exercise_plan.equipment.name},{subscription.start_date},{subscription.end_date}\n")

def del_subscriptions(name):
    with open("subscriptions.txt", "r") as file:
        lines = file.readlines()
    with open("subscriptions.txt", "w") as file:
        for line in lines:
            if not line.startswith(name):
                file.write(line)
    print(f"{name} has been deleted from subscriptions")

# Defining main function of the program
# Calling the `read_data` function and assigning the returned values to the variables 'customers', 'trainers' etc

def main():
    customers, trainers, equipments, exercise_plans, subscriptions = read_data()
# Using a loop to display a menu of options to the user.

    while True:
        print("1. Add Customer")
        print("2. Add Trainer")
        print("3. Add Equipment")
        print("4. Add Exercise Plan")
        print("5. Add Subscription")
        print("6. View Customers")
        print("7. View Trainers")
        print("8. View Equipments")
        print("9. View Exercise Plans")
        print("10. View Subscriptions")
        print("11. Exit")
        print("12. Delete Customer")
        print("13. Delete Trainer")
        print("14. Delete Equipment")
        print("15. Delete Exercise plan")
        print("16. Delete subscription")

 # Prompting user to enter their choice and using `int()` function converting input to
# integer and assign it to the variable `choice`

        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            gender = input("Enter gender: ")
            email = input("Enter email: ")
            password = input("Enter password: ")
            customer = Customers(name, age, gender, email, password)
            customers.append(customer)
            add_customer(customers)
            print("Customer added successfully!")

        elif choice == 2:
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            gender = input("Entergender: ")
            email = input("Enter email: ")
            password = input("Enter password: ")
            trainer = Trainers(name, age, gender, email, password)
            trainers.append(trainer)
            add_trainer(trainers)
            print("Trainer added successfully!")

        elif choice == 3:
            name = input("Enter name: ")
            description = input("Enter description: ")
            equipment = Equipment(name, description)
            equipments.append(equipment)
            add_equipments(equipments)
            print("Equipment added successfully!")

        elif choice == 4:
            trainer_name = input("Enter trainer name: ")
            equipment_name = input("Enter equipment name: ")
            duration = int(input("Enter duration: "))
            trainer = None
            for t in trainers:
                if t.name == trainer_name:
                    trainer = t
                    break
            equipment = None
            for e in equipments:
                if e.name == equipment_name:
                    equipment = e
                    break
            exercise_plan = ExercisePlan(trainer.name, equipment.name, duration)
            exercise_plans.append(exercise_plan)
            add_exercisePlans(exercise_plans)
            print("Exercise plan added successfully!")

        elif choice == 5:
            customer_name = input("Enter customer name: ")
            trainer_name = input("Enter trainer name: ")
            equipment_name = input("Enter equipment name: ")
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            customer = None
            for c in customers:
                if c.name == customer_name:
                    customer = c
                    break
            trainer = None
            for t in trainers:
                if t.name == trainer_name:
                    trainer = t
                    break
            exercise_plan = None
            for e in exercise_plans:
                if e.trainer == trainer and e.equipment.name == equipment_name:
                    exercise_plan = e
                    break
            subscription = Subscription(customer, trainer, exercise_plan, start_date, end_date)
            subscriptions.append(subscription)
            add_subscriptions(subscriptions)
            print("Subscription added successfully!")

        elif choice == 6:
            print("Customers:")
            for customer in customers:
                print(customer)

        elif choice == 7:
            print("Trainers:")
            for trainer in trainers:
                print(trainer)

        elif choice == 8:
            print("Equipments:")
            for equipment in equipments:
                print(equipment)

        elif choice == 9:
            print("Exercise Plans:")
            for exercise_plan in exercise_plans:
                print(exercise_plan)

        elif choice == 10:
            print("Subscriptions:")
            for subscription in subscriptions:
                print(subscription)

        elif choice == 11:
            break

        elif choice == 12:
            customer_name = input("Enter name of customer to delete: ")
            del_customer(customer_name)

        elif choice == 13:
            trainer_name = input("Enter name of trainer to delete: ")
            del_trainer(trainer_name)
#handling unexpected input by printing error message when deleting equipment
        elif choice == 14:
            equipment_name = input("Enter name of equipment to delete: ")
            for equipment in equipments:
                if equipment.name != equipment_name:
                    # raise ValueError(f"Invalid equipment name: {equipment_name}")
                    print(f"Invalid equipment name: {equipment_name}, Try again")
            else:
                del_equipments(equipment_name)

        elif choice == 15:
            exercise_plan_name = input("Enter name of exercise plan to delete: ")
            del_customer(exercise_plan_name)

        elif choice == 16:
            subscription_name = input("Enter subscription to delete: ")
            del_customer(subscription_name)

        else:
            print("Invalid choice. Please try again.")

main()



