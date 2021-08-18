# find the smallest number such that it is a mutliple of 1 through to 20
def smallest_multiple_solution():
    # sufficient to only check these numbers, remember, work backwards instead of forwards
    checklist = [20, 19, 18, 17, 16, 14, 13, 11]
    count = 0
    step = 20
    while count != 8:
        # refresh count
        count = 0
        for item in checklist:
            if step % item == 0:
                count += 1
        if count == 8:
            print(step)
            break
        step = step + 20  # i can skip by 20 becase it must be divisible by 20


smallest_multiple_solution()
