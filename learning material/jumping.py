jump = False
if jump is True:
    y -= vel_y
    vel_y -= 1
    if vel_y < -10:
        jump = False
        vel_y = 10