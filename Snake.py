import turtle
import sys
import tkinter
import time
import random
import os.path
from os import path
turtle.title("Ganesh_Snake_20/20")
style1=('Lucida Sans Unicode',20,"bold",)
style2=('Lucida Sans Unicode',10,"italic")
style3=('Lucida Sans Unicode',10,"bold")
turtle.bgcolor("Grey")
Navigation=turtle.Screen()
Playzone=[(x,y)for x in range(-180,200,20) for y in range(-180,200,20)]
Sketch=turtle.Turtle()
Border=[]
Sketch.hideturtle()
Sketch.speed(10)
Sketch.penup()
Sketch.goto(0,240)
Sketch.pencolor("Yellow")
Sketch.write("SNAKE",font=style1,align="Center",)
Sketch.goto(-150,210)
Sketch.pencolor("Brown")
Sketch.write("Score :",font=style2,align="Right",)
Sketch.goto(0,225)
Sketch.write("High Score :",font=style2,align="Right",)
Sketch.goto(0,210)
Sketch.write("Eggs_Eaten :",font=style2,align="Right",)
Sketch.goto(150,210)
Sketch.write("Speed :",font=style2,align="Right",)
Sketch.goto(-200,-269)
Sketch.write("1,2,3,4\t\t:\tSpeed Controls\nArrow_keys\t:\tDirection Controls\nR\t\t:\tRestart_Game\nP\t\t:\tPause/Resume_Game",font=style3,align="Left",)
Sketch.goto(-200,200)
Sketch.pendown()
Sketch.pencolor("Black")
Sketch.pensize(5)
#Creating Border
for a in range(4):
    for b in range(20):
        Sketch.fd(20)
        c,d=Sketch.pos()
        cd=(round(c),round(d))
        Border.append(cd)
    Sketch.rt(90)
Sketch.penup()
Gover=turtle.Turtle()
Gover.hideturtle()
def Game_Pause():
    global paused
    if paused==True:
        paused=False
    else:
        paused=True
def Turnup():
    global s
    if(Snakehead.heading()!=270)and(Game==0)and(s==0):
        s=1
        Snakehead.setheading(90)
def TurnDown():
    global s
    if(Snakehead.heading()!=90)and(Game==0)and(s==0):
        s=1
        Snakehead.setheading(270)
def TurnRight():
    global s
    if(Snakehead.heading()!=180)and(Game==0)and(s==0):
        s=1
        Snakehead.setheading(360)
def TurnLeft():
    global s
    if(Snakehead.heading()!=0)and(Game==0)and(s==0):
        s=1
        Snakehead.setheading(180)
def Speed1():
    global t
    t=0.3
    Speed.undo()
    Speed.write("Slow",font=style3,align="Left",)
def Speed2():
    global t
    t=0.15
    Speed.undo()
    Speed.write("Normal",font=style3,align="Left",)
def Speed3():
    global t
    t=0.06
    Speed.undo()
    Speed.write("Fast",font=style3,align="Left",)
def Speed4():
    global t
    t=0.02
    Speed.undo()
    Speed.write("Fastest",font=style3,align="Left",)    
def Findposition(e):
    f,g=e.pos()
    fg=(round(f),round(g))
    return(fg)
def Setposition(l,m):
    l.hideturtle()
    l.setpos(m)
    l.showturtle()
def Eatenegg(j,EC):
    global snake,Snakebody,Tail,Game,Eggcount,t,score,k,Speed,Score,Eggs_Eaten,Snakehead,Egg,s
    if EC==0:
        n=0
    else:
        n=j
    Snakebody.insert(j,turtle.Turtle())
    Snakebody[n].speed(10)
    Snakebody[n].penup()
    Setposition(Snakebody[n],k)
    Snakebody[n].shape("square")
    Snakebody[n].shapesize(0.65)
    Snakebody[n].fillcolor("Red")    
    if t==0.02:
        score=score+20
    elif t==0.06:
        score=score+15
    elif t==0.15:
        score=score+10
    else :
        score=score+5
    Eggs_Eaten.undo()
    Eggs_Eaten.write(EC+1,font=style3,align="Left",)
    Score.undo()
    Score.write(score,font=style3,align="Left",)
    Setposition(Egg,(random.choice([p for p in Playzone if p not in snake and p!= k])))
    Snakehead.fd(20)
    time.sleep(t)
    s=0    
