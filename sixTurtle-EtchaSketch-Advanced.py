import turtle

# Setup
t = turtle.Turtle()
screen = turtle.Screen()
t.speed(0)
t.pensize(2)

# Flags for movement
moving = {
    "up": False,
    "down": False,
    "left": False,
    "right": False
}

# Movement function
def move_loop():
    x, y = t.pos()
    half_w = screen.window_width() // 2
    half_h = screen.window_height() // 2
    step = 5

    if moving["up"] and y + step < half_h:
        t.setheading(90)
        t.forward(step)
    if moving["down"] and y - step > -half_h:
        t.setheading(270)
        t.forward(step)
    if moving["left"] and x - step > -half_w:
        t.setheading(180)
        t.forward(step)
    if moving["right"] and x + step < half_w:
        t.setheading(0)
        t.forward(step)

    screen.ontimer(move_loop, 50)

# Press functions
def start_move_up(): moving["up"] = True
def stop_move_up(): moving["up"] = False
def start_move_down(): moving["down"] = True
def stop_move_down(): moving["down"] = False
def start_move_left(): moving["left"] = True
def stop_move_left(): moving["left"] = False
def start_move_right(): moving["right"] = True
def stop_move_right(): moving["right"] = False

# Bind keys
screen.listen()
screen.onkeypress(start_move_up, "Up")
screen.onkeyrelease(stop_move_up, "Up")
screen.onkeypress(start_move_down, "Down")
screen.onkeyrelease(stop_move_down, "Down")
screen.onkeypress(start_move_left, "Left")
screen.onkeyrelease(stop_move_left, "Left")
screen.onkeypress(start_move_right, "Right")
screen.onkeyrelease(stop_move_right, "Right")

# Start moving loop
move_loop()
turtle.done()
