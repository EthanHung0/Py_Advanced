from Classes import FullTimeEmployee,PartTimeEmployee,Freelancer

tlist = [FullTimeEmployee("Aaron","001"),PartTimeEmployee("Anora","002"),Freelancer("Ethan","003")]
for i in tlist:
    print(i.calculate_salary(3))