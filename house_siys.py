from turtle import *
dis=[200,200,150,150,190,175,70,80,70]
ngl=[90,72,40,68,90,90,90,90,90]
#our home

speed('slow')
bgcolor('yellow')
pencolor('brown')

pensize(3)
for d,a in zip(dis,ngl):
    forward(d)
    left(a)

hideturtle()
mainloop()