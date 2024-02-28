from turtle import Turtle,Screen
import turtle
import random

HEIGHT=600
WIDTH=600


offsets = {
    "up":(0,20),
    "down":(0,-20),
    "left":(-20,0),
    "right":(20,0),
}


def game_reset():
    global score,food_pos,snake,snake_direction,delay
    score = 0
    delay=400
    snake = [[0,0],[20,0],[40,0],[60,0]]
    snake_direction = "up"
    food_pos = get_random_food_pos()
    food.goto(food_pos)

    game_loop()

def game_loop():
    stamper.clearstamps()
    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]

    if new_head in snake or new_head[0] < -WIDTH /2 or new_head[0] > WIDTH / 2 or new_head[1] < -HEIGHT /2 or new_head[1] > HEIGHT / 2:
        game_reset()

    else:
        snake.append(new_head)
        if not food_collision():
            snake.pop(0)
        
        for segment in snake:
            stamper.goto(segment[0],segment[1])
            stamper.stamp()
        
        screen.title(titlestring=f"Snake Game Score: {score}")
        screen.update()
        turtle.ontimer(game_loop,delay)

def food_collision():
    global food_pos,score,delay
    if get_distance(snake[-1],food_pos) < 20:
        food_pos = get_random_food_pos()
        food.goto(food_pos)
        score += 1
        delay=int(0.9 * delay)
        return True
    return False

def get_distance(pos1,pos2):
    x1,y1 = pos1
    x2,y2 = pos2
    distance = ((y2-y1)**2 + (x2-x1)**2)**0.5
    return distance


def get_random_food_pos():
    food_position_x = random.randint(-250,250)
    food_position_y = random.randint(-250,250)
    return (food_position_x,food_position_y)

def go_up():
    global snake_direction

    if snake_direction != "down":
        snake_direction = "up"

def go_down():
    global snake_direction

    if snake_direction != "up":
        snake_direction = "down"

def go_right():
    global snake_direction

    if snake_direction != "left":
        snake_direction = "right"

def go_left():
    global snake_direction

    if snake_direction != "right":
        snake_direction = "left"

screen = Screen()
screen.setup(width=WIDTH,height=HEIGHT)
screen.bgcolor("cyan")
screen.title(titlestring="Snake Game")
screen.tracer(0)

screen.listen()
screen.onkey(go_up,"Up")
screen.onkey(go_down,"Down")
screen.onkey(go_right,"Right")
screen.onkey(go_left,"Left")

stamper = Turtle()
stamper.shape("square")
stamper.penup()

food = Turtle()
food.shape("circle")
food.penup()

game_reset()

turtle.done()
