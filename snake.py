"""
Modificado por: 
Eduardo Aguilar Chías
Alison Daniela Nava Bravo
Líder: Eduardo Aguilar
Colaborador: Alison Daniela Nava 
""" 

from turtle import *
from random import *
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    # Determina el color de la serpiente y la comida
    crayola = ["cyan", "purple", "yellow", "blue", "green", "pink", "orange", "gold", "silver","beige", "spring green"]
    colorSnake = choice(crayola)
    colorComida = choice(crayola)
    if colorSnake == colorComida:
        colorComida = choice(crayola)
        
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, "magenta")
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, colorSnake)

    square(food.x, food.y, 9, colorComida)
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()

#Determina la dirección de la serpiente
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()

