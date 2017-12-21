# ·封装一个超级乌龟工具
#  使用尽量多的参数
# ·实现直线绘制方法，参数有起止坐标、颜色、笔刷大小
# ·实现圆绘制方法，参数圆心坐标、半径、颜色、笔刷大小、#是否填充
# ·实现矩形绘制方法，参数有对角线坐标、颜色、笔刷大小
# ·实现文本绘制方法，参数有坐标、字体、字号、颜色、字体风格
# ·在外界导入并使用该工具
#  在本地
import turtle

turtle.showturtle()
def drawLine(x1,x2,y1,y2,size,color):
     turtle.showturtle()
     turtle.penup()
     turtle.goto(x1,x2)
     turtle.pendown()
     color = turtle.color(color,)
     size= turtle.pensize(size)
     turtle.goto(y1,y2)
     #turtle.done()
    #print()
def drawCircle(x3,x4,r,color,size,fillcolor):
    turtle.showturtle()
    turtle.penup()
    color = turtle.color(color)
    size = turtle.pensize(size)
    fillcolor = turtle.fillcolor(fillcolor)
    turtle.goto(x3,x4-r)
    turtle.pendown()
    turtle.circle(r)
    #turtle.done()
    #print()
def rectangle(x4,x5,height,width,color,pensize):
    turtle.showturtle()
    turtle.penup()
    color = turtle.color(color, )
    size = turtle.pensize(pensize)
    turtle.goto(x4+width/2,x5+height/2)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    #turtle.done()
    #print()
def drawText(x6,x7,s,color,font=("楷体", 30, "italic")):
    turtle.showturtle()
    turtle.penup()
    #fontsize = turtle.pensize(fontsize)
    color = turtle.color(color)
    turtle.goto(x6,x7)
    turtle.pendown()
    turtle.write(s)
    turtle.done()
# drawLine(-50,-50,50,50,10,"red")
# drawCircle(50, 50, 50, "red", 5, "pink")
# rectangle(50,55,300,200,"green",10)
# drawText(50,58,"我是中国","blue")