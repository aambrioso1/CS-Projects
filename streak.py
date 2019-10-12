# Find the length of the longest streak of positive values in a list of numbers

gains1 = [2,-1,-1, 3, 4, 5, -1, -2, 1, 3]

def find_streak(gains):
    streak = 0
    max_streak = 0
    for gain in gains:
        if gain > 0:
            streak += 1
            continue
        else:
            if streak > max_streak:
                max_streak = streak
            streak = 0
    if streak > max_streak:
        max_streak = streak
    return max_streak
            
print(find_streak(gains1))          

    