from ARSENAL import Arsenal
from Classes import Gun, Tank, Airstrike
import time



def main():
    system = Arsenal()

    while True:
        print("""
    |==== MILITARY EQUIPMENT MANAGEMENT SYSTEM ====|
    |    1. Add New Equipment                      |
    |    2. Equipment List                         |
    |    3. Use an Equipment                       |
    |    4. Exit                                   |
    |==============================================|""")

        choice = input("Make a choice (1-4): ")

        if choice == "1":
            equipment_type = input("Input available types (Gun/Tank/Airstrike): ").lower()
            name = input("Input equiment's name: ")
            weight = input("Input equipment's weight (kilograms): ")
            effective_range = input("Input equipment's effective range (meters): ")
            power = input("Input equipment's destruction power: ")

            try:
                if equipment_type == "gun":
                    ammo = input("Input firearm's current ammo (bullets): ")
                    system.addArsenal(Gun(name,weight,effective_range,power,ammo))
                elif equipment_type == "tank":
                    armor = input("Input tank's armor type: ")
                    system.addArsenal(Tank(name,weight,effective_range,power,armor))
                elif equipment_type == "airstrike":
                    payload = input("Input airstrike's current payload (missles): ")
                    system.addArsenal(Airstrike(name,weight,effective_range,power,payload))
                else: raise ValueError(f"Equipment type <{equipment_type}> not available.")

                print(f"> Added {name} to <{equipment_type}> unit.")
            except ValueError as e:
                print(f"Error while adding equpment: {e}")

        elif choice == "2":
            try:
                system.Present("all")
            except ValueError as e:
                print(f"Error while presentation: {e}")
            input(">")

        elif choice == "3":
            try:
                system.useOne()
            except ValueError as e:
                print(f"Error while using equipment: {e}")

        elif choice == "4":
            print("Shutting down...")
            time.sleep(0.5)
            break


main()






