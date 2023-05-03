class Customer:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def calculate_percentages(self):
        annual_rate = 0.005  # 0.5%
        deposit_interest = self.balance * annual_rate
        return deposit_interest
    import datetime

class Human:
    def __init__(self, name, surname, email):
        self.name = name
        self.surname = surname
        self.email = email
        self.datetime_created = datetime.datetime.now()

class Customer(Human):
    def __init__(self, name, surname, email, customer_id):
        super().__init__(name, surname, email)
        self.customer_id = customer_id

import csv

class Customer:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

def write_customers_to_csv(customers, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Email", "Phone"])
        for customer in customers:
            writer.writerow([customer.name, customer.email, customer.phone])
            
import csv

def display_customer_csv(csv_filename):
    with open(csv_filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            print(row)
            
import csv

class Customer:
    def __init__(self, name, surname, email):
        self.name = name
        self.surname = surname
        self.email = email

    def modify_customer(self):
        print("Please enter the new data for the customer:")
        self.name = input("Name: ")
        self.surname = input("Surname: ")
        self.email = input("Email: ")

        # Update the CSV file with the modified data
        customers = []
        with open('customers.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[2] == self.email:
                    row[0] = self.name
                    row[1] = self.surname
                    row[2] = self.email
                customers.append(row)

        # Write the updated data back to the CSV file
        with open('customers.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(customers)

        # Call create_customer_csv() to ensure the changes are saved
        create_customer_csv()

import random
from datetime import datetime

class Account:
    def __init__(self, creation_date):
        self.creation_date = creation_date
        self.balance = 0

    def generate_prize(self):
        if self.creation_date.month == 4 and self.creation_date.day == 1:
            prize_amount = random.randint(1, 100)
            self.balance += prize_amount
            return prize_amount
        return 0
