from turtle import*

'''fd(100)
lt(90)
fd(100)
lt(90)
fd(100)
lt(90)
fd(100)
lt(90)'''

#stairs 
speed ('slowest')
goto(-300,-300)
for i in range (5):
    fd (100)
    lt (90)
    fd (100)
    rt (90)
hideturtle()  #removing arrow 
mainloop()  #keeps the window open 


'''speed ('slowest')
for i in range (7):
     fd (80)
     lt(360/7)'''