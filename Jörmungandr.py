import turtle
import time
import random
score=0
high_score=0
delay=0.1
wn=turtle.Screen()
wn.bgcolor("light blue")
wn.setup(600,600)
wn.title("Jörmungandr - The World Serpent")
wn.bgcolor("light blue")
wn.tracer(0)

#head snake
head=turtle.Turtle()
head.pensize(5)
head.speed(0)
head.shape("circle")
head.color("white")
head.penup()
head.goto(0,0)
head.direction="stop"

#snake food
food=turtle.Turtle()
food.pensize(5)
food.speed(0)
food.shape("turtle")
food.color("green")
food.lt(90)
food.penup()
food.goto(0,100)

#title Screen
frog = turtle.Turtle()
frog.speed(0)
frog.shape("circle")
frog.color("white")
frog.penup()
frog.hideturtle()
frog.goto(0, 260)
frog.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

#body
body=[]

#functions for moving snake head by keys
def up():
    head.direction="up"
def down():
    head.direction="down"
def right():
    head.direction="right"
def left():
    head.direction="left"


#functions for moving snake head
def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)  #current y postion
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20) #current X postion
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)  #current y postion
    if head.direction=="left":
        x=head.xcor() 
        head.setx(x-20)  #current X postion

#keyboard binding to the function
wn.listen()
wn.onkey(up,"Up")
wn.onkey(down,"Down")
wn.onkey(right,"Right")
wn.onkey(left,"Left")
while True:
    wn.update()
    # wall collision code
    if head.xcor() > 290 or head.xcor() <-290 or head.ycor()>290 or head.ycor()<-290:
        head.goto(0,0)
        head.direction="stop"
        for x in body:
            x.goto(1000,1000)
        body.clear()
        # resit the score to 0
        score=0
        frog.clear()
        frog.write("Score:{}  High Score:{}".format(score, high_score),align="center",font=("Courier",24,"normal"))
    # the food moves to a random position of collison of the head
    if head.distance(food)<20:
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)
        #new body segment
        segment=turtle.Turtle()
        #segment.pensize(5)
        segment.speed(0)
        segment.shape("circle")
        segment.color("white")
        segment.penup()
        body.append(segment)
        # setting the score
        score+=10
        if score > high_score:
            high_score=score
        frog.clear()
        frog.write("Score:{}  High Score:{}".format(score, high_score),align="center",font=("Courier",24,"normal"))
# increase score
    # code for adding body by -1
    
    for i in range(len(body)-1,0,-1):
        x=body[i-1].xcor()
        y=body[i-1].ycor()
        body[i].goto(x,y)
    if  len(body)>0:
        x=head.xcor()
        y=head.ycor()
        body[0].goto(x,y)     
    move()
    # body collision
    for x in body:
        if x.distance(head) < 20:
            head.goto(0,0)
            head.direction="stop"
            for x in body:
                x.goto(1000,1000)
            body.clear()
            
    time.sleep(delay)
wn.mainloop()


