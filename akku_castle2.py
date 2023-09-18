from turtle import *
dis=[300,180,300,180]
ngl=[90,90,90,90]

for d,a in zip(dis,ngl):
    fd(d)
    lt(a)

dis=[100,300,100,120]
ngl=[90,90,90,90]

for d,a in zip(dis,ngl):
    bk(d)
    rt(a)
penup()
goto(300,0)
pendown()

dis=[100,300,100,120]
ngl=[90,90,90,90]

for d,a in zip(dis,ngl):
    fd(d)
    lt(a)


dis=[45,50,30,50]
ngl=[90,90,90,90]

for d,a in zip(dis,ngl):
    bk(d)
    rt(a)
dis=[90,50,30,50]
ngl=[90,90,90,90]

for d,a in zip(dis,ngl):
    bk(d)
    rt(a)
dis=[90,50,30,50]
ngl=[90,90,90,90]

for d,a in zip(dis,ngl):
    bk(d)
    rt(a)
dis=[90,50,30,50]
ngl=[90,90,90,90]

for d,a in zip(dis,ngl):
    bk(d)
    rt(a)
dis=[90,50,30,50]
ngl=[90,90,90,90]

for d,a in zip(dis,ngl):
    bk(d)
    rt(a)

penup()
goto(240,0)
pendown()

dis=[100,180,100,0]
ngl=[90,90,90,90]

for d,a in zip(dis,ngl):
    lt(a)
    fd(d)
penup()
goto(400,0)

penup()
goto(0,300)
pendown()
dis=[0,58,58]
ngl=[90,60,60]

for d,a in zip(dis,ngl):
    lt(a)
    fd(d)

penup()
goto(300,0)
goto(-100,0)
goto(395,0)
goto(300,300)
pendown()
dis=[0,58,58]
ngl=[90,90,60]

for d,a in zip(dis,ngl):
    rt(a)
    fd(d)

hideturtle()
mainloop()