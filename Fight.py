import turtle
import time
style1=('Lucida Sans Unicode',20,"bold",)
style2=('Lucida Sans Unicode',10,"italic")
health1=100
health2=100
def SetPosition(g,d):
    g.hideturtle()
    g.setposition(d)
    g.showturtle()
player1=turtle.Turtle()
player1.penup()
player1.speed(10)
SetPosition(player1,(-100,0))
player1.shapesize(2)
player1.fillcolor('Blue')
player2=turtle.Turtle()
player2.penup()
player2.speed(10)
SetPosition(player2,(100,0))
player2.shapesize(2)
player2.fillcolor("Yellow")
control=turtle.Screen()
bullets=[[],[]]
allowed=[[0,0,0,0,0],[0,0,0,0,0]]
bulletbox1=[(-225,0),(-225,-10),(-225,-20),(-225,-30),(-225,-40)]
bulletbox2=[(225,0),(225,-10),(225,-20),(225,-30),(225,-40)]
for i in range(5):
    bullet=turtle.Turtle()
    bullet.hideturtle()
    bullets[0].append(bullet)
    bullets[0][i].speed(10)
    bullets[0][i].penup()
    bullets[0][i].shape("circle")
    bullets[0][i].fillcolor('Blue')
    bullets[0][i].shapesize(0.4)
    bullets[0][i].setposition(bulletbox1[i])
    bullets[0][i].showturtle()
    
for i in range(5):
    bullet=turtle.Turtle()
    bullet.hideturtle()
    bullets[1].append(bullet)
    bullets[1][i].speed(10)
    bullets[1][i].penup()
    bullets[1][i].shape("circle")
    bullets[1][i].fillcolor('Yellow')
    bullets[1][i].shapesize(0.4)
    bullets[1][i].setposition(bulletbox2[i])
    bullets[1][i].showturtle()
ph1=turtle.Turtle()
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
ph1.write("Player1\n Health",font=style2,align="Center",)
ph1.goto(-250,50)
ph1.write(health1,font=style1,align="Center",)
ph2=turtle.Turtle()
ph2.hideturtle()
ph2.penup()
ph2.goto(250,100)
ph2.pencolor('Yellow')
ph2.write("Player2\n Health",font=style2,align="Center",)
ph2.goto(250,50)
ph2.write(health2,font=style1,align="Center",)
def Findposition(e):
    f,g=e.pos()
    fg=(round(f),round(g))
    return(fg)
def Amove():
    apos=Findposition(player1)
    global a,allowed,health2,turn_rt,turn_lt
    for ele in range(5) :
        if allowed[0][ele]==1:
            wait1=True
        if allowed[0][ele] :
            bapos=Findposition(bullets[0][ele])
            if (200>bapos[0]>-200) and (200>bapos[1]>-200):
                bullets[0][ele].fd(10)
                allowed[0][ele]=allowed[0][ele]+1
            elif allowed[0][ele]<=100 :
                bullets[0][ele].hideturtle()
                allowed[0][ele]=allowed[0][ele]+1
            else:
                allowed[0][ele]=0
                bullets[0][ele].setposition(bulletbox1[ele])
                bullets[0][ele].showturtle()
            wait1=False
            bpos=Findposition(player2)
            if -10<(bpos[0]-bapos[0])<10 and -10<(bpos[1]-bapos[1])<10 :
                player2.fillcolor("Red")
                health2=health2-15
                bullets[0][ele].fd(30)
                player2.fillcolor('Yellow')
    if a and (200>apos[0]>-200) and (200>apos[1]>-200):
        player1.fd(10)
    elif(apos[0]>=200)or(apos[0]<=-200)or(apos[1]>=200)or(apos[1]<=-200):
        player1.backward(10)
    elif turn_rt==True:
        player1.rt(9)
    elif turn_lt==True:
        player1.lt(9)
    
def Bmove():
    bpos=Findposition(player2)
    global b,allowed,health1,turnrt,turnlt
    for ele in range(5) :
        if allowed[1][ele]==1 :
            wait2=True
        if allowed[1][ele]:
            bbpos=Findposition(bullets[1][ele])
            if (200>bbpos[0]>-200) and (200>bbpos[1]>-200):
                bullets[1][ele].fd(10)
                allowed[1][ele]=allowed[1][ele]+1
            elif allowed[1][ele]<=100 :
                allowed[1][ele]=allowed[1][ele]+1
                bullets[1][ele].hideturtle()
            else:
                allowed[1][ele]=0
                bullets[1][ele].setposition(bulletbox2[ele])
                bullets[1][ele].showturtle()
            wait2=False
            apos=Findposition(player1)
            if -10<(apos[0]-bbpos[0])<10 and -10<(apos[1]-bbpos[1])<10 :
                player1.fillcolor("Red")
                health1=health1-15
                bullets[1][ele].fd(30)
                player1.fillcolor('Blue')
    if b and (200>bpos[0]>-200) and (200>bpos[1]>-200):
        player2.fd(10)
    elif(bpos[0]>=200)or(bpos[0]<=-200)or(bpos[1]>=200)or(bpos[1]<=-200):
        player2.backward(10)
    elif turnrt==True:
        player2.rt(9)
    elif turnlt==True:
        player2.lt(9)
def allow_Amove():
    global a
    a=True
def stop_Amove():
    global a
    a=False
def allow_Bmove():
    global b
    b=True
def stop_Bmove():
    global b
    b=False
def Turn1_right():
    global turn_rt
    turn_rt=True
def Turn1_left():
    global turn_lt
    turn_lt=True
def stop_rturn1():
    global turn_rt
    turn_rt=False
def stop_lturn1():
    global turn_lt
    turn_lt=False
def Turn2_right():
    global turnrt
    turnrt=True
def Turn2_left():
    global turnlt
    turnlt=True
def stop_rturn2():
    global turnrt
    turnrt=False
def stop_lturn2():
    global turnlt
    turnlt=False
def bullet1():
    global a1,allowed
    if allowed[0][a1]==0 and wait1==False:
        SetPosition(bullets[0][a1],Findposition(player1))
        bullets[0][a1].setheading(player1.heading())
        allowed[0][a1]=1
        if a1==4:
            a1=0
        else:
            a1=a1+1
def bullet2():
    global b1,allowed
    if allowed[1][b1]==0 and wait2==False:
        SetPosition(bullets[1][b1],Findposition(player2))
        bullets[1][b1].setheading(player2.heading())
        allowed[1][b1]=1
        if b1==4:
            b1=0
        else:
            b1=b1+1

def check_intersect():
    global health1,health2,a,b
    apos=Findposition(player1)
    bpos=Findposition(player2)
    aaa=bpos[0]-apos[0]
    bbb=bpos[1]-apos[1]
    if -15<aaa<15 and -15<bbb<15:
        if a:
            player2.fillcolor("Red")
            player1.backward(25)
            health2=health2-10
            player2.fillcolor("Yellow")
        if b:
            player1.fillcolor("Red")
            player2.backward(25)
            health1=health2-10
            player1.fillcolor("Blue")
        if a and b :
            player1.fillcolor("Red")
            player2.fillcolor("Red")
            player1.backward(25)
            player2.backward(25)
            health1=health1-10
            health2=health2-10
            player1.fillcolor('Blue')
            player2.fillcolor('Yellow')
a=b=bulletA=bulletB=wait1=wait2=turn_rt=turn_lt=turnrt=turnlt=False
b1=a1=0
control.onkeypress(lambda:allow_Amove(),'Up')
control.onkeyrelease(stop_Amove,'Up')
control.onkeypress(lambda:Turn1_right(),'Right')
control.onkeyrelease(stop_rturn1,'Right')
control.onkeypress(lambda:Turn1_left(),'Left')
control.onkeyrelease(stop_lturn1,'Left')
control.onkeypress(lambda: allow_Bmove(),'d')
control.onkeyrelease(stop_Bmove,'d')
control.onkeypress(lambda:Turn2_right(),'c')
control.onkeyrelease(stop_rturn2,'c')
control.onkeypress(lambda:Turn2_left(),'z')
control.onkeyrelease(stop_lturn2,'z')
control.onkey(bullet1,'Down')
control.onkey(bullet2,'x')
control.listen()
while True:
    Amove()
    Bmove()
    check_intersect()
    ph1.undo()
    ph1.write(health1,font=style1,align="Center",)
    ph2.undo()
    ph2.write(health2,font=style1,align="Center",)
    if health1<=0 or health2<=0:
        break
if health1<health2 :
    ph1.undo()
    ph1.write("LOST",font=style1,align="Center",)
    ph2.undo()
    ph2.write("WON",font=style1,align="Center",)
else :
    ph1.undo()
    ph1.write("WON",font=style1,align="Center",)
    ph2.undo()
    ph2.write("LOST",font=style1,align="Center",)
        
    
