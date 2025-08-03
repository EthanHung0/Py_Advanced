import time

class Shift:
    def __init__(self, day, time_of_day):
        self.day = day
        self.time_of_day = time_of_day

    def __str__(self):
        return f"{self.day} - {self.time_of_day}"


class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.shifts = []

    def assign_shift(self, shift):
        self.shifts.append(shift)

    def get_schedule(self):
        return [str(shift) for shift in self.shifts]

    def __str__(self):
        return f"{self.name} ({self.role})"


class Store:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def list_employees(self):
        info = "\nAvailable Employees:\n"
        for i, emp in enumerate(self.employees, 1):
            info += f"{i}. {emp.name} ({emp.role})\n"
        return info

    def find_employee(self, name):
        for emp in self.employees:
            if emp.name.lower() == name.lower():
                return emp
        return None

    def assign_shift_to(self, employee_name, shift):
        emp = self.find_employee(employee_name)
        if emp:
            emp.assign_shift(shift)
            print(f"> Assigned {emp.name} to {shift}")
            time.sleep(0.5)
        else:
            print("> Employee not found.")
            time.sleep(0.5)

    def show_schedule(self):
        print("\n--- WORK SCHEDULE ---")
        for emp in self.employees:
            for shift in emp.shifts:
                print(f"{emp.name}: {shift}")
        print()
        input("> ")
