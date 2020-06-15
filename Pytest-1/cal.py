class Calculator:

    def add(self, a, b):
        if isinstance(a, str) or isinstance(b, str):
            raise TypeError("参数类型不正确")
        else:
            return a + b


    def subtract(self, a, b):
        if isinstance(a, str) or isinstance(b, str):
            raise TypeError("参数类型不正确")
        else:
            return a - b

    def multiply(self, a, b):
        if isinstance(a, str) or isinstance(b, str):
            raise TypeError("参数类型不正确")
        else:
            return a * b

    def divide(self, a, b):
        if isinstance(a, str) or isinstance(b, str):
            raise TypeError("参数类型不正确")
        elif b == 0:
            raise ZeroDivisionError("除数不能为0")
        else:
            return a / b
