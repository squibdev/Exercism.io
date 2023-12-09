def classify(number):
    total = 0
    if number > 0 and type(number) == int:
        for i in range(1, number):
            if number % i == 0 and number != i and number > 0:
                total += i
            i += 1
        if number == total:
            return "perfect"
        elif number > total:
            return "deficient"
        elif number < total:
            return "abundant"
    else:
        raise ValueError('Invalid input')