import turtle

turtle.setup(600, 600)  # Determine the window size
window = turtle.Screen()  # Get a reference to the window
window.title("Handling keypresses!")  # Change the window title
window.bgcolor("lightgreen")  # Set the window background color

tess = turtle.Turtle()  # Create the 1st turtle
tess.color("purple")
tess.pensize(3)
tess.shape("circle")

alex = turtle.Turtle()  # Create the 2nd turtle
alex.color("blue")
alex.pensize(5)
alex.shape("circle")

alex.forward(100)


# The next functions are our "event handlers".
def h1():
  tess.forward(30)


def h2():
  tess.left(45)


def h3():
  tess.right(45)


def h4():
  window.bye()  # Close down the turtle window


def h5(x, y):
  tess.goto(x, y)


def onTimerHandler():
  tess.forward(100)
  tess.left(56)
  window.ontimer(onTimerHandler,
                 2000)  # timer activates the handler every 2 seconds


def hTess(x, y):
  tess.left(42)
  tess.forward(30)


def hAlex(x, y):
  alex.right(84)
  alex.forward(50)


# These lines "wire up" keypresses to the handlers we've defined
window.onkey(h1, "Up")
window.onkey(h2, "Left")
window.onkey(h3, "Right")
window.onkey(h4, "q")

# These lines "wire up" mouse clicks to the handlers we've defined
window.onclick(h5)
tess.onclick(hTess)
alex.onclick(hAlex)

# Now we need to tell the window to start listening for events,
# If any of the keys that we're monitoring is pressed, its handler will be called.
window.listen()
onTimerHandler()
window.mainloop()
