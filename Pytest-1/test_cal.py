import pytest
import yaml


@pytest.mark.parametrize("data", yaml.safe_load(open("./data_cal.yml")))
class TestCal:

    def test_add(self, conf, data):
        print("--加法--")
        assert data['re_add'] == conf.add(data['a'], data['b'])

    def test_subtract(self, conf, data):
        print("--减法--")
        assert data['re_sub'] == conf.subtract(data['a'], data['b'])

    def test_multiply(self, conf, data):
        print("--乘法--")
        assert data['re_mul'] == conf.multiply(data['a'], data['b'])

    def test_divide(self, conf, data):
        print("--除法--")
        assert '%.2f' % data['re_div'] == '%.2f' % conf.divide(data['a'], data['b'])
