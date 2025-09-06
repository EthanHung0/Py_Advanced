from Classes import Gun, Tank, Airstrike, Equipment, OutOfAmmoError


class Arsenal:
    def __init__(self):
        self._arsenal = {"Guns":[], "Tanks":[], "Airtrikes":[]}


    def addArsenal(self, equipment:Equipment):
        if isinstance(equipment,Gun):
            self._arsenal["Guns"].append(equipment)
        elif isinstance(equipment,Tank):
            self._arsenal["Tanks"].append(equipment)
        elif isinstance(equipment,Airstrike):
            self._arsenal["Airstrikes"].append(equipment)


    def Present(self,equipment_type) -> bool:
        if equipment_type == "all":
            for unit_name,equipment in self._arsenal.items():
                print(f"\n========== {unit_name} ==========")
                if equipment:
                    for i,a in enumerate(equipment,1):
                        print(f"{i}. {a.display_info()}")
                else:
                    print("There are no available equipments in that category.")
        else:
            print(f"\n========== {equipment_type} ==========")
            if self._arsenal[f"{equipment_type}"]:
                for i,a in enumerate(self._arsenal[f"{equipment_type}"]):
                    print(f"{i}. {a.display_info()}")
            else:
                print("There are no available equipments in that category.")
                return False
        print()


    def useOne(self):
        equipment_type = input("Input type of available equipments (Gun/Tank/Airstrike): ").capitalize()
        if equipment_type not in ["Gun", "Tank", "Airstrike"]:
            raise ValueError(f"Equipment type <{equipment_type}> not available.")

        if not self.Present(equipment_type):
            return

        unit = self._arsenal[f"{equipment_type}"]
        try:
            choice = int(input(f"Choose an equipment 1-{len(unit)}: "))
        except ValueError:
            raise ValueError("Index must be an <int> value.")
        if choice not in range(1,len(unit)+1):
            raise ValueError("Equipment not found.")

        equipment = unit[choice+1]
        if isinstance(equipment,Gun) or isinstance(equipment,Airstrike):
            amount = input("Input amount of firing rounds (bullets): " if isinstance(equipment,Gun) else "Input amount of firing load (missles): ")
        equipment.use(amount)
