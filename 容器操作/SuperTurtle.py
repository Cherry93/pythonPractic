'''
·封装一个超级乌龟工具
·实现直线绘制函数，参数有起止坐标、颜色、笔刷大小
·实现圆绘制函数，参数圆心坐标、半径、颜色、笔刷大小
·实现矩形绘制函数，参数有点坐标、颜色、笔刷大小
·实现文本绘制函数，参数有坐标、字体、字号、颜色、字体风格
·使用尽量多的参数类型
·在本地（工程内）导入并使用该工具
·将该工机具丢入系统类库，导入并使用
'''
import turtle


def drawLine(x1, y1, x2, y2,*moreLines,color="black", pensize=5,**infos):
    print("drawLine")
    print("moreLines",moreLines)
    print("infos",infos)

    turtle.showturtle()
    turtle.color(color)
    turtle.pensize(pensize)

    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)

    turtle.penup()
    turtle.goto(moreLines[0], moreLines[1])
    turtle.pendown()
    turtle.goto(moreLines[2], moreLines[3])

    turtle.done()


def drawCircle(cx, cy, raius,   *moreCircles,   color="black", pensize=5,   **infos):
    print("drawCircle")
    pass


def drawRect(
        x1, y1, x2, y2,
        *moreCircles,
        color="black", pensize=5,
        **infos
):
    print("drawRect")
    pass


def drawText(
        x,y,text,
        *texts,
        font="宋体",color="black",style="normal",pensize=20,
        **infos
):
    print("drawText")
    print("infos",infos)
    print("texts",texts)

    turtle.showturtle()
    turtle.color(color)

    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.write(text,move=True, align="center", font=(font, pensize, style))

    turtle.hideturtle()
    turtle.done()
