from turtle import*

bgcolor('green')
pencolor('blue')

speed('slow')
move = 5 
while True :

  for i in range(6):
    fd(100+move)
    #rt(60)
    for i in range (6):
        fd(50)
        rt(60)
        rt(60)

    rt(60)
    move += 5     

hideturtle()
mainloop()