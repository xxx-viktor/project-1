class transport(object):
    name = 'Renaul Logan'
    max_speed = 180
    mileage = 12

    def __init__(self, n, m, ml):
        self.name = n
        self.max_speed = m
        self.mileage = ml

    def scor(self):
        print(f'Название автомобиля:{self.name} Скорость:{self.max_speed} Пробег:{self.mileage}')


Autobus = transport('Renaul Logan', 180, 12)
Autobus.scor()
