def calc_h_cost(current, target):
    return 3 * (abs(target[0] - current[0]) + abs(target[1] - current[1]))