import sys
from os import path
if(path.exists('input.txt')):
    sys.stdin = open("input.txt","r")
    sys.stdout = open("output.txt","w")
import math
for t in range(int(input())):
    n = int(input())
    x_axis_cordinates = dict()
    y_axis_cordinates = dict()
    for i in range(4*n-1):
        X1, Y1 = tuple(map(int, input().split()))
        x_axis_cordinates[X1] = x_axis_cordinates.get(X1,0) + 1
        y_axis_cordinates[Y1] = y_axis_cordinates.get(Y1,0) + 1
    for keys1,values in x_axis_cordinates.items():
        if (values%2!=0):
            a1_answer=keys1
            break
    for keys1, values in y_axis_cordinates.items():
        if (values%2!=0):
            b1_answer=keys1
            break
    print(a1_answer, b1_answer)