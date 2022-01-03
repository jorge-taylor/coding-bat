def close_far(a, b, c):
    if abs(b-c) >= 2:
        if (abs(a-b) <= 1 and abs(a-c) > 1) or (abs(a-c) <= 1 and abs(a-b) > 1):
            return True
    return False
