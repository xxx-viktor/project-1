class Transport(object):
    name = 'Renaul Logan'
    max_speed = 180
    mileage = 12

    def __init__(self, n, mx, mil):
        self.name = n
        self.max_speed = mx
        self.mileage = mil


class Autobus(Transport):
    capacity = 50

    def seating_capacity(self):
        return f"Вместимость одного автобуса {self.name} {Autobus.capacity} пассажиров"


Renal = Autobus('Renaul Logan', 180, 12)
print(Renal.seating_capacity())

