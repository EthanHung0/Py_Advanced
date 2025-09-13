from ROOMS import Standard, VIP, ConferenceRoom
from HOTEL import Main_Hotel



def main():
    main_sys = Main_Hotel()

    while True:
        print("""
|---------------------------------------------------------|
|                    Hotel Management                     |
|---------------------------------------------------------|
| 1. Add room.                                            |
| 2. Show all rooms.                                      |
| 3. Check-in.                                            |
| 4. Check-out.                                           |
| 5. Find Room (by ID).                                   |
| 6. Show all customers.                                  |
| 7. Exit                                                 |
|---------------------------------------------------------|
""")

        choice = input("Choose (1-7): ")
        if choice == "1":
            try:
                room_type = input("Input Room Type (Standard/VIP/Conference): ").lower()
                if room_type not in ["standard","vip","conference"]:
                    raise ValueError(f"Room type <{room_type}> Unavailable. (only Standard, VIP and Conference are available)")
                room_id = input("Input Room ID (5 letters and/or numbers): ").upper()
                price = input("Input room's price (integer, $)")
                if room_type == "standard":
                    main_sys.addRoom(Standard(room_id,price))
                elif room_type == "vip":
                    base = input('Input VIP room services (separate with ","): ').strip()
                    if not base:
                        raise ValueError("There must be at least one VIP service for VIP rooms.")
                    services = [service.strip() for service in base.split(",")]
                    main_sys.addRoom(VIP(room_id,price,services))
                elif room_type == "conference":
                    capacity = input("Input Conference room's capacity: ")
                    main_sys.addRoom(ConferenceRoom(room_id,price,capacity))
                else:
                    raise ValueError("Invalid Room Type.")
            except ValueError as e:
                price(f"Error while adding Room: {e}")

        elif choice == "2":
            main_sys.showRooms()
            input(">")

        elif choice == "3":
            try:
                main_sys.showRooms()
                #roomf_id:str, customer_id:str, name:str, phone_num
                roomf_id = input("Input Check-in room id (5 letters and/or numbers):").upper()
                customer_id = input("Input Customer's ID: ").upper()
                name = input("Input Customer's Name: ").title()
                phone_num = input("Input Customer's phone number (exactly 9 digits): ")
                main_sys.checkIn(roomf_id, customer_id, name, phone_num)
            except ValueError as e:
                print(f"Error during Check-in: {e}")

        elif choice == "4":
            try:
                roomf_id = input("Input Check-out room id (5 letters and/or numbers):").upper()
                main_sys.checkOut(roomf_id)
            except ValueError as e:
                print(f"Error during Check-out: {e}")

        elif choice == "5":
            try:
                main_sys.showRooms()
                input(">")
            except ValueError as e:
                print(f"Error while presenting available Rooms: {e}")

        elif choice == "6":
            try:
                main_sys.showCustomers()
            except ValueError as e:
                print(f"Error while showing Customers list: {e}")

        elif choice == "7":
            print("Shutting Down...")
            break
        else:
            print("Invalid choice (only 1-7)")



#-----------------------
main()






