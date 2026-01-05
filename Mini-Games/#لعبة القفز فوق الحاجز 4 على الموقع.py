#لعبة القفز فوق الحاجز 4 على الموقع
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    if front_is_clear():
        while wall_on_right():
            if front_is_clear():
                move()
            else:
                turn_left()
        turn_right()
        move()
        turn_right()
while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()
          