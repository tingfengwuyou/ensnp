# -*- coding: utf-8 -*- #

from pep_run_version import *
import sys
# import enum
# import pythoncom
# import pyHook
import threading
import csv

step = False
# nr of simulation steps
nrSteps = 1

# -----main function-----
flag = 1
# 输入数组
# 0.872 0.00 0.516 1.0 0.0 1.0 0.0 0.0 0.909 1.0 1.0 0.0 1.0 0.600 0.250 1.0 0.0 0.717 0.692 0.875 1.0 0.688
# 0.0 0.781 0.0 0.455 0.779 0.788 00.437 0.600 0.0 0.515 0.231 0.990 0.0 0.0 0.0 0.0 0.647 0.0 0.462 0.438 0.0 0.625
# 0.939 1.0 1.0 0.818 1.0 0.515 0.844 1.0 0.545 0.557 0.154 1.0 0.0 1.0 0.500 0.667 0.706 0.229 0.615 0.688 0.017 0.875
# 1.0 0.192 0.718 0.727 0.421 0.0 1.0 0.80 1.0 0.850 0.846 0.875 0.333 0.80 1.0 0.833 1.0 1.0 1.0 1.0 0.671 1.0
# D = input("输入数据，以空格隔开：")
D = '1.0 0.192 '
D = D.split(' ')
for i in range(0,2):
    D[i]=float(D[i])
# print D
while flag:
    start = time.time()
    system = readInputFile("./test.pep")
    ##########################################################################################
    # 设置pep文件里用到的参数
    for p_object in system.variables:
        if p_object.name == 'b':
            system.variables[system.variables.index(p_object)].value = D[0]
        if p_object.name == 'c':
            system.variables[system.variables.index(p_object)].value = D[1]
        if p_object.name == 'd':
            system.variables[system.variables.index(p_object)].value = D[1]
    # start membrane simulate
    system.simulate(stepByStepConfirm=step, maxSteps=nrSteps)

    # get speed value
    A ,D,b2,b3= 0,0,0,0

    for p_object in system.variables:
        if p_object.name == 'a':
            A = p_object.value
        if p_object.name == 'd':
            D = p_object.value
        if p_object.name == 'x':
            X = p_object.value
        if p_object.name == 'y':
            Y = p_object.value
    end = time.time()
    print("----------------------------")
    # print end - start
    print ("A:")
    print(A)
    print ("D:")
    print(D)
    print ("X:")
    print(X)
    print("Y:")
    print(Y)
    print(end-start)
    flag = 0

