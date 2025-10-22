import turtle
import threading
import subprocess
import time
import pyautogui

def draw_smiley():
    turtle.TurtleScreen._RUNNING = True
    screen = turtle.Screen()
    screen.clear()
    screen.title("Smiley Face")
    screen.bgcolor("white")

    pen = turtle.Turtle()
    pen.speed(5)

    # Draw face (Yellow Circle)
    pen.up()
    pen.goto(0, -100)
    pen.down()
    pen.color("black", "yellow")
    pen.begin_fill()
    pen.circle(100)
    pen.end_fill()

    # Draw left eye (Black)
    pen.up()
    pen.goto(-35, 50)
    pen.down()
    pen.color("black", "black")
    pen.begin_fill()
    pen.circle(10)
    pen.end_fill()

    # Draw right eye (Black)
    pen.up()
    pen.goto(35, 50)
    pen.down()
    pen.begin_fill()
    pen.circle(10)
    pen.end_fill()

    # Draw smile (Red)
    pen.up()
    pen.goto(-40, 20)
    pen.setheading(-60)
    pen.down()
    pen.color("red")
    pen.width(5)
    pen.circle(40, 120)

    # Write text under the smiley
    pen.up()
    pen.goto(-35, -130)
    pen.color("blue")
    pen.write("Keep Smiling! 😊", font=("Arial", 18, "bold"))

    pen.hideturtle()
    
    time.sleep(3)

    # Open Notepad and type a message
    subprocess.Popen(["notepad.exe"])
    time.sleep(2)
    pyautogui.typewrite("Thank you for drawing a smiley! 😊", interval=0.1)

    # Automatically close the turtle window after 3 seconds
    time.sleep(3)
    screen.bye()

def execute_smiley():
    draw_smiley()
