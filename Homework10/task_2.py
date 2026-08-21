# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest

def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division

# Тест деления на ноль
def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        all_division(10, 0)

# Тест деления на единицу (маркирован как smoke)
@pytest.mark.smoke
def test_division_by_one():
    assert all_division(10, 1) == 10

# Тест умножения на отрицательное число (деление на отрицательное число)
@pytest.mark.smoke
def test_division_by_negative():
    assert all_division(10, -2) == -5

# Тест деления на отрицательное число
def test_division_with_negative():
    assert all_division(-20, -4) == 5

# Тест умножения на единицу (деление на единицу)
def test_multiplication_by_one():
    assert all_division(1, 1) == 1