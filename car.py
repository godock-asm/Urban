class Car:
    def __init__(self, model, year, engine_volume, price, mileage):
        self.model = model
        self.year = year
        self.engine_volume = engine_volume
        self.price = price
        self.mileage = mileage
        self.wheels = 4  # Атрибут по умолчанию для класса Car

    def description(self):
        return (f"Модель: {self.model}, Год выпуска: {self.year}, Объем двигателя: {self.engine_volume} л, " 
                f"Цена: {self.price} рублей, Пробег: {self.mileage} км, Количество колес: {self.wheels}")


# Создание экземпляра класса Car
car = Car("Skoda Octavia", 2019, 1.4, 2150000, 130000)
print("Информация о легковом автомобиле:")
print(car.description())


# Наследник класса Car - Грузовик
class Truck(Car):
    def __init__(self, model, year, engine_volume, price, mileage):
        super().__init__(model, year, engine_volume, price, mileage)
        self.wheels = 8  # У грузовика больше колес

# Создание экземпляра класса Truck
truck = Truck("MAN TGS", 2020, 10.4, 10950000, 425000)
print("\nИнформация о грузовике:")
print(truck.description())