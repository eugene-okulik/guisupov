class Books:
    page_material = "Бумага"
    has_text = True

    def __init__(self, title, author, page_count, isbn, is_reserved=False):
        self.title = title
        self.author = author
        self.page_count = page_count
        self.isbn = isbn  # ISBN
        self.is_reserved = is_reserved

    def get_description(self):
        return (f"Название: {self.title}, Автор: {self.author}, страниц: {self.page_count}, "
                f"материал: {self.page_material}{', зарезервирована' if self.is_reserved else ''}")


class SchoolBook(Books):
    def __init__(self, title, author, page_count, isbn, subject, class_room, is_reserved=False, has_exercises=False):
        super().__init__(title, author, page_count, isbn, is_reserved)
        self.subject = subject
        self.class_room = class_room
        self.has_exercises = has_exercises

    def get_description(self):
        base_description = super().get_description()
        return (
            base_description
            + f", предмет: {self.subject}, класс: {self.class_room}")


school_book_1 = Books("Война и мир", "Толстой", 100, "13: 978-2-266-1115-0", True)
school_book_2 = Books("Мертвые души", "Гоголь", 50, "13: 978-2-266-11156-1")
school_book_3 = Books("Мцирии", "Лермонтов", 130, "13: 978-2-266-11156-2")
school_book_4 = Books("Собачье сердце", "Булгаков", 100, "13: 978-2-266-11156-3")
school_book_5 = Books("Каштанка", "Чехов", 95, "13: 978-2-266-11156-5")

school_book_6 = SchoolBook(title="Алгебра", author="Иванов", page_count=200,
                           isbn="13: 978-2-266-11156-6", subject="Математика", class_room=9)

school_book_7 = SchoolBook(title="История государства", author="Карамзин", page_count=300,
                           isbn="13: 978-2-266-11156-7", subject="История", class_room=10)

school_book_8 = SchoolBook(title="География", author="Пржевальский", page_count=430,
                           isbn="13: 978-2-266-11156-8", subject="Записки о путешествиях", class_room=9)

print(school_book_1.get_description())
print(school_book_2.get_description())
print(school_book_3.get_description())
print(school_book_4.get_description())
print(school_book_5.get_description())
print(school_book_6.get_description())
print(school_book_7.get_description())
