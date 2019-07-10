# CAR TRACK, rectangle 
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
t1.pensize(30)
t1.color('green')
t1.hideturtle()
t1.down
t1.goto(0,0)
for j in range (2):
    t1.fd(300)
    t1.right(90)
    t1.fd(200)
    t1.right(90)

t1.up()



t2=turtle.Turtle()
t2.setheading(0)
t2.shapesize(1)
t2.pensize(40)
t2.color('green')
t2.hideturtle()
t2.up()

def road1():

    for i in range (2):
        
        for j in range (300):
            a.fd(1)
            time.sleep(0.01)
        a.right(90)
        for j in range (200):
            a.fd(1)
            time.sleep(0.01)
        a.right(90)
 
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
a.goto(0,0)
a.setheading(0)
b=a.heading()
print(b)
a.showturtle()

a.shapesize(0.5)

while True:
    road1()
