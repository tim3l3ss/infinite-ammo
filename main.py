"""
Главный модуль, который импортирует и использует функции из math_utils и пакета shapes
"""

# Импорт из модуля math_utils
from math_utils import add, mul

# Импорт из пакета shapes
from shapes.circle import area_circle
from shapes.square import area_square

def main():
    print("=== МОДУЛЬНОСТЬ И ПАКЕТЫ ===\n")
    
    # 1. Тестирование функций из math_utils
    print("1. Тестирование модуля math_utils:")
    result_add = add(10, 5)
    result_mul = mul(7, 3)
    
    print(f"add(10, 5) = {result_add}")
    print(f"mul(7, 3) = {result_mul}")
    print()
    
    # 2. Тестирование функций из пакета shapes
    print("2. Тестирование пакета shapes:")
    
    # Тестируем функцию area_circle
    radius = 5
    circle_area = area_circle(radius)
    print(f"Площадь круга с радиусом {radius}: {circle_area:.2f}")
    
    # Тестируем функцию area_square
    side = 4
    square_area = area_square(side)
    print(f"Площадь квадрата со стороной {side}: {square_area}")
    
    print("\nВсе функции работают корректно!")

if __name__ == "__main__":
    main()
