class Books:
    page_material = "Бумага"
    has_text = True

    def __init__(self, title, author, page_count, isbn, is_reserved=False):
        self.title = title
        self.author = author
        self.page_count = page_count
        self.isbn = isbn  # ISBN
        self.is_reserved = is_reserved


school_book = Books("Война и мир", "Толстой", 100, "13: 978-2-266-11156-0", True)
school_book_2 = Books("Мертвые души", "Гоголь", 50, "13: 978-2-266-11156-1")
school_book_3 = Books("Мцирии", "Лермонтов", 130, "13: 978-2-266-11156-2")
school_book_4 = Books("Собачье сердце", "Булгаков", 100, "13: 978-2-266-11156-3")
school_book_5 = Books("Каштанка", "Чехов", 95, "13: 978-2-266-11156-5")

print(f"Название: {school_book.title}, Автор: {school_book.author}, страниц: {school_book.page_count}, "
      f"материал: {school_book.page_material}{', зарезервирована' if school_book.is_reserved else ''}")
print(f"Название: {school_book_2.title}, Автор: {school_book_2.author}, страниц: {school_book_2.page_count}, "
      f"материал: {school_book_2.page_material}{', зарезервирована' if school_book_2.is_reserved else ''}")
print(f"Название: {school_book_3.title}, Автор: {school_book_3.author}, страниц: {school_book_3.page_count}, "
      f"материал: {school_book_3.page_material}{', зарезервирована' if school_book_3.is_reserved else ''}")
print(f"Название: {school_book_4.title}, Автор: {school_book_4.author}, страниц: {school_book_4.page_count}, "
      f"материал: {school_book_4.page_material}{', зарезервирована' if school_book_4.is_reserved else ''}")
print(f"Название: {school_book_5.title}, Автор: {school_book_5.author}, страниц: {school_book_5.page_count}, "
      f"материал: {school_book_5.page_material}{', зарезервирована' if school_book_5.is_reserved else ''}")


class SchoolBook(Books):
    def __init__(self, title, author, page_count, isbn, subject, class_room, is_reserved=False, has_exercises=False):
        super().__init__(title, author, page_count, isbn, is_reserved)
        self.subject = subject
        self.class_room = class_room
        self.has_exercises = has_exercises


# Так вроде более читабельно
school_book_6 = SchoolBook(
    title="Алгебра",
    author="Иванов",
    page_count=200,
    isbn="13: 978-2-266-11156-6",
    subject="Математика",
    class_room=9
)

school_book_7 = SchoolBook(
    title="История государства",
    author="Карамзин",
    page_count=300,
    isbn="13: 978-2-266-11156-7",
    subject="История",
    class_room=10
)

school_book_8 = SchoolBook(
    title="География",
    author="Пржевальский",
    page_count=430,
    isbn="13: 978-2-266-11156-8",
    subject="Записки о путешествиях",
    class_room=9
)
print(f"Название: {school_book_6.title}, Автор: {school_book_6.author}, страниц: {school_book_6.page_count}, "
      f"материал: {school_book_6.page_material}, "
      f"предмет: {school_book_6.subject}, класс: {school_book_6.class_room}"
      f"{', зарезервирована' if school_book_6.is_reserved else ''}")

print(f"Название: {school_book_7.title}, Автор: {school_book_7.author}, страниц: {school_book_7.page_count}, "
      f"материал: {school_book_7.page_material}, "
      f"предмет: {school_book_7.subject}, класс: {school_book_7.class_room}"
      f"{', зарезервирована' if school_book_7.is_reserved else ''}")

print(f"Название: {school_book_8.title}, Автор: {school_book_8.author}, страниц: {school_book_8.page_count}, "
      f"материал: {school_book_8.page_material}, "
      f"предмет: {school_book_8.subject}, класс: {school_book_8.class_room}"
      f"{', зарезервирована' if school_book_8.is_reserved else ''}")

# Помечаю, учебник Алгебры зарезервированым
school_book_6.is_reserved = True

print(f"Название: {school_book_6.title}, Автор: {school_book_6.author}, страниц: {school_book_6.page_count}, "
      f"материал: {school_book_6.page_material}, "
      f"предмет: {school_book_6.subject}, класс: {school_book_6.class_room}"
      f"{', зарезервирована' if school_book_6.is_reserved else ''}")
