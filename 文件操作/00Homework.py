import time
from demos.W2.day4.GeometricObject import GeometricObject


class Fan:
    # SLOW = 1
    # MEDIUM = 2
    # FAST = 3
    SLOW, MEDIUM, FAST = 1, 2, 3

    __speed = SLOW
    __on = False
    __radius = 0.0
    __color = None

    # 访问器
    def getSpeed(self):
        return self.__speed

    # 修改器
    def setSpeed(self, speed):
        self.__speed = speed

    # 访问器
    def getRaius(self):
        return self.__radius

    # 修改器
    def setRaius(self, radius):
        self.__radius = radius

    # 访问器
    def getColor(self):
        return self.__color

    # 修改器
    def setColor(self, color):
        self.__color = color

    # 访问器
    def isOn(self):
        return self.__on

    # 修改器
    def setOn(self, on):
        self.__on = on

    # 构造方法
    def __init__(self, speed, on, radius, color):
        self.__speed = speed
        self.__on = on
        self.__radius = radius
        self.__color = color

    # 定义并返回对象的打印样式
    def __str__(self):
        return str({"speed": self.__speed, "on": self.__on, "color": self.__color, "radius": self.__radius})


class StopWatch:
    __startTime = 0
    __endTime = 0

    def getStartTime(self):
        return self.__startTime

    def getEndTime(self):
        return self.__endTime

    def start(self):
        self.__startTime = time.time()

    def stop(self):
        self.__endTime = time.time()

    def getElapsedTime(self):
        return int((self.__endTime - self.__startTime) * 1000)


class Triangle(GeometricObject):
    side1 = 1.0
    side2 = 1.0
    side3 = 1.0

    def __init__(self, side1, side2, side3, color="green", filled=False):
        super(Triangle, self).__init__(color, filled)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def getSide1(self):
        return self.side1

    def getSide2(self):
        return self.side2

    def getSide3(self):
        return self.side3

    def getArea(self):
        s = self.getPerimeter() / 2
        return (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** (1 / 2)

    def getPerimeter(self):
        return self.side1 + self.side2 + self.side3

    def __str__(self):
        superStr = super(Triangle, self).__str__()
        return superStr +"\n=>Triangle:" + str({"side1": self.side1, "side2": self.side2, "side3": self.side3})


def testFan():
    fan1 = Fan(Fan.FAST, True, 10, "yellow")
    fan2 = Fan(Fan.MEDIUM, False, 5, "blue")
    print(fan1)
    print(fan2)


def testStopWatch():
    sw = StopWatch()
    sw.start()
    time.sleep(5)
    sw.stop()
    print("小明的百米成绩是：", sw.getElapsedTime())


def testTriangle():
    t = Triangle(3, 4, 5, filled=False)
    print(t)
    print(t.getArea())


if __name__ == '__main__':
    # testFan()
    # testStopWatch()
    # testTriangle()
    pass
