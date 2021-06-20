from pythoncode.calculator import Div
import pytest
import yaml


class TestDivInput:

    def setup(self):
        print("开始计算")

    def teardown(self):
        print("结束计算")

    @pytest.mark.parametrize("a, b, expect", yaml.safe_load(open("div_input_type.yaml")))
    def test_input_type(self, a, b, expect):
        div = Div()
        with pytest.raises(TypeError):
            assert div.div(a, b) == expect

    @pytest.mark.parametrize("a, b, expect", yaml.safe_load(open("div_input_oversize.yaml")))
    def test_input_len(self, a, b, expect):
        div = Div()
        assert div.div(a, b) == expect

    @pytest.mark.parametrize("a, b, expect", yaml.safe_load(open("div_input_zero.yaml")))
    def test_input_zero(self, a, b, expect):
        div = Div()
        with pytest.raises(ZeroDivisionError):
            assert div.div(a, b) == expect

    @pytest.mark.parametrize("a, b, expect", yaml.safe_load(open("div_input_none.yaml")))
    def test_input_none(self, a, b, expect):
        div = Div()
        with pytest.raises(TypeError):
            assert div.div(a, b) == expect


class TestDivOutput:

    def setup(self):
        print("开始计算")

    def teardown(self):
        print("结束计算")

    @pytest.mark.parametrize("a, b, expect", yaml.safe_load(open("div_output_oversize.yaml")))
    def test_output_oversize(self, a, b, expect):
        div = Div()
        assert div.div(a, b) == expect

    @pytest.mark.parametrize("a, b, expect", yaml.safe_load(open("div_output.yaml")))
    def test_output(self, a, b, expect):
        div = Div()
        assert div.div(a, b) == expect
