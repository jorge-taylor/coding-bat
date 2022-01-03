def front_back(str):
    length = len(str)
    if length <= 1:
        return str
    mid = str[1:length-1]
    return str[length-1] + mid + str[0]
