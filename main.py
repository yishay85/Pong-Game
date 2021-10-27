import turtle
import tkinter
HEIGHT = 600
WIDTH = 800

running = True
# Score
score_a = 0
score_b = 0

win = turtle.Screen()  # הגדרת מסך
win.title("Pong")  # כותרת
win.bgcolor("black")  # צבע לרקע
win.setup(width=WIDTH, height=HEIGHT)  # הגדרת גודל מסך
win.tracer(0)  # מונע הקפאת מסך


canvas = win.getcanvas()  # or, equivalently: turtle.getcanvas()
root = canvas.winfo_toplevel()

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)  # מהירות אנימציה
paddle_a.shape("square")  # צורת האנימציה
paddle_a.color("white")  # צבע הצורה
paddle_a.shapesize(stretch_wid=5, stretch_len=1)  # גודל צורה
paddle_a.penup()  # כדי שלא יהיה קבוע במקום
paddle_a.goto(-(WIDTH / 2 - 50), 0)  # מיקום התחלתי

# Paddle B

paddle_b = turtle.Turtle()
paddle_b.speed(0)  # מהירות אנימציה
paddle_b.shape("square")  # צורת האנימציה
paddle_b.color("white")  # צבע הצורה
paddle_b.shapesize(stretch_wid=5, stretch_len=1)  # גודל צורה
paddle_b.penup()  # כדי שלא יהיה קבוע במקום
paddle_b.goto(WIDTH / 2 - 50, 0)  # מיקום התחלתי

# Ball
ball = turtle.Turtle()
ball.speed(0)  # מהירות אנימציה
ball.shape("circle")  # צורת האנימציה
ball.color("white")  # צבע הצורה
ball.penup()  # כדי שלא יהיה קבוע במקום
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(0, HEIGHT / 2 - 40)
pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 20, "normal"))
# mom

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


def quit():
    global running
    running = False

root.protocol("WM_DELETE_WINDOW", quit)


win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")
win.onkeypress(quit, "q")

while running:
    win.update()  # מעדכן את המסך

    # move the ball
    ball.setx(ball.xcor() + ball.dx)  # מעדכן את מיקום הכדור
    ball.sety(ball.ycor() + ball.dy)

    # Border check
    if ball.ycor() >= HEIGHT / 2 - 10:
        ball.sety(HEIGHT / 2 - 10)
        ball.dy *= -1

    if ball.ycor() <= -(HEIGHT / 2 - 10):
        ball.sety(-(HEIGHT / 2 - 10))
        ball.dy *= -1

    if ball.xcor() >= WIDTH / 2 - 10:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 20, "normal"))

    if ball.xcor() <= -(WIDTH / 2 - 10):
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 20, "normal"))

    # Paddle and ball collisions
    if (ball.xcor() > WIDTH / 2 - 60 and ball.xcor() < WIDTH / 2 - 50) and (
            ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(WIDTH / 2 - 60)
        ball.dx *= -1
    if (ball.xcor() < -(WIDTH / 2 - 60) and ball.xcor() > -(WIDTH / 2 - 50)) and (
            ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-(WIDTH / 2 - 60))
        ball.dx *= -1
    if not running:
        break

