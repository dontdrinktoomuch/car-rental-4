import os

class Car:
    def __init__(self, brand, model, year, color, plate_number, price,):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.plate_number = plate_number
        self.price = price
        self.available = True

    def rent(self):
        self.available = False

    def return_car(self):
        self.available = True

# Predefined admin credentials
admin_username = "admin"
admin_password = "admin123"

# Initialize users dictionary with admin user
users = {admin_username: admin_password}

# Initialize empty list of cars
cars = []

def create_user():
    username = input("Enter your username: ")
    if username.lower() == 'exit':
        return None

    if username not in users:
        password = input("Enter your password: ")
        users[username] = password
        print("User created successfully!")
    else:
        print("Username already exists. Please choose a different username.")

def authenticate_user():
    while True:
        username = input("Enter your username: ")

        if username.lower() == 'exit':
            return None

        if username in users:
            password = input("Enter your password: ")
            if password == users[username]:
                print(f"Welcome, {username}!")
                return username
            else:
                print("Incorrect password. Please try again.")
        else:
            print("User not found. Please try again.")

def add_car():
    brand = input("Enter car brand: ")
    model = input("Enter car model: ")
    year = input("Enter car year: ")
    color = input("Enter car color: ")
    plate_number = input("Enter Car Plate Number: ")
    price = input("Enter Car Price: ")
    new_car = Car(brand, model, year, color, plate_number, price,)
    cars.append(new_car)
    print("Car added successfully!")

def delete_car():
    print("Available Cars:")
    for i, car in enumerate(cars):
        if car.available:
            print(f"{i + 1}. {car.brand} {car.model} ({car.year}), Color: {car.color}, {car.plate_number} ({car.price})")

    car_index = int(input("Enter the index of the car you want to delete: ")) - 1
    if 0 <= car_index < len(cars):
        del cars[car_index]
        print("Car deleted successfully!")
    else:
        print("Invalid car index.")

def rent_car(user):
    print("Available Cars:")
    for i, car in enumerate(cars):
        if car.available:
            print(f"{i + 1}. {car.brand}, {car.model}, ({car.year}), Color: {car.color}, Plate Number: {car.plate_number}, {car.price}")

    car_index = int(input("Enter the index of the car you want to rent: ")) - 1
    if 0 <= car_index < len(cars):
        chosen_car = cars[car_index]
        chosen_car.rent()
        print(f"You have rented the {chosen_car.brand} {chosen_car.model} {chosen_car.plate_number} {chosen_car.price}. Enjoy your ride!")
    else:
        print("Invalid car index.")

def return_car(user):
    print("Your Rented Cars:")
    rented_cars = [car for car in cars if not car.available]
    if rented_cars:
        for i, car in enumerate(rented_cars):
            print(f"{i + 1}. {car.brand}, {car.model}, ({car.year}), Color: {car.color}, Plate Number: {car.plate_number}, Price:: {car.price}")

        car_index = int(input("Enter the index of the car you want to return: ")) - 1
        if 0 <= car_index < len(rented_cars):
            chosen_car = rented_cars[car_index]
            chosen_car.return_car()
            print(f"You have returned the {chosen_car.brand} {chosen_car.model} {chosen_car.plate_number} {chosen_car.price}. Thank you!")
        else:
            print("Invalid car index.")
    else:
        print("You have no rented cars.")

def admin_login():
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")
    if username == admin_username and password == admin_password:
        return True
    else:
        print("Invalid admin credentials.")
        return False

def main():
    while True:
        # os.system('cls' if os.name == 'nt' else 'clear')
        print("\n----- Car Rental System -----")
        print("1. Sign Up")
        print("2. Sign In")
        print("3. Admin Login")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("Sign Up")
            create_user()
        elif choice == '2':
            print("Sign In")
            username = authenticate_user()
            if username:
                user_choice(username)
        elif choice == '3':
            print("Admin Login")
            if admin_login():
                admin_choice()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

def user_choice(username):
    while True:
        # os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\n----- Welcome, {username} -----")
        print("1. Rent a Car")
        print("2. Return a Car")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("Rent a Car")
            rent_car(username)
        elif choice == '2':
            print("Return a Car")
            return_car(username)
        elif choice == '3':
            print("Exiting to main menu.")
            break
        else:
            print("Invalid choice. Please try again.")

def admin_choice():
    while True:
        # os.system('cls' if os.name == 'nt' else 'clear')
        print("\n----- Admin Panel -----")
        print("1. Add Car")
        print("2. Delete Car")
        print("3. Exit to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("Add Car")
            add_car()
        elif choice == '2':
            print("Delete Car")
            delete_car()
        elif choice == '3':
            print("Exiting to main menu.")
            break
        else:
            print("Invalid choice. Please try again.")


main()