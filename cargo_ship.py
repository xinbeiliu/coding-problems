class CargoShip:
    def __init__(self, capacity):
        self.cargo = []
        self.capacity = capacity

    def unload(self, port):
        """
        :param port: (String)
        :returns: [(String, Int)]
        """
        for item in self.cargo:
            if port in item:
                return item
            return []

    def can_depart(self):
        """
        :returns: (Bool)
        """
        # return True if sum of all weights in cargo is less than or equal to the capacity
        # and False if not
        total_weight = 0

        for i in range(len(self.cargo)):
            total_weight += self.cargo[i][1]
        if total_weight <= self.capacity:
            return True

        return False

    def load(self, new_cargo):
        """
        :param new_cargo: [(String, Int)]
        """
        # add new cargo

        for item in new_cargo:
            self.cargo.append(item)
        return self.cargo


ship = CargoShip(10)
print(ship.load([("New York", 1), ("London", 20)]))
print(ship.unload("New York"))  # should print [("New York", 1)]
print(ship.unload("Los Angeles")) # should return empty list
print(ship.can_depart())  # should print False