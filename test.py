

class Human:
    def __init__(self, name: str, age: int, work: str):
        self.name = name
        self.age = age
        self.work = work
    def __str__(self):
        return f'{self.name} возрастом {self.age} лет и работает в {self.work}'

    def working(self):
        print(f'{self.name} начал/а работу в {self.work}')

hum_1 = Human('Герман', 19, 'GB')
hum_1.working()
hum_2 = Human('Анастасия', 18, 'Яндекс')
hum_2.working()