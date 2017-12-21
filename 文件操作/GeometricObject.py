class GeometricObject:
    def __init__(self, color = "green", filled = True):
        self.__color = color
        self.__filled = filled

    # 访问器：获取私有属性的值
    def getColor(self):
        return self.__color

    # 修改器：修改私有属性的值
    def setColor(self, color):
        self.__color = color

    def isFilled(self):
        return self.__filled

    def setFilled(self, filled):
        self.__filled = filled
  
    def __str__(self):
        return "color: " + self.__color + \
            " and filled: " + str(self.__filled)
