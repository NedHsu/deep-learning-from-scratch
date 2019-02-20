# coding: utf-8
class Man:
    """サンプルクラス"""

    def __init__(self, name):  # 建構子
        self.name = name
        print("Initilized!")

    def hello(self):  # 方法1
        print("Hello " + self.name + "!")

    def goodbye(self):  #方法2
        print("Good-bye " + self.name + "!")

m = Man("David")
m.hello()
m.goodbye()