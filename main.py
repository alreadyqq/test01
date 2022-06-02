import base.nomal
import base.request

# 实例化类
test = base.request.SendRequest("初始化类的参数")

if __name__ == '__main__':
    # 调用类方法
    test.test_classmethod("类函数参数")
    # 调用实例方法
    test.public_method("实例参数")
    # 调用静态方法
    base.request.SendRequest.test_staticmethod("静态参数")
    # 调用普通方法
    base.nomal.nomal_method("普通参数")
