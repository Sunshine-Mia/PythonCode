# 创建模块，模块里面创建方法，定义有参数，和无参数，有返回值和无返回值 的情况，并说明 无返回值的默认返回值
# 无参数，无返回值,默认返回None
def func1():
    print("f1: ", "Hello Python!")

# 有默认参数，无返回值
def func2(arg1 = 'default'):
    print("f2: ", arg1)

# 有参数，有返回值
def func3(arg1, arg2):
    return arg1 + arg2

if __name__ == '__main__':
    f1 = func1()
    f2 = func2()
    f3 = func3('abc', '123')
    print("f3: ", f3)