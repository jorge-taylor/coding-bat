def make_chocolate(small, big, goal):
  floor = goal // 5
  if big < floor:
    floor = big
  goal = goal - 5 * floor
  
  if goal-small <= 0:
    return goal
  else:
    return -1