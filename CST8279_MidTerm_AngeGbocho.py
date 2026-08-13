# Mid Term Python Project
# Course: CST8279
# Student: Ange Gbocho
#
# This program uses functions to draw shapes in the terminal


# Function to draw a square
def draw_square(size):
    # Check that the value is an integer
    if not isinstance(size, int):
        print("Error: The size must be an integer.")
        return

    # Check that the value is greater than zero
    if size <= 0:
        print("Error: The size must be greater than 0.")
        return

    # Draw the square
    for _ in range(size):
        print("* " * size)


# Function to draw a rectangle
def draw_rectangle(width, height):
    # Check that both values are integers
    if not isinstance(width, int) or not isinstance(height, int):
        print("Error: Width and height must be integers.")
        return

    # Check that both values are greater than zero
    if width <= 0 or height <= 0:
        print("Error: Width and height must be greater than 0.")
        return

    # Draw the rectangle
    for _ in range(height):
        print("* " * width)


# Class used to draw shapes in the terminal
class TerminalScribe:

    # Draw a square
    def draw_square(self, size):
        draw_square(size)


# Test the functions
print("Square:")
draw_square(7)

print("\nRectangle:")
draw_rectangle(8, 4)

print("\nSquare using TerminalScribe:")
scribe = TerminalScribe()
scribe.draw_square(5)