from Classes import Car,Bike,Boat

tlist = [Car(),Bike(),Boat()]
for i in tlist:
    print(i.run())
    print(i.start_engine())