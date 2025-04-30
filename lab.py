def factorial_recursive(n):
    """
    Обчислює факторіал числа n рекурсивно.

    Аргументи:
    n (int): Невід'ємне ціле число.

    Повертає:
    int: Факторіал числа n.
    """
    if not isinstance(n, int):
        raise TypeError("Аргумент має бути цілим числом")
    if n < 0:
        raise ValueError("Факторіал визначено лише для невід'ємних чисел")
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)


def fibonacci_recursive(n):
    """
    Обчислює n-те число Фібоначчі рекурсивно.

    Аргументи:
    n (int): Невід'ємне ціле число.

    Повертає:
    int: n-те число Фібоначчі.
    """
    if not isinstance(n, int):
        raise TypeError("Аргумент має бути цілим числом")
    if n < 0:
        raise ValueError("Фібоначчі визначено лише для невід'ємних чисел")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def sum_list_recursive(lst):
    """
    Обчислює суму елементів списку рекурсивно.

    Аргументи:
    lst (list): Список чисел.

    Повертає:
    int або float: Сума елементів списку.
    """
    if not isinstance(lst, list):
        raise TypeError("Аргумент має бути списком")
    if not lst:
        return 0
    return lst[0] + sum_list_recursive(lst[1:])


def is_palindrome_recursive(s):
    """
    Перевіряє, чи є рядок паліндромом, рекурсивно.

    Аргументи:
    s (str): Вхідний рядок.

    Повертає:
    bool: True, якщо рядок є паліндромом, інакше False.
    """
    if not isinstance(s, str):
        raise TypeError("Аргумент має бути рядком")
    s = ''.join(filter(str.isalnum, s)).lower()
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome_recursive(s[1:-1])


# Демонстрація роботи
if __name__ == "__main__":
    print("Факторіал 5:", factorial_recursive(5))
    print("10-те число Фібоначчі:", fibonacci_recursive(10))
    print("Сума [1, 2, 3, 4, 5]:", sum_list_recursive([1, 2, 3, 4, 5]))
    print("Чи є 'A man a plan a canal Panama' паліндромом?:", is_palindrome_recursive("A man a plan a canal Panama"))
