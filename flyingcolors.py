import turtle;

win = turtle.Screen()
win.setup(height=600,width=800)
win.bgcolor('#FF9899')
win.title('color by Mickey')

t = turtle.Turtle()
t.color('white')

print(t.ycor())
print(t.xcor())

def goUp():
    t.color('#CC3366')
    y = t.ycor()
    y = y + 10
    t.sety(y)

def goDown():
    t.color('black')
    y = t.ycor()
    y = y - 10
    t.sety(y)

def left():
    t.color('#FF6699')
    x = t.xcor()
    x = x - 10
    t.setx(x)

def right():
    t.color('#FDE5B4')
    x = t.xcor()
    x = x + 10
    t.setx(x)

def clear():
    t.clear()

win.listen()
win.onkeypress(goUp, 'Up')
win.onkeypress(goDown, 'Down')
win.onkeypress(left, 'Left')
win.onkeypress(right, 'Right')
win.onkeypress(clear, 'x')

turtle.done()
