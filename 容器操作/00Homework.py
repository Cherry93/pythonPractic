# 导入整个模块
import demos.W2.day2.SuperTurtle
# import mytool.SuperTurtle

# 导入模块的个别成员
from demos.W2.day2.SuperTurtle import drawText
from demos.W2.day2.SuperTurtle import *

# from mytool.SuperTurtle import *

# demos.W2.day2.SuperTurtle.drawText()

# drawLine(
#     0,0,300,400,
#     10,10,200,200,
#     color="red",pensize=10,
#     food="鸡腿",drink="1984年的雪花纯生"
# )

drawText(
    0, 0, "鸡腿",
    "汉堡", 666, False,
    color="#ff0000",
    food="鸡腿", drink="1984年的雪花纯生"
)
