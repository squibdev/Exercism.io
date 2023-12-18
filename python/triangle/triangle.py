def equilateral(sides):
    return sides[0] == sides[1] == sides[2]

def isosceles(sides):
    return sides[0] == sides[1] or sides[0] == sides[2] if not(sides[1] == sides[2]) else False

def scalene(sides):
    return sides[0] != sides[1] != sides[2]