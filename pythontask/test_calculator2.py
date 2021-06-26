from conftest import get_clac_data
import pytest
import allure
import logging

totals = get_clac_data()
driver = None


@allure.feature("计算器")
class TestCalculator2:

    # 传参调用fixture，并调用fixture的返回
    # 整数相加
    @allure.story("相加功能")
    @allure.title("整数相加")
    @pytest.mark.add
    @pytest.mark.parametrize('a, b, expect', totals['add']['int']['datas'], ids=totals['add']['int']['ids'])
    def test_add_int(self, a, b, expect, start_and_end, fix_get_clac):
        with allure.step(f"测试步骤1：加法计算 {a} + {b} = {expect}"):
            logging.info(f"test_add_int: 测试数据：{a} + {b}")
            assert expect == fix_get_clac.add(a, b)
        with allure.step(f"测试步骤2：截图"):
            allure.attach.file("./img/test.png", name="test.png", attachment_type=allure.attachment_type.PNG)



    # 通过 pytest.mark.usefixtures 调用 fixture
    # 浮点数相加
    @allure.title("浮点数相加")
    @allure.story("相加功能")
    @pytest.mark.add
    @pytest.mark.parametrize('a, b, expect', totals['add']['float']['datas'], ids=totals['add']['float']['ids'])
    @pytest.mark.usefixtures('start_and_end')
    def test_add_float(self, a, b, expect, fix_get_clac):
        logging.info(f"test_add_float: 测试数据：{a} + {b}")
        assert expect == fix_get_clac.add(a, b)

    # 调用通过fixture获取的被测方法
    # 复数相加
    @allure.title("复数相加")
    @allure.story("相加功能")
    @pytest.mark.add
    @pytest.mark.parametrize('a, b, expect', totals['add']['complex']['datas'], ids=totals['add']['complex']['ids'])
    def test_add_complex(self, a, b, expect, fix_get_clac):
        logging.info(f"test_add_complex: 测试数据：{a} + {b}")
        a, b, expect = complex(a), complex(b), complex(expect)
        assert expect == fix_get_clac.add(a, b)

    # 调用通过fixture获取的测试数据
    # 错误数据类型相加
    @allure.title("异常数据相加: {fix_get_datas[0]} + {fix_get_datas[1]}")
    @allure.story("相加功能")
    @pytest.mark.add
    def test_add_other(self, fix_get_datas, fix_get_clac):
        logging.info(f"test_add_other: 测试数据：{fix_get_datas[0]} + {fix_get_datas[1]}")
        with pytest.raises(TypeError):
            assert fix_get_datas[2] == fix_get_clac.add(fix_get_datas[0], fix_get_datas[1])

    @allure.title("被除数为0")
    @allure.story("相除功能")
    @pytest.mark.parametrize('a, b, expect', totals['div']['zeroerror']['datas'], ids=totals['div']['zeroerror']['ids'])
    @pytest.mark.div
    def test_div_zeroerror(self, a, b, expect, fix_get_clac):
        logging.info(f"test_div_zeroerror: 测试数据：{a} / {b}")
        with pytest.raises(ZeroDivisionError):
            assert expect == fix_get_clac.div(a, b)

    @allure.title("整数相除")
    @allure.story("相除功能")
    @pytest.mark.parametrize('a, b, expect', totals['div']['int']['datas'], ids=totals['div']['int']['ids'])
    @pytest.mark.div
    def test_div_int(self, a, b, expect, fix_get_clac):
        logging.info(f"test_div_int: 测试数据：{a} / {b}")
        assert expect == fix_get_clac.div(a, b)

    @allure.title("浮点数相除")
    @allure.story("相除功能")
    @pytest.mark.parametrize('a, b, expect', totals['div']['float']['datas'], ids=totals['div']['float']['ids'])
    @pytest.mark.div
    def test_div_float(self, a, b, expect, fix_get_clac):
        logging.info(f"test_div_float: 测试数据：{a} / {b}")
        assert expect == fix_get_clac.div(a, b)

    @allure.title("复数相除")
    @allure.story("相除功能")
    @pytest.mark.parametrize('a, b, expect', totals['div']['complex']['datas'], ids=totals['div']['complex']['ids'])
    @pytest.mark.div
    def test_div_complex(self, a, b, expect, fix_get_clac):
        logging.info(f"test_div_complex: 测试数据：{a }/ {b}")
        a, b, expect = complex(a), complex(b), complex(expect)
        assert expect == fix_get_clac.div(a, b)

    @allure.title("错误类型相除")
    @allure.story("相除功能")
    @pytest.mark.parametrize('a, b, expect', totals['div']['typeerror']['datas'], ids=totals['div']['typeerror']['ids'])
    @pytest.mark.div
    def test_div_typeerror(self, a, b, expect, fix_get_clac):
        logging.info(f"test_div_typeerror: 测试数据：{a} / {b}")
        with pytest.raises(TypeError):
            assert expect == fix_get_clac.div(a, b)
