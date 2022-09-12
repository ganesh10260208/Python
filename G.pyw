import turtle
import random
import tkinter
noofp=turtle.Screen()
noofp.setup(400,300)
position=[(-200,320),(-200,210),(-200,100),(-200,-10),(-200,-120),(-200,-230),(-570,320),(-570,210),(-570,100),(-570,-10),(-570,-120),(-570,-230)]
style1=('Lucida Sans Unicode',15,"italic")
styl1=('Lucida Sans Unicode',13)
style2=('Lucida Sans Unicode',15,"bold")
style3=('Lucida Sans Unicode',50,"bold")
names=[]
numpos=[]
num90=[]
def takeinput(kj): 
    number=int(noofp.textinput("1_of_12","Enter No.of Players"))
    if number not in range(2,13):
        takeinput(6) 
    else :
        return number
number=takeinput(6)
for A0 in range(number):
    tdg="Name of player-",str(A0+1)
    name=noofp.textinput("1_of_12",tdg)
    names.append(name)
    num90.append([])
for A7 in range(90):
    numpos.append([])

screen=turtle.Screen()
screen.setup(width = 1.0, height = 1.0)
form=turtle.Turtle()
form.hideturtle()
form.speed(10)
def Places():
    r1=[10,11,12,13,14,15,16,17,18]
    r2=[20,21,22,23,24,25,26,27,28]
    r3=[30,31,32,33,34,35,36,37,38]
    r4=[0,1,2,3,4,5,6,7,8]
    random.shuffle(r4)
    r5=[r1[r4[0]],r2[r4[1]],r3[r4[2]],r1[r4[3]],r2[r4[3]],r2[r4[4]],r3[r4[4]],r3[r4[5]],r1[r4[5]],r1[r4[6]],r2[r4[6]],r2[r4[7]],r3[r4[7]],r3[r4[8]],r1[r4[8]]]            
    return(r5)        
def Ninety():
    global numpos 
    form.penup()
    X,Y=150,0
    for A in range(9):
        for B in range(10):
            form.goto(X+(B*50),Y-(A*35))
            form.write((B*1)+1+(A*10),align='left',font=style2)
            numpos[(B*1)+(A*10)].append([X+(B*50),Y-(A*35)+12])
def Create(person,pos,i):
    ticknum=[[1,2,3,4,5,6,7,8,9],[10,11,12,13,14,15,16,17,18,19],[20,21,22,23,24,25,26,27,28,29],[30,31,32,33,34,35,36,37,38,39],[40,41,42,43,44,45,46,47,48,49],[50,51,52,53,54,55,56,57,58,59],[60,61,62,63,64,65,66,67,68,69],[70,71,72,73,74,75,76,77,78,79],[80,81,82,83,84,85,86,87,88,89,90]]
    form.goto(pos)
    form.write(names[i],align='center',font=style2)
    form.pendown()
    form.setheading(360)
    form.fd(270)
    form.rt(90)
    form.fd(30)
    form.rt(90)
    form.fd(270)
    form.lt(90)
    form.fd(30)
    form.lt(90)
    form.fd(270)
    form.rt(90)
    form.fd(30)
    form.rt(90)
    form.fd(270)
    form.rt(90)
    for j in range(4):
        form.fd(90)
        form.rt(90)
        form.fd(30)
        form.rt(90)
        form.fd(90)
        form.lt(90)
        form.fd(30)
        form.lt(90)
    form.fd(90)
    form.rt(90)
    form.fd(30)
    form.rt(90)
    form.fd(90)
    #numbers
    form.penup()
    g=Places()
    for A1 in range(3):
        line=[]
        for B1 in range(9):
            C1=(B1*1)+((A1+1)*10)
            if C1 in g:
                form.goto(pos[0]+(B1*30),pos[1]-(A1*30)-25)
                D1=random.choice(ticknum[B1])
                numpos[D1-1].append([pos[0]+(B1*30),pos[1]-(A1*30)-13])
                form.write(D1,font=style1,align='left')
                line.append(D1)
                ticknum[B1].remove(D1)
        num90[i].append(line)
                
Ninety()
colors=["blue","slate grey","orange","green","crimson","dodger blue","indigo","violet","purple","dark green","dark goldenrod","brown"]
for i in range(number):
    x=random.choice(colors)
    form.pencolor(x)
    Create(names[i],position[i],i)
    colors.remove(x)
N=[x for x in range(1,91)]
Dispaly=turtle.Turtle()
Dispaly.hideturtle()
Dispaly.pencolor("brown")
Dispaly.penup()
Dispaly.goto(200,100)
Pr=turtle.Turtle()
Pr.pencolor("brown")
Pr.hideturtle()
Pr.penup()
Pr.goto(200,180)
Pr2=turtle.Turtle()
Pr2.hideturtle()
Pr2.penup()
Pr2.goto(200,200)
Pr2.pencolor("brown")
Pr2.write(names[0],font=styl1,align='center')
Pr.write("Press_G_to_roll",font=styl1,align='center')
Pr.pencolor("blue")
def Turn():
    global ganesh,lavanya,game,pry
    if ganesh==True :
        ganesh=False
        dis=random.choice(N)
        Dispaly.clear()
        Dispaly.write(dis,align='Center',font=style3)
        for i in range(len(numpos[dis-1])):
            form.goto(numpos[dis-1][i])
            form.pendown()
            form.setheading(360)
            form.fd(25)
            form.penup()
        for A26 in range(len(names)):
            for A27 in range(3):
                for A28 in (num90[A26][A27]):
                    if dis==A28:
                        num90[A26][A27].remove(dis)
                        jl=len(num90[A26][0])+len(num90[A26][1])+len(num90[A26][2])
                        if (game[0]==0):
                            if((jl)==10):
                                Pr.goto(300,pry)
                                msg=str(names[A26])+" won First Five by"+str(dis)
                                Pr.write(msg,align='left',font=styl1)
                                ff[0]=1
                                pry=pry-30
                        if (game[1]==0):
                            if (len(num90[A26][0])==0):
                                Pr.goto(300,pry)
                                msg=str(names[A26])+" won Upper Line by "+str(dis)
                                Pr.write(msg,align='left',font=styl1)
                                ff[1]=1
                                pry=pry-30
                        if (game[2]==0):
                            if (len(num90[A26][1])==0):
                                Pr.goto(300,pry)
                                msg=str(names[A26])+" won Middle line by "+str(dis)
                                Pr.write(msg,align='left',font=styl1)
                                ff[2]=1
                                pry=pry-30
                        if (game[3]==0):
                            if (len(num90[A26][2])==0):
                                Pr.goto(300,pry)
                                msg=str(names[A26])+" won Lower line by "+str(dis)
                                Pr.write(msg,align='left',font=styl1)
                                ff[3]=1
                                pry=pry-30
                        if (game[4]==0):
                            if(jl==0):
                                Pr.goto(300,pry)
                                msg=str(names[A26])+" won The Game by "+str(dis)
                                Pr.write(msg,align='left',font=styl1)
                                lavanya=91
                                ff[4]=1
                                ry=pry-30
                        for marvel in range(5):
                            if ff[marvel]==1:
                                game[marvel]=1
        Pr2.clear()
        Pr2.write(names[(lavanya%len(names))],align='center',font=styl1)
        N.remove(dis)
        if lavanya<91:
            lavanya=lavanya+1
            ganesh=True
form.pencolor("Red")
form.pensize(4)
screen.onkey(Turn,"g")
ff=[0,0,0,0,0]
lavanya=1
pry=250
ganesh=True
game=[0,0,0,0,0]
screen.listen()

turtle.mainloop()
