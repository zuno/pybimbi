import turtle
import random


def start(border=20):
    global p, s
    s = turtle.Screen()
    s.delay(0)
    _wsize(border)
    p = turtle.Pen(shape="blank", visible=False)
    p.speed(0)
    p.penup()


def clear():
    s.clear()

def end():
    turtle.done()


def plot(x, y, color=None):
    if color is not None:
        o = p.color()
        p.color(color)
    d = p.isdown()
    p.penup()
    p.goto(x, y)
    p.pendown()
    p.goto(x, y)
    if not d:
        p.penup()
    if color is not None:
        p.color(o)


def goto(x, y):
    d = p.isdown()
    p.penup()
    p.goto(x, y)
    if d:
        p.pendown()


def line(x1, y1, x2=None, y2=None, color=None, rel=False):
    if color is not None:
        o = p.color()
        p.color(color)
    d = p.isdown()
    if rel:
        px, py = p.pos()
    else:
        px, py = 0, 0
    if x2 is None or y2 is None:
        p.pendown()
        p.goto(x1+px, y1+py)
    else:
        p.penup()
        p.goto(x1+px, y1+py)
        p.pendown()
        p.goto(x2+px, y2+py)
    if not d:
        p.penup()
    if color is not None:
        p.color(o)


def _rline(x, y, color=None):
    if color is not None:
        o = p.color()
        p.color(color)
    d = p.isdown()
    x1, y1 = p.pos()
    p.pendown()
    p.goto(x1+x, y1+y)
    if not d:
        p.penup()
    if color is not None:
        p.color(o)


def border(c="white"):
    d = p.color()
    p.color(c)
    w = int(s.window_width()/2)/turtle._CFG["width"]
    h = int(s.window_height()/2)/turtle._CFG["height"]
    p.penup()
    p.goto(w, h)
    p.pendown()
    p.begin_fill()
    p.goto(w,-h)
    p.goto(-w,-h)
    p.goto(-w,h)
    p.goto(w,h)
    p.goto(maxx,maxy)
    p.goto(maxx,miny)
    p.goto(minx,miny)
    p.goto(minx,maxy)
    p.goto(maxx,maxy)
    p.end_fill()
    p.color(d[0],d[1])


def paper(color="white"):
    if isinstance(color,tuple):
        color="#%02x%02x%02x" % (int(color[0]*255),int(color[1]*255),int(color[2]*255))
    s.screensize(bg=color)
    if p.isdown():
        p.penup()
        p.pendown()
    else:
        p.pendown()
        p.penup()


def ink(color="black"):
    p.color(color)

def randcol():
    return "#%02x%02x%02x" % (random.randint(0,255), random.randint(0,255), random.randint(0,255))


def _wsize(b=20):
    global maxx, maxy, minx, miny
    w = s.window_width()
    h = s.window_height()
    maxx = int(w/2)-b
    maxy = int(h/2)-b
    minx = -int(w/2)+b
    miny = -int(h/2)+b

maxx=0
maxy=0
minx=0
miny=0
w=0
h=0

colors=[
    "black",
    "blue",
    "red",
    "magenta",
    "green",
    "cyan",
    "yellow",
    "white"
]


if __name__ == "__main__":
    start()
    import random
    border("red")
    paper("yellow")
    ink((0,1,0))
    for i in range(1,100):
        plot(random.randint(minx,maxx),random.randint(miny,maxy))

    line(minx, 0, maxx, 0)
    line(0, miny, 0, maxy)
    line(minx, miny, maxx, maxy)
    line(maxx, miny, minx, maxy)

    line(minx, miny, minx, maxy)
    line(maxx, miny, maxx, maxy)
    line(minx, miny, maxx, miny)
    line(minx, maxy, maxx, maxy)

    for x in range(0, maxx+1, 10):
        line(x, -5, x, 5)

    for y in range(0, maxy+1, 10):
        line(-5, y, 5, y)

    end()

