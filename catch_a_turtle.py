# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl

import random as rand






#-----game configuration----
wn = trtl.Screen()

#spot variables
spot_size = 2
spot_color = "pink"
spot_shape = "circle"
#score variables
global score
score = 0
font_setup = ("Arial", 20, "normal")
#timer variables
timer = 30
counter_interval = 1000
timer_up = False
#color list
colors = ['red','orange','yellow','green','blue','purple','pink','black']
#size list
size = [0.5, 1.5, 2, 4, 6, 8, 10, 12, 14]


#-----initialize turtle-----
count = trtl.Turtle()
scorewriter = trtl.Turtle()
spot = trtl.Turtle()
spot.shape(spot_shape)
spot.shapesize(spot_size)
spot.fillcolor(spot_color)
spot.color(spot_color)
wn.bgcolor("bisque")



#-----game functions--------
def start_game():
   global timer_up 
   timer_up = False





def change_color():
  new_color = rand.choice(colors)
  spot.color(new_color)

def change_size():
  new_size = rand.choice(size)
  spot.shapesize(new_size)

  

def update_score():
  global score
  score = score + 1
  scorewriter.clear()
  scorewriter.write(score, font=font_setup)

def change_position():
  spot.hideturtle()
  new_xpos = rand.randint(-200,200)
  new_ypos = rand.randint(-150,150)
  spot.goto(new_xpos,new_ypos)
  spot.showturtle()


def countdown():
  global timer, timer_up
  count.clear()
  if timer <= 0:
    count.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    count.write("Timer: " + str(timer), font =font_setup)
    timer -= 1
    count.getscreen().ontimer(countdown, counter_interval)


def spot_clicked(x,y):
  global timer_up
  if timer_up == False:
    update_score()
    change_color()
    change_size() 
    change_position()
  else:
    spot.hideturtle()


#-----events----------------
start_game()

count.hideturtle()
count.penup()
count.goto(250,250)
count.pendown()

wn.ontimer(countdown, counter_interval)

scorewriter.hideturtle()
scorewriter.penup()
scorewriter.goto(-300,250)
scorewriter.pendown()

spot.penup()
spot.onclick(spot_clicked)






wn.mainloop()