def steps(number):

    if number < 1:
        raise ValueError("Only positive integers are allowed")
    if number == 1:
        return 0
    else:
        counter = 0
        while number != 1:
            counter += 1
            if number % 2 == 0:
                number = number / 2
            else:
                number = number * 3 + 1
        return counter

#def steps(num: int, count=0):
#    if num <1:
#        raise ValueError("Only positive integers are allowed")
#    return count if num==1 else steps(3*num+1 if num %2 else num//2, count+1)
