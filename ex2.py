from turtle import *

speed ('fastest')
bgcolor('black')
pencolor('red')

for i in range (1,1000,5):
    fd(i)
    lt(360/4)
    write (i)


hideturtle()
mainloop()
                        