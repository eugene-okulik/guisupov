import random

# Списки значений для генерации
names = ["One", "Two", "Three", "Four", "Five", "Six"]
colors = ["Red", "Blue", "Green", "Yellow", "Black", "White"]
sizes = ["small", "medium", "large", "max", "min"]


name = random.choices(names)
color = random.choices(colors)
size = random.choices(sizes)
body = {"name": "Five",
            "data": {
                "color": "Black",
                "size": "max"}
            }


