import turtle
wn = turtle.Screen()
wn.setup(width=400, height=400)
red = turtle.Turtle() # 
pen = turtle.Turtle()
def curve(): #  draw curve
    for i in range(200): # 
        red.right(1)
        red.forward(1)

def heart():  # full Heart
    red.fillcolor('red')
    red.begin_fill()
    red.left(140)
    red.forward(113)
    curve() # Left Curve
    red.left(120)
    curve() # Right Curve
    red.forward(112)
    red.end_fill()

def txt():
  
    # 
    pen.up()
  
    # position
    pen.setpos(-77, 101)
  
    # ground
    pen.down()
  
    # black text
    pen.color('black')
  
    #
    # 
    pen.write("I love you Angela <3", font=(
      "Verdana", 12, "bold"))

heart()
txt()
red.ht() # Hiding Turtle
turtle.done()

