
 #lag en sirkel i python  ut av firkanter
 #my first .py 
 


import turtle

x = turtle.Turtle()
x.speed(0)
x.color("red")

def square_circle(length,angle):
  


        for i in range (4):  
            x.forward(length)
            x.right(angle)
           
 

for i in range(100):    #hvor mange ganger en frikant skal bli tegnet opp 
    square_circle(100,90)
    x.right(11) # 360 kan ikke deles på 11 fordi 11 er et primtall, derfor vil ikke frikant stoppe å bli tegnet opp
                        # En sirkel har kun 360 grader for at sirkelen skal kunne bli tegenet opp i evig tid må vi dele på et primtall
   
