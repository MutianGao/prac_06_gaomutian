class Guitar:
    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}), worth $ {self.cost}"

    def __repr__(self):
        return f"[{self.__str__()}]"