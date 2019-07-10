#CAR TRACK, sine wave 
import turtle
import time
import math
wn=turtle.Screen()
wn.bgcolor('lightgreen')
s=turtle.Shape("compound")
turtle.tracer(2)
t1=turtle.Turtle('turtle')
t1.setheading(0)
t1.shapesize(1)
t1.pensize(20)
t1.color('grey')
t1.hideturtle()
t1.up()

R=100
t2=turtle.Turtle()
t2.setheading(0)
t2.shapesize(1)
t2.pensize(40)
t2.color('green')
t2.hideturtle()
t2.up()

def road1():
    for j in range (-360,360):
        SIN=50*math.sin(j/25)
        if j==-360:
            t1.goto(j,SIN)
        t1.down()
        t1.setposition(j,SIN)
        a.setposition(j,SIN)
        a.setheading(50*math.cos(j/25))
        time.sleep(0.01)

# Car Drawing    
#Head
head=turtle.Turtle()
head.hideturtle()
head.penup()
head.goto(-20,30)
head.begin_poly()
for i in range (2):
    head.fd(40)
    head.right(90)
    head.fd(20)
    head.right(90)
head.end_poly()
m1=head.get_poly()
s.addcomponent(m1,'blue')

#Body
body=turtle.Turtle()
body.hideturtle()
body.penup()
body.goto(-50,10)
body.begin_poly()
for j in range (2):
    body.fd(100)
    body.right(90)
    body.fd(15)
    body.right(90)
body.end_poly()
m2=body.get_poly()
s.addcomponent(m2,'red')

#Leg1
leg1=turtle.Turtle()
leg1.hideturtle()
leg1.penup()
leg1.goto(-35,-10) 
leg1.begin_poly()
leg1.circle(10)
leg1.end_poly()
m3=leg1.get_poly()
s.addcomponent(m3,'black')

#Leg2
leg2=turtle.Turtle()
leg2.hideturtle()
leg2.penup()
leg2.goto(35,-10) 
leg2.begin_poly()
leg2.circle(10)
leg2.end_poly()
m4=leg2.get_poly()
s.addcomponent(m4,'black')

wn.register_shape('man',s)
a=turtle.Turtle(shape='man')
a.up()
a.tilt(90)
a.goto(0,-2*R)
a.showturtle()
a.shapesize(0.5)

road1()


