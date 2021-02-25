def is_armstrong_number(number):

    arm = 0
    num_len = len(str(number))
    
    for i in str(number):
        arm += int(i) ** num_len

    print(number)
    print(arm)

    if number == arm:
        return True
    else:
        return False