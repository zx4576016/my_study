# -*- coding: utf-8 -*-
# @Project: study_pyt
# @Author: Areli
# @File name: test_cal
# @Create time: 2021/5/31 15:36
from util.demo_calculator import CalculatorDemo
import pytest


class TestCal:

    def setup_class(self):
        self.cal = CalculatorDemo()

    @pytest.mark.add
    @pytest.mark.parametrize(['a', 'b', 'exp'], [
        (3, 4, 7),
        (5, 6, 7),
        (3, 5, 'a')
    ])
    def test_add(self, a, b, exp):
        result = self.cal.addd(a, b)
        assert result == exp

    @pytest.mark.add
    def test_add2(self):
        result = self.cal.addd(2, 8)
        assert result == 9

    @pytest.mark.sub
    def test_sub(self):
        result = self.cal.subb(98, 91)
        assert result == 7

    @pytest.mark.mul
    def test_mul(self):
        result = self.cal.mull(6, 9)
        assert result == 54

    @pytest.mark.div
    def test_div(self):
        result = self.cal.divv(6, 3)
        assert result == 2
