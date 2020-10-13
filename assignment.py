#! python3

import math

def tempConversion(degrees,unit="C"):
    if unit == "C":
        answer = (degrees * 9/5) + 32
    if unit == "F":
        answer = (degrees - 32) * 5/9

    answer = round(answer,1)
    return answer

def factorPair(a,b):
    c = a / b
    answer = [int(b),int(c)]
    answer.sort()
    return answer

def cosineLaw(a,b,c,oppositeSide=True):
    c = toRadians(c)
    if oppositeSide == True:
        # trying to find opposite side
        ans2 = (a ** 2) + (b ** 2) - 2 * a * b * math.cos(c)
        s = math.sqrt(ans2)
        return s
    else:
        # trying to find adjacent side
        sides = [a,b,c]
        sides.sort()
        if a > b:
            a1 = 1
            b1 = 2 * (a) * (math.cos(c))
            c1 = (a ** 2)-(b ** 2)
            s = quadratic(a1,b1,c1)
            return s
        if b > a:
            a1 = 1
            b1 = 2 * (b) * (math.cos(c))
            c1 = (b ** 2)-(a ** 2)
            s = quadratic(a1,b1,c1)
            return s


def toRadians(degrees):
    degrees = float(degrees)
    rad = ((degrees * math.pi) / 180)
    return rad

def solution(quadAnswer):
    quadAnswer.sort()
    solanswer = quadAnswer[1]
    return solanswer

def quadratic(a,b,c):
    x1 = (-b + math.sqrt((b ** 2) - 4 * a * c)) / (2 * a)
    x2 = (-b - math.sqrt((b ** 2) - 4 * a * c)) / (2 * a)
    quadAnswer = [x1,x2]
    quadAnswer.sort()
    return quadAnswer



