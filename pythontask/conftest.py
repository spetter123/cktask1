from pythoncode.calculator2 import Calculator
import pytest
import yaml
import logging


def pytest_configure(config):
    config.addinivalue_line("markers", "input_typeerror")


def get_clac_data():
    with open(f"./calc_datas.yaml") as f:
        return yaml.safe_load(f)


@pytest.fixture()
def start_and_end():
    yield 'fixture return'


@pytest.fixture(scope="class", autouse=True)
def get_something():
    logging.info("开始计算")
    yield
    logging.info("结束计算")


# 获取被测方法
@pytest.fixture()
def fix_get_clac():
    clac = Calculator()
    yield clac


# 获取测试数据：params 接收的数据必须是list类型
@pytest.fixture(params=get_clac_data()['add']['typeerror']['datas'], ids=get_clac_data()['add']['typeerror']['ids'])
def fix_get_datas(request):
    return request.param
