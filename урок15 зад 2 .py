class Transport(object):
    name = 'Renaul Logan'
    max_speed = 180
    mileage = 12
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return (f"Вместимость одного автобуса {self.name} {capacity} пассажиров")
Autobus = Transport('Renaul Logan',180,12)
print(Autobus.seating_capacity(50))