def Play_Game():
    global paused,HighScore,highscore,snake,Snakebody,Tail,Game,Eggcount,t,score,k,Speed,Score,Eggs_Eaten,Snakehead,Egg,s
    if path.exists(r"C:\Users\Public\Snakefile.txt")==True:
        file=open(r'C:\Users\Public\Snakefile.txt','r')
        highscore=int(file.read())
        file.close()
    else:
        highscore=0
    snake=[]
    Snakebody=[]
    Tail=Game=0
    EggCount=0
    s=0
    t=0.15
    score=0
    paused=False
    HighScore=turtle.Turtle()
    HighScore.speed(10)
    HighScore.hideturtle()
    HighScore.penup()
    HighScore.pencolor("White")
    Speed=turtle.Turtle()
    Speed.speed(10)
    Speed.hideturtle()
    Speed.penup()
    Score=turtle.Turtle()
    Score.speed(10)
    Score.hideturtle()
    Score.penup()
    Eggs_Eaten=turtle.Turtle()
    Eggs_Eaten.speed(10)
    Eggs_Eaten.hideturtle()
    Eggs_Eaten.penup()
    Score.pencolor("White")
    Eggs_Eaten.pencolor("White")
    Speed.pencolor("White")
    Score.goto(-150,210)
    Score.write("0",font=style3,align="Left",)
    Eggs_Eaten.goto(0,210)
    Eggs_Eaten.write("0",font=style3,align="Left",)
    HighScore.goto(0,225)
    HighScore.write(highscore,font=style3,align="Left",)
    Speed.goto(150,210)
    Speed.write("Normal",font=style3,align="Left",)
    Snakehead=turtle.Turtle()
    Snakehead.speed(10)
    Snakehead.penup()      
    Snakehead.shape("square")
    Snakehead.shapesize(0.85)
    Snakehead.fillcolor("Red")
    Egg=turtle.Turtle()
    Egg.speed(10)
    Egg.penup()
    Egg.shape("circle")
    Egg.shapesize(0.6)
    Egg.fillcolor("Blue")
    while Game==0 :

        if not paused:
            k=Findposition(Snakehead)
            if ( k in Border) or (k in snake):
                Game_Over()
            elif k==(Findposition(Egg)):
                Eatenegg(Tail+1,EggCount)
                EggCount=EggCount+1
            else :
                snake.remove(Findposition(Snakebody[Tail]))
                Setposition(Snakebody[Tail],k)
                Snakehead.fd(20)
                time.sleep(t)
                    
                s=0
                if Tail==0:
                    Tail=(len(Snakebody)-1)
                else:
                    Tail=Tail-1  
            snake.append(k)
        else:
            Navigation.update()
def Game_Over():
    global Game
    Gover.write("   Game_Over\nPress R to restart",font=style1,align="Center")
    if score>highscore:
        gfile=open(r'C:\Users\Public\Snakefile.txt','w+')
        gfile.write(str(score))
        gfile.close()
    Hide(Snakehead)
    Game=1    
def Restart_Game():
    Hide(Snakehead)
    Hide(Egg)
    Speed.clear()
    Score.clear()
    Eggs_Eaten.clear()
    HighScore.clear()
    for q in Snakebody:
        q.hideturtle()
    Snakebody.clear()
    Gover.clear()
    Play_Game()
def Hide(r):
    r.clear()
    r.hideturtle()
    
Navigation.onkey(Turnup,"Up")
Navigation.onkey(TurnDown,"Down")
Navigation.onkey(TurnRight,"Right")
Navigation.onkey(TurnLeft,"Left")
Navigation.onkey(Restart_Game,"r")
Navigation.onkey(Game_Pause,"p")
Navigation.onkey(Speed1,"1")
Navigation.onkey(Speed2,"2")
Navigation.onkey(Speed3,"3")
Navigation.onkey(Speed4,"4")
Navigation.listen()     
Play_Game()
turtle.mainloop()

