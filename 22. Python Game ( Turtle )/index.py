import turtle 

screen = turtle.Screen()
screen.title('PING PONG')
screen.bgcolor(0.5,0.5,0.5)
screen.setup(width=800, height=600)
screen.tracer(0)

step = 10


first_paddle = turtle.Turtle()
first_paddle.shape("square")
first_paddle.color('white')
first_paddle.shapesize(stretch_len=1 , stretch_wid=5)
first_paddle.penup()
first_paddle.goto(-350, 0 )



second_paddle = turtle.Turtle()
second_paddle.shape("square")
second_paddle.color('white')
second_paddle.shapesize(stretch_len=1 , stretch_wid=5)
second_paddle.penup()
second_paddle.goto(350, 0 )



def first_paddle_up():
    y = first_paddle.ycor()
    y = y + step 
    first_paddle.sety(y)
    if y > 240 : 
        first_paddle.sety(240)


def first_paddle_down():
    y = first_paddle.ycor()
    y = y - step 
    first_paddle.sety(y)
    if y > -240 : 
        first_paddle.sety(240)


screen.listen()
screen.onkeypress( first_paddle_up , "w")
screen.onkeypress( first_paddle_down , "s")   

while(1):
    screen.update()