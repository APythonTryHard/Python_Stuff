import turtle

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Simple Animation with Turtle")

# Create a turtle
t = turtle.Turtle()
t.shape("turtle")
t.speed(0)

# Define vibrant pink color
vibrant_pink = (1.0, 0.08, 0.58)  # RGB values normalized to the range [0, 1]
t.color(vibrant_pink)

# Disable animation updates
turtle.tracer(0, 0)

# Animation function
def animate():
    for i in range(600):
        t.circle(10 + i, 180)
        t.right(91)
        # Update the screen every 100 iterations for better performance
        if i % 10 == 0:
            turtle.update()

# Run the animation
animate()

# Enable updates again
turtle.update()

# Keep the window open
turtle.done()
