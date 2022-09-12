import turtle
import time
import math
def CreateTurtle(b,c,d,e):
    a=turtle.Turtle()
    a.penup()
    a.speed(10)
    a.fillcolor(b)
    SetPosition(a,c)
    a.shape(d)
    a.shapesize(e)
    return a
def SetPosition(g,d):
    g.hideturtle()
    g.setposition(d)
    g.showturtle()
def FindPosition(e):
    f,g=e.pos()
    fg=(round(f),round(g))
    return(fg)
def m(a):
    global moves
    moves[a]=True
def n0():
    global moves
    moves[0]=False
def n1():
    global moves
    moves[1]=False
def n2():
    global moves
    moves[2]=False
def n3():
    global moves
    moves[3]=False
def n4():
    global moves
    moves[4]=False
def n5():
    global moves
    moves[5]=False
def Health():
    pass
def move():
    if moves[0]:
        p1.fd(10)
    if moves[3]:
        p2.fd(10)
    if moves[1]:
        p1.rt(9)
    if moves[2]:
        p1.lt(9)
    if moves[4]:
        p2.rt(9)
    if moves[5]:
        p2.lt(9)
def bt1():
    global p1b,k1,p1pos
    if p1b[k1][2]==0 :
        p1b[k1][2]=1
        p1b[k1][0].setposition(p1pos)
        p1b[k1][0].setheading(p1.heading())
    if k1==4:
        k1=0
    else:
        k1=k1+1
def bt2():
    global p2b,k2,p2pos
    if p2b[k2][2]==0 :
        p2b[k2][2]=1
        p2b[k2][0].setposition(p2pos)
        p2b[k2][0].setheading(p2.heading())
    if k2==4:
        k2=0
    else:
        k2=k2+1
s1=('Lucida Sans Unicode',20,"bold",)
s2=('Lucida Sans Unicode',10,"italic")
h1=h2=100
k1=k2=0
p1b=[]
p2b=[]
moves=[False for x in range(6)]
p1=CreateTurtle('Blue',(-100,0),'turtle',1)
p2=CreateTurtle('Green',(100,0),'turtle',1)
control=turtle.Screen()
for i in range(5):
    b1=CreateTurtle('Blue',(-225,i*(-10)),"circle",0.4)
    p1b.append([b1,(-225,i*(-10)),0])
    b2=CreateTurtle('Green',(225,i*(-10)),"circle",0.4)
    p2b.append([b2,(225,i*(-10)),0])
ph1=turtle.Turtle()
ph1.speed(10)
ph1.hideturtle()
ph1.penup()
ph1.goto(-200,200)
ph1.pendown()
ph1.fd(400)
ph1.rt(90)
ph1.fd(400)
ph1.rt(90)
ph1.fd(400)
ph1.rt(90)
ph1.fd(400)
ph1.penup()
ph1.goto(-250,100)
ph1.pencolor('Blue')
ph1.write("PLAYER 1\n Health",font=s2,align="Center",)
ph1.goto(-250,50)
ph1.write(h1,font=s1,align="Center",)
ph2=turtle.Turtle()
ph2.speed(10)
ph2.hideturtle()
ph2.penup()
ph2.goto(250,100)
ph2.pencolor('Green')
ph2.write("PLAYER 2\n Health",font=s2,align="Center",)
ph2.goto(250,50)
ph2.write(h2,font=s1,align="Center",)
control.onkeypress(lambda:m(0),'d')
control.onkeypress(lambda:m(1),'c')
control.onkeypress(lambda:m(2),'z')
control.onkeypress(lambda:m(3),'Up')
control.onkeypress(lambda:m(4),'Right')
control.onkeypress(lambda:m(5),'Left')
control.onkeyrelease(n0,'d')
control.onkeyrelease(n1,'c')
control.onkeyrelease(n2,'z')
control.onkeyrelease(n3,'Up')
control.onkeyrelease(n4,'Right')
control.onkeyrelease(n5,'Left')
control.onkey(bt1,'x')
control.onkey(bt2,'Down')
control.listen()
while True:
    p1pos=FindPosition(p1)
    p2pos=FindPosition(p2)
    for i in range(5):
        p1bpos=FindPosition(p1b[i][0])
        p2bpos=FindPosition(p2b[i][0])
        if p1b[i][2]:
            if abs(p1bpos[0]-p2pos[0])<20 and abs(p1bpos[1]-p2pos[1])<20 :
                p2.fillcolor('Red')
                h2=h2-10;
                SetPosition(p1b[i][0],p1b[i][1])
                p1b[i][2]=0
                p2.fillcolor('Green')
            elif  200>p1bpos[0]>-200 and 200>p1bpos[1]>-200 :
                p1b[i][0].fd(15)
            else :
                p1b[i][2]=0
                SetPosition(p1b[i][0],p1b[i][1])
        if p2b[i][2]:
            if abs(p2bpos[0]-p1pos[0])<20 and abs(p2bpos[1]-p1pos[1])<20 :
                p1.fillcolor('Red')
                h1=h1-10
                SetPosition(p2b[i][0],p2b[i][1])
                p2b[i][2]=0
                p1.fillcolor('Blue')
            elif  200>p2bpos[0]>-200 and 200>p2bpos[1]>-200 :
                p2b[i][0].fd(15)
            else :
                p2b[i][2]=0
                SetPosition(p2b[i][0],p2b[i][1])
    if 200<=p1pos[0] or 200<=p1pos[1] or -200>=p1pos[0] or -200>=p1pos[1] :
        p1.undo()
    elif 200<=p2pos[0] or 200<=p2pos[1] or -200>=p2pos[0] or -200>=p2pos[1] :
        p2.undo()
    else:
        move()
        if abs(p1pos[0]-p2pos[0])<20 and abs(p1pos[1]-p2pos[1])<20 :
            if moves[0]:
                p2.fillcolor('Red')
                h2=h2-10
                p2.fillcolor('Green')
                p2.setposition(p2pos[0]+(70*math.cos(p1.heading()*(math.pi/180))),p2pos[1]+(70*math.sin(p1.heading()*(math.pi/180))))
                p1.bk(20)
            if moves[3]:
                p1.fillcolor('Red')
                h1=h1-10
                p1.fillcolor('Blue')
                p1.setposition(p1pos[0]+(70*math.cos(p2.heading()*(math.pi/180))),p1pos[1]+(70*math.sin(p2.heading()*(math.pi/180))))
                p2.bk(20)
        if h1<=0 or h2<=0 :
            break
        else :
            ph1.undo()
            ph1.write(h1,font=s1,align="Center")
            ph2.undo()
            ph2.write(h2,font=s1,align="Center")
    
if h1<h2 :
    ph1.undo()
    ph1.write("LOST",font=s1,align="Center")
    ph2.undo()
    ph2.write("WON",font=s1,align="Center")
else :
    ph1.undo()
    ph1.write("WON",font=s1,align="Center")
    ph2.undo()
    ph2.write("LOST",font=s1,align="Center")
        
    
