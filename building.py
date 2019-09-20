import datetime
# Practice: Urban Planner
class Building:

    def __init__(self, address, stories):
        self.designer = "Me"
        self.date_constructed = ""
        self.owner = ""
        self.address = address
        self.stories = stories

    def construct(self):
        self.date_constructed = datetime.datetime.now()

    def purchase(self, buyer):
        self.owner = buyer

    def __str__(self):
        return f"{self.address} was purchased by {self.owner} on {self.date_constructed} and has {self.stories} stories."

