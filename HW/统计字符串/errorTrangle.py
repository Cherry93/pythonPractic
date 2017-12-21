# #import math
#
# # 自定义异常，精细化地定位和提示错误信息
# class TriangleError(Exception):
#     side1 =0
#     side2 =0
#     side3 =0
#
#     def __init__(self,side1,side2,side3):
#         super(TriangleError, self).__init__()
#         self.side1 = side1
#         self.side2 = side2
#         self.side3 = side3
#         # self.side1 = a
#         # self.side2 = b
#         # self.side3 = c
#     # def getSide1(self):
#     #     return self.__side1
#     #
#     # def getSide2(self):
#     #     return self.__side2
#     #
#     # def getSide3(self):
#     #     return self.__side3
#     def __str__(self):
#         return "三角形异常："
#
#
# def calcCircleArea(side1,side2,side3):
#
#     # 如果三条边不能形成三角形，导致无法正常继续下去，抛出一个异常
#       if (side1+side2-side3)*(side1+side3-side2)*(side2+side3-side1)<0 and side1<0 and side2<0 and side3<0:
#
#     # 抛出一个异常
#          raise TriangleError ("wrong!")
#
# side1,side2,side3 = eval(input("请输入三角形三条边的边长："))
#
#
# # 这个函数有可能抛出异常
# try:
#     calcCircleArea(side1, side2, side3)
# except TriangleError as re:
#     print(re)
#     pass
#
class GeometricObject:
    def __init__(self, color="green", filled=True):
        self.__color = color
        self.__filled = filled

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def isFilled(self):
        return self.__filled

    def setFilled(self, filled):
        self.__filled = filled

    def __str__(self):
        return "color: " + self.__color + \
               " and filled: " + str(self.__filled)
class Triangle(GeometricObject):


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

    def checkTriangle(self):
        if (self.side1 + self.side2 - self.side3) * (self.side1 + self.side3 - self.side2) * (
                self.side2 + self.side3 - self.side1) < 0 or self.side1 < 0 or self.side2 < 0 or self.side3 < 0:
          raise TriangleError(self.side1,self.side2,self.side3)
        else:
            print("可以组成三角形")

    def __str__(self):
        superStr = super(Triangle, self).__str__()
        return superStr +"\n=>Triangle:" + str({"side1": self.side1, "side2": self.side2, "side3": self.side3})

# def testTriangle():
#     t = Triangle(3, 4, 5, filled=False)
#     print(t)
#     print(t.getArea())
#
# if __name__ == '__main__':
#     testTriangle()
#     pass
class TriangleError(RuntimeError):
    def __init__(self, side1, side2, side3):
       super(TriangleError, self).__init__()
       self.__side1 = side1
       self.__side2 = side2
       self.__side3 = side3

    def getSide1(self):
        return self.__side1

    def setSide1(self, side1):
        self.__side1 = side1

    def getSide2(self):
        return self.__side2

    def setSide2(self, side2):
        self.__side2 = side2

    def getSide3(self):
        return self.__side3

    def setSide3(self, side3):
        self.__side3 = side3
    def __str__(self):
        return "三角形异常"

def testTriangle():
    t = Triangle(1, 1, 3,color="red", filled=False)
    print(t)
    print(t.getArea())

    try:
     t.checkTriangle()
    except TriangleError as re:
     print(re)
    pass
testTriangle()