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
    a = b ** 2
    b = 2 * a * math.cos(c)
    answer = (a ** 2 - b ** 2)
    return answer

def toRadians():
    pass

def solution(quadAnswer):
    if quadAnswer(0) < 0:
        quadAnswer.remove(0)

solutAnswer = quadAnswer
return solutAnswer

def quadratic(a,b,c):
    x = (b ** 2) - (4*a*c)
    y = (b ** 2) + (4*a*c)
    quadAnswer = [x,y]
    quadAnswer.sort()
return quadAnswer

