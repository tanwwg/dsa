from datetime import datetime

def display_records():
    print("Records:")

def input_name():
    while True:
        print("Please enter your name")
        name = input()
        if name == "":
            continue
        if len(name) < 3:
            print("Name must be at least 3 characters")
            continue
        if len(name) > 20:
            print("Name must be less than 20 characters")
            continue
        return name

def add_employee():
    print("Add employee")
    name = input_name()
    print(f"Add employee {name}")

def print_blue(s):
    print(f"\033[94m{s}\033[0m")

def log(s):
    with open("output.txt", "a") as file:
        print(datetime.now(), file=file)
        print(s, file=file)

import csv

def write_csv():
    data = [
        ["Name", "Age", "City"],
        ["Alice", 30, "New York"],
        ["Bob", 25, "Los Angeles"],
        ["Charlie", 35, "Chicago"]
    ]
    with open("output.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)

def main_menu():
    while True:
        print_blue("hello world")
        print("1) Display all employee records")
        print("2) Add a new employee record")
        option = input()
        if option == '1':
            display_records()
        elif option == '2':
            add_employee()
        else:
            print('Invalid option')

write_csv()
log("App Start")
main_menu()