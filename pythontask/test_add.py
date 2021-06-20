from pythoncode.calculator import Calculator
import pytest
import yaml


class TestJudgeInput:

    def setup(self):
        print("开始计算")

    def teardown(self):
        print("结束计算")

    # 验证输入的值
    @pytest.mark.parametrize("num1, num2, expect", yaml.safe_load(open("add_input_type.yaml")))
    def test_judge_input_type(self, num1, num2, expect):
        calc = Calculator()
        # 验证输入值得类型
        assert calc.judge_add(num1, num2) == expect

    @pytest.mark.parametrize("num1, num2, expect", yaml.safe_load(open("add_input_none.yaml")))
    def test_judge_input_none(self, num1, num2, expect):
        calc = Calculator()
        # 验证输入值不为空
        assert calc.judge_add(num1, num2) == expect

    @pytest.mark.parametrize("num1, num2, expect", yaml.safe_load(open("add_input_oversize.yaml")))
    def test_judge_input_len(self, num1, num2, expect):
        calc = Calculator()
        # 验证输入值得长度
        assert calc.judge_add(num1, num2,) == expect


class TestJudgeOutput:

    def setup(self):
        print("开始计算")

    def teardown(self):
        print("结束计算")

    # 验证计算结果
    @pytest.mark.parametrize("num1, num2, expect", yaml.safe_load(open("add_output_oversize1.yaml")))
    def test_judge_output_len(self, num1, num2, expect):
        # 验证结果长度
        calc = Calculator()
        assert calc.judge_add(num1, num2) == expect

    @pytest.mark.parametrize("num1, num2, expect", yaml.safe_load(open("add_output.yaml")))
    def test_judge_output_sum(self, num1, num2, expect):
        # 验证计算结果
        calc = Calculator()
        assert calc.judge_add(num1, num2) == expect
