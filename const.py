# 定义一个常量类实现常量的功能
class _const:
    # 定义一个异常，继承自TypeError
    class ConstError(TypeError): pass

    # 定义一个方法，判断定义的常量是否包含在类自带的字典__dict__中
    def __setattr__(self, key, value):
        # 如果字典中已包含此变量，则抛出异常
        if key in self.__dict__:
            raise self.ConstError(f"Can not rebind const {key}")
        # 创建新的常量并赋值
        self.__dict__[key] = value
