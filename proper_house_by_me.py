from turtle import *

speed('slow')
bgcolor('white')

dis=[140,120,80,80,120,240,120,80,100,80,100]
fig=[90,60,60,60,90,90,60,30,150,30,0]

for d,a in zip(dis,fig):
    fd(d)
    lt(a)

penup()
goto(80,0)
pendown()

dij=[0,50,20,50]
yib=[90,90,90,90]

for d,a in zip(dij,yib):
    fd(d)
    lt(a)

penup()
goto(165,70)
pendown()

dis=[50,30,50,30]
fij=[90,90,90,240]

for a,d in zip(dis,fij):
    fd(a)
    lt(d)



penup()
goto(220,120)
pendown()
    
dif = [80,20,80,20,80,20,80]
fij = [30,150,210,330,30,150,0]

for a,d in zip(dif,fij):
    fd(a)
    lt(d)


else:
     penup()
     goto(70,110)
     pendown()

     write("bhupii&akku house",align = 'center')


hideturtle()
mainloop()
