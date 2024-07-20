import random
import time
import turtle

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Simple Animation with Turtle")

# Create a turtle
t = turtle.Turtle()
t.shape("turtle")
t.speed(0)

turtle.tracer(0, 0)

# Function to get a random color
def random_color():
    return (random.random(), random.random(), random.random())

# Animation function
def animate():
    for i in range(600):
        t.color(random_color())
        t.forward(1000*(i/500))
        t.right(91)
        if i % 10 == 0:
            turtle.update()
        #     t.clear()
        # time.sleep(0.01)


# Run the animation
animate()

# Keep the window open
turtle.done()
