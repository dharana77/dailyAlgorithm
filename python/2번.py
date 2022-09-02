import math
import os
import random
import re
import sys

  

#
# Complete the 'findPoint' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY lines as parameter.
#

  

def calc_dis(x, y, line):
    x1 = line[0]
    y1 = line[1]
    x2 = line[2]
    y2 = line[3]
    area = abs((x1-x) * (y2-y) - (y1-y) * (x2 - x))
    AB = ((x1-x2)**2 + (y1-y2)**2) **0.5
    dis= area/AB

    if (x >= x1 and x <= x2) or (y >= y1 and y <= y2):
        return dis

    return min( ((x1-x)**2 + (y1-y)**2), ((x2-x)**2 + (y1-y1)**2))

def findPoint(lines):
    # Write your code here
    # find integer point p
    mn_x = 0
    mn_y = 0
    mx_x = 0
    mx_y = 0

    for line in lines:
        x1 = line[0]
        y1 = line[1]
        x2 = line[2]
        y2 = line[3]
        if mn_x > x1:
            mn_x = x1
        if mx_x < x1:
            mx_x = x1
        if mn_y > y1:
            mn_y = y1
        if mx_y < y1:
            mx_y = y1
        if mn_x > x2:
            mn_x = x2
        if mx_x < x2:
            mx_x = x2
        if mn_y > y2:
            mn_y = y2
        if mx_y < y2:
            mx_y = y2
    ans_x = -1
    ans_y = -1
    temp = 1e9

    for x in range(mn_x, mx_x+1):
        for y in range(mn_y, mx_y+1):
            total = 0
            for line in lines:
                test = calc_dis(x, y, line)
                print("dist", test)
                total += test
                if(total < temp):
                    temp = total
            ans_x = x
            ans_y = y
            print("total", total, ans_x, ans_y)
            ans = []
            chk = False


    for x in range(mn_x, mx_x+1):
        for y in range(mn_y, mx_y+1):
            total = 0
            for line in lines:
                test = calc_dis(x, y, line)
                total += test
            if(test == temp):
                ans.append(x)
                ans.append(y)
                chk = True
                break

        if chk:
            break

    return ans

  

