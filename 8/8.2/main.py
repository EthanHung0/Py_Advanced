from classes import Store, Employee, Shift
import time

def main():
    store = Store("ABC STORE")

    print("------------------------")
    print(f"|     {store.name}     |")
    print("------------------------")

    while True:
        print("|1. Add Employee       |")
        print("|2. Assign Shift       |")
        print("|3. Show Employee List |")
        print("|4. Show Work Schedule |")
        print("|0. Exit               |")
        print("------------------------\n")

        choice = input("> ")

        if choice == "1":
            name = input("Enter employee name: ")
            role = input("Enter employee role (cashier, stock, guard...): ")
            store.add_employee(Employee(name, role))
            print(f"> Added {name} ({role})")
            time.sleep(0.5)

        elif choice == "2":
            if not store.employees:
                print("> No employees yet.")
                time.sleep(0.5)
                continue
            print(store.list_employees())
            name = input("Enter the employee's name to assign a shift: ")
            day = input("Enter the day (e.g. Monday): ")
            time_of_day = input("Enter the shift (Morning/Afternoon/Night): ")
            store.assign_shift_to(name, Shift(day, time_of_day))

        elif choice == "3":
            print(store.list_employees())
            input("> ")

        elif choice == "4":
            store.show_schedule()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("> Invalid choice.")
            time.sleep(0.5)


main()