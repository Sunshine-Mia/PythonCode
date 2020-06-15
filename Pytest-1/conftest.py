import pytest
from cal import Calculator


@pytest.fixture()
def conf():
    print("开始计算")
    cal = Calculator()
    yield cal
    print("计算结束")
