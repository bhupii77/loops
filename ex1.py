from turtle import*   # 'from turtle import' is for brings object from the module 

for i in range (4):
    fd(100)
    lt(90)
    

#stairs 
speed ('slowest')
bgcolor('red')
pensize(5)
goto(-300,-300)
for i in range (3):      #range(stop)
    fd (100)
    lt (90)
    fd (100)
    rt (90)



speed ('slowest')
for i in range (7):
     fd (80)
     lt(360/7)

     

hideturtle()  #removing arrow 
mainloop()  #keeps the window open      