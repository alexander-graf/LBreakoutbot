import turtle

wn =turtle.Screen()
wn.title("Pong lala juhu")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


# Main loop



# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)  # maximaler speed
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)
paddle_a.shapesize(stretch_wid=5, stretch_len=1)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)  # maximaler speed
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0)
paddle_b.shapesize(stretch_wid=5, stretch_len=1)

# Ball zeichnen

# Paddle B
ball = turtle.Turtle()
ball.speed(0)  # maximaler speed
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)




# Ball
while True:
    wn.update()

