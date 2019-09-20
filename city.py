class City:

    def __init__(self, name, mayor, date_established):
        self.name = name
        self.mayor = mayor
        self.date_established = date_established
        self.buildings = list()

    def add_building(self, building):
        self.buildings = building