def make_bricks(small, big, goal):
    floor = goal // 5  # 8 // 5 == 1
    if big < floor:
        floor = big
    goal = goal - (floor * 5)  # 8 - (1 * 5) == 3
    return goal <= small
