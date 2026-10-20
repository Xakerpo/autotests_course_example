# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest
class Test_main:
    @pytest.mark.usefixtures("class_fixture")
    def test_addition(self, test_duration_fixture):
        """Тест сложения."""
        result = 5 + 5
        assert result == 10

    def test_subtraction(self, test_duration_fixture):
        """Тест вычитания."""
        result = 6 - 5
        assert result == 1

    def test_multiplication(self):
        """Тест умножения (без фикстуры для теста)."""
        result = 5 * 9
        assert result == 45