import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 6, 6) == 36

    # def test_multiply_failed(self):
    #     assert self.calc.multiply(self, 6, 6) == 46

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 10, 5) == 2

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 40, 10) == 30

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 15, 5) == 20