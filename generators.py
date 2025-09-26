# ===== 1. ИТЕРАТОРЫ И ГЕНЕРАТОРЫ =====

print("=== 1. ИТЕРАТОРЫ И ГЕНЕРАТОРЫ ===\n")

# 1.1 Countdown итератор
class Countdown:
    def __init__(self, n):
        self.n = n
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.n <= 0:
            raise StopIteration
        current = self.n
        self.n -= 1
        return current

print("1.1 Countdown итератор:")
for num in Countdown(5):
    print(num, end=" ")
print("\n")

# 1.2 Генератор чётных чисел
def even_numbers(limit):
    for i in range(2, limit + 1, 2):
        yield i

print("1.2 Генератор чётных чисел до 10:")
for num in even_numbers(10):
    print(num, end=" ")
print("\n")

# 1.3 Бесконечный генератор
def infinite_cycle(lst):
    while True:
        for item in lst:
            yield item

print("1.3 Бесконечный генератор (первые 7 элементов):")
cycle = infinite_cycle([1, 2, 3])
for _ in range(7):
    print(next(cycle), end=" ")
print("\n")

# ===== 2. ДЕКОРАТОРЫ И МЕТАКЛАССЫ =====

print("\n=== 2. ДЕКОРАТОРЫ И МЕТАКЛАССЫ ===\n")

# 2.1 Простой декоратор
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Вызов функции {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@logger
def hello():
    print("Привет")

print("2.1 Простой декоратор:")
hello()
print()

# 2.2 Декоратор с параметром
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def hi():
    print("Hi!")

print("2.2 Декоратор с параметром:")
hi()
print()

# 2.3 Метакласс
class AutoStr(type):
    def __new__(cls, name, bases, attrs):
        def __str__(self):
            return f"{name} {self.__dict__}"
        attrs['__str__'] = __str__
        return super().__new__(cls, name, bases, attrs)

class Person(metaclass=AutoStr):
    def __init__(self, name, age):
        self.name = name
        self.age = age

print("2.3 Метакласс:")
person = Person("Michael", 20)
print(person)
print()

# ===== 4. ПРОДВИНУТЫЕ СТРУКТУРЫ ДАННЫХ =====

print("=== 4. ПРОДВИНУТЫЕ СТРУКТУРЫ ДАННЫХ ===\n")

from collections import Counter, defaultdict
from dataclasses import dataclass

# 4.1 Counter
text = "hello world"
char_count = Counter(text)
print("4.1 Counter - подсчёт символов в 'hello world':")
print(dict(char_count))
print()

# 4.2 defaultdict
students = [("Mike", 1), ("Shauna", 2), ("Tom", 1)]
courses = defaultdict(list)

for name, course in students:
    courses[course].append(name)

print("4.2 defaultdict - группировка студентов по курсам:")
print(dict(courses))
print()

# 4.3 dataclass
@dataclass
class Book:
    title: str
    author: str
    year: int

books = [
    Book("1984", "Джордж Оруэлл", 1949),
    Book("Война и мир", "Лев Толстой", 1869),
    Book("Гарри Поттер", "Дж.К. Роулинг", 1997)
]

print("4.3 dataclass - книги до сортировки:")
for book in books:
    print(book)

books.sort(key=lambda x: x.year)
print("\nКниги после сортировки по году:")
for book in books:
    print(book)