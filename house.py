from turtle import*


speed('slowest')
bgcolor('green')
pencolor('red')
pensize('5')
dis=[200,200,150,150,200,80]
ngl=[90,65,50,65,90,90]


for d, a in zip(dis,ngl):
   fd(d)
   lt(a)


penup()
goto(140,0)
pendown()

ngl=[90,90,90,90]
dis=[0,60,30,60]


for d,a in zip(dis,ngl):

   rt(a)
   fd(d)

hideturtle()
mainloop()   