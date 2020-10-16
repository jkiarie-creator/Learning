def speed_check(speed):
    speed_limit = 70
    demerit_points = 0
    if speed > speed_limit in range(70, 150, 5):
        demerit_points += (speed - speed_limit)/5
        print(f"Points:{demerit_points} ")
    if demerit_points > 12:
        print("License suspended!")
    return
