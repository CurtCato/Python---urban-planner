from building import Building
from city import City

megalopolis = City("Nashville", "Mayor", "1892")


waffle_house = Building("2020 Murfreesboro Pk", 1)
amazon = Building("Downtown", 24)
new_school = Building("300 Plus Park", 5)
old_school = Building("500 Interstate Blvd", 4)
pre_school = Building("123 Sesame St", 2)

waffle_house.construct()
amazon.construct()
new_school.construct()
old_school.construct()
pre_school.construct()

waffle_house.purchase("IHOP")
amazon.purchase("Dr Phil")
new_school.purchase("John Wark")
old_school.purchase("MLS")
pre_school.purchase("Barney")

megalopolis.buildings.append(waffle_house)
megalopolis.buildings.append(amazon)
megalopolis.buildings.append(new_school)
megalopolis.buildings.append(old_school)
megalopolis.buildings.append(pre_school)

for buildings in megalopolis.buildings:
    print(buildings)