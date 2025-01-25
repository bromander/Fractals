import turtle as t

window_width = 1910
window_height = 1080
t.setup(width=window_width, height=window_height)

def sierpinski(size, iteration, colorofpen, coloroffill):
    t.fillcolor(coloroffill)
    t.pencolor(colorofpen)
    t.penup()
    if iteration == 0:
        t.begin_fill()
        t.pendown()
    for i in range(0, 3):
        if iteration > 0:
            sierpinski(size / 2, iteration - 1, colorofpen, coloroffill)
        t.forward(size)
        t.left(120)
    if iteration == 0:
        t.penup()
        t.end_fill()


t.speed(1000)

edge_size = 500
window = t.Screen()


t.penup()
t.goto(-edge_size / 2, -3 ** 0.5 / 4 * edge_size)


coloroffill, colorofpen = 'black', 'purple'

sierpinski(edge_size, 3, coloroffill, colorofpen)

window.exitonclick()