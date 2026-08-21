# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

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
@pytest.mark.parametrize(
    "args, expected, marks",
    [
        # Тест деления на ноль (ожидается ZeroDivisionError)
        ((10, 0), ZeroDivisionError, pytest.raises(ZeroDivisionError)),

        # Тест деления на единицу (маркирован как smoke)
        pytest.param((10, 1), 10, None, marks=pytest.mark.smoke),

        # Тест деления на отрицательное число
        ((10, -2), -5, None),

        # Тест деления двух отрицательных чисел
        ((-20, -4), 5, None),

        # Пропускаемый тест (деление на единицу)
        pytest.param((1, 1), 1, None, marks=pytest.mark.skip("Пропускаем этот тест")),
    ],
)
def test_all_division(args, expected, marks):
    if isinstance(expected, type) and issubclass(expected, Exception):
        # Если ожидается исключение
        with marks:
            all_division(*args)
    else:
        # Обычное сравнение результата
        assert all_division(*args) == expected



