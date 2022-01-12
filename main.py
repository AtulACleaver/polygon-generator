import turtle
draw = turtle.Turtle()

num_of_sides = int(input("Number of sides in a polygon: "))

# sum of angles = (num_of_sides − 2) × 180
# sum of each angle = [(num_of_sides − 2) × 180]/num_of_sides
# Opposite of each angle = 180 of each angle

sum_of_each_angles = 180 - (((num_of_sides - 2) * 180)/num_of_sides)

# Without using +1 with num_of_sides I don't overlap with the first line
for i in range(num_of_sides):
    draw.forward(80)
    draw.left(sum_of_each_angles)

turtle.done()
