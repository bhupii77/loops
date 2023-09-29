from turtle import *

speed ('slow')
bgcolor('black')
pencolor('red')
    
for i in range (0,100,5):        #range(start,stop,step) , range(start,stop)
    fd(i)
    lt(360/4)
    write (i)

'''goto(-95,-95)
for p in range (5):
      fd(60)
      lt(90)'''

#hideturtle()
mainloop()
                        