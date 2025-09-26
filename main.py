"""
Главный модуль, использующий math_utils
"""

from math_utils import add, mul

if __name__ == "__main__":
    print("=== 3. МОДУЛЬНОСТЬ И ПАКЕТЫ ===")
    print("3.1 Использование модуля math_utils:")
    
    result_add = add(5, 3)
    result_mul = mul(4, 7)
    
    print(f"add(5, 3) = {result_add}")
    print(f"mul(4, 7) = {result_mul}")
    print()