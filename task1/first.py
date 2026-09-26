print('X | Y')

cur_x = -8
end_x = 10
while cur_x <= end_x:
    if cur_x <= -5:
        print(cur_x, -3)
    elif cur_x <= -3:
        print(cur_x, cur_x + 3)
    elif cur_x <= 3:
        print(cur_x, round((9 - cur_x ** 2) ** 0.5, 2))
    elif cur_x <= 8:
        print(cur_x, round(3 / 5 * (cur_x - 3), 2))
    else:
        print(cur_x, 3)
    cur_x += 1