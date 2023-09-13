from turtle import *

speed ('fastest')
bgcolor('black')
pencolor('red')
pensize(3)

for i in range (100,0,-5):    # - is  for negative loop
    fd(i)
    lt(360/6)
    write (i)
    circle (i)


hideturtle()
mainloop()