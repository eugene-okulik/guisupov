class Flower:
    """ Общий класс для всех цветов"""

    def __init__(self, name, color, fresh_ness, stem_length, price):
        self.name = name  # Название цветка
        self.color = color  # Цвет цветка
        self.fresh_ness = fresh_ness  # Свежесть, с момента, как срезан
        self.stem_length = stem_length  # Длина стебля
        self.price = price  # Цена цветка

    def __repr__(self):
        return f"{self.name}: {self.color}, {self.stem_length} см, {self.price} Руб"


class Rose(Flower):
    """Класс для роз"""

    def __init__(self, color, fresh_ness, stem_length, price):
        super().__init__("Rose", color, fresh_ness, stem_length, price)


class Astra(Flower):
    """Класс для астр"""

    def __init__(self, color, fresh_ness, stem_lenght, price):
        super().__init__("Astra", color, fresh_ness, stem_lenght, price)


class Daisy(Flower):
    """Класс для ромашек"""

    def __init__(self, color, fresh_ness, stem_length, price):
        super().__init__("Daisy", color, fresh_ness, stem_length, price)


class Tulip(Flower):
    """Класс для тюльпанов"""

    def __init__(self, color, fresh_ness, stem_length, price):
        super().__init__("Tulip", color, fresh_ness, stem_length, price)


class Bouquet:
    """Класс для букета цветов."""

    def __init__(self):
        self.flowers = []  # Список цветов в букете

    def add_flower(self, flower):
        """Метод для добавления цветка в букет."""
        self.flowers.append(flower)

    def cost_calculate(self):
        """Метод для расчета общей стоимости букета."""
        return sum(flower.price for flower in self.flowers)

    def wilting_time_calculate(self):
        """Метод для определения среднего времени увядания в букете"""
        if not self.flowers:
            return 0
        return sum(flower.fresh_ness for flower in self.flowers) / len(self.flowers)

    def sorted_flowers(self, key):
        """ Метод для сортировки цветов в букете по указанному параметру"""
        self.flowers.sort(key=lambda flower: getattr(flower, key))

    def find_flowers(self, **criteria):
        """Метод для поиска цветов в  букете по заданным критериям, и выводу на печать"""
        results = self.flowers
        for key, value in criteria.items():
            results = [flower for flower in results if getattr(flower, key) == value]
        criteria_str = ", ".join(f"{k} = {v}" for k, v in criteria.items())
        if results:
            print(f"По критериям {criteria_str} найдены цветы: {', '.join(map(str, results))}")
        else:
            print(f"Нет цветов, подходящих по критериям {criteria_str}.")

    def __repr__(self):
        return ", ".join(map(str, self.flowers))


# Создаю цветы
rose1 = Rose(color="Red", stem_length=50, fresh_ness=2, price=150)
rose2 = Rose(color="White", stem_length=40, fresh_ness=1, price=130)
tulip1 = Tulip(color="Yellow", stem_length=30, fresh_ness=3, price=100)
daisy1 = Daisy(color="White", stem_length=25, fresh_ness=4, price=80)
astra1 = Astra(color="Orange", stem_lenght=35, fresh_ness=5, price=95)

# Создаю букет
bouquet = Bouquet()
bouquet.add_flower(rose1)
bouquet.add_flower(rose2)
bouquet.add_flower(tulip1)
bouquet.add_flower(daisy1)
bouquet.add_flower(astra1)

# Вывожу созданный букет
print(f"Букет: {bouquet}\n")

# Вывожу общую стоимость букета
print(f"Общая стоимость букета: {bouquet.cost_calculate()} Руб\n")

# Расчитываю среднее время увядания букета
print(f"Среднее время увядания букета: {bouquet.wilting_time_calculate()} дней\n")

# Сортируем цветы  в букете по свежести
bouquet.sorted_flowers(key="fresh_ness")
print(f"Букет отсортированый по свежести:, {bouquet}\n")

bouquet.sorted_flowers(key="color")
print(f"Букет отсортированый по цвету:, {bouquet}\n")

bouquet.sorted_flowers(key="stem_length")
print(f"Букет отсортированый по длине стебля:, {bouquet}\n")

bouquet.sorted_flowers(key="price")
print(f"Букет отсортированый по цене:, {bouquet}\n")

# Ищу цветы по критерию (можно указать: price = 100, stem_length = 40, name = "Rose" )
bouquet.find_flowers(color="White")
