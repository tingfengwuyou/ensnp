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
nrSteps = 4


# -----main function-----
flag = 1
# 输入数组
# 0.872 0.00 0.516 1.0 0.0 1.0 0.0 0.0 0.909 1.0 1.0 0.0 1.0 0.600 0.250 1.0 0.0 0.717 0.692 0.875 1.0 0.688
# 0.0 0.781 0.0 0.455 0.779 0.788 00.437 0.600 0.0 0.515 0.231 0.990 0.0 0.0 0.0 0.0 0.647 0.0 0.462 0.438 0.0 0.625
# 0.939 1.0 1.0 0.818 1.0 0.515 0.844 1.0 0.545 0.557 0.154 1.0 0.0 1.0 0.500 0.667 0.706 0.229 0.615 0.688 0.017 0.875
# 1.0 0.192 0.718 0.727 0.421 0.0 1.0 0.80 1.0 0.850 0.846 0.875 0.333 0.80 1.0 0.833 1.0 1.0 1.0 1.0 0.671 1.0
# 0.9 0.8 0.7 0.6 0.5 0.4 0.3 0.2 0.1 0.9 0.8 0.7 0.6 0.5 0.4 0.3 0.2 0.1 0.9 0.8 0.7 0.6
# D = input("输入数据，以空格隔开：")
D = '0.465 0.263 0.236 0.000 0.612 0.152 0.287 0.400 0.182 0.000 0.000 0.679 0.333 0.400 0.500 0.500 0.294 0.243 0.000 0.000 0.487 0.0'
D = D.split(' ')
for i in range(0,22):
    D[i]=float(D[i])
# print D
while flag:

    system = readInputFile("./human.pep")
    ##########################################################################################
    # 设置pep文件里用到的参数
    for p_object in system.variables:
        if p_object.name == 'd1':
            system.variables[system.variables.index(p_object)].value = D[0]
        if p_object.name == 'd2':
            system.variables[system.variables.index(p_object)].value = D[1]
        if p_object.name == 'd3':
            system.variables[system.variables.index(p_object)].value = D[2]
        if p_object.name == 'd4':
            system.variables[system.variables.index(p_object)].value = D[3]
        if p_object.name == 'd5':
            system.variables[system.variables.index(p_object)].value = D[4]
        if p_object.name == 'd6':
            system.variables[system.variables.index(p_object)].value = D[5]
        if p_object.name == 'd7':
            system.variables[system.variables.index(p_object)].value = D[6]
        if p_object.name == 'd8':
            system.variables[system.variables.index(p_object)].value = D[7]
        if p_object.name == 'd9':
            system.variables[system.variables.index(p_object)].value = D[8]
        if p_object.name == 'd10':
            system.variables[system.variables.index(p_object)].value = D[9]
        if p_object.name == 'd11':
            system.variables[system.variables.index(p_object)].value = D[10]
        if p_object.name == 'd12':
            system.variables[system.variables.index(p_object)].value = D[11]
        if p_object.name == 'd13':
            system.variables[system.variables.index(p_object)].value = D[12]
        if p_object.name == 'd14':
            system.variables[system.variables.index(p_object)].value = D[13]
        if p_object.name == 'd15':
            system.variables[system.variables.index(p_object)].value = D[14]
        if p_object.name == 'd16':
            system.variables[system.variables.index(p_object)].value = D[15]
        if p_object.name == 'd17':
            system.variables[system.variables.index(p_object)].value = D[16]
        if p_object.name == 'd18':
            system.variables[system.variables.index(p_object)].value = D[17]
        if p_object.name == 'd19':
            system.variables[system.variables.index(p_object)].value = D[18]
        if p_object.name == 'd20':
            system.variables[system.variables.index(p_object)].value = D[19]
        if p_object.name == 'd21':
            system.variables[system.variables.index(p_object)].value = D[20]
        if p_object.name == 'd22':
            system.variables[system.variables.index(p_object)].value = D[21]
    start = time.time()
    # start membrane simulate
    xx = 1
    while xx>0:
        system.simulate(stepByStepConfirm=step, maxSteps=nrSteps)
        xx -= 1
    end = time.time()
    # get speed value
    # A ,b1,b2,b3= 0,0,0,0
    # c1,c2,c3=0,0,0
    # d1,d2,d3,d4,d5,d6=0,0,0,0,0,0
    for p_object in system.variables:
        if p_object.name == 'a':
            A = p_object.value
        if p_object.name == 'b1':
            b1 = p_object.value
        if p_object.name == 'b2':
            b2 = p_object.value
        if p_object.name == 'b3':
            b3 = p_object.value
        if p_object.name == 'c1':
            c1 = p_object.value
        if p_object.name == 'c2':
            c2 = p_object.value
        if p_object.name == 'c3':
            c3 = p_object.value
        if p_object.name == 'c4':
            c4 = p_object.value
        if p_object.name == 'c5':
            c5 = p_object.value
        if p_object.name == 'c6':
            c6 = p_object.value
        if p_object.name == 'c7':
            c7 = p_object.value
        if p_object.name == 'x1':
            x1 = p_object.value
        if p_object.name == 'x2':
            x2 = p_object.value
        if p_object.name == 'x3':
            x3 = p_object.value
        if p_object.name == 'x4':
            x4 = p_object.value
        if p_object.name == 'x5':
            x5 = p_object.value
        if p_object.name == 'x6':
            x6 = p_object.value
        if p_object.name == 'x13':
            x13 = p_object.value
        if p_object.name == 'x14':
            x14 = p_object.value
        if p_object.name == 'x15':
            x15 = p_object.value
        if p_object.name == 'f':
            f = p_object.value

    print("----------------------------")
    # print end - start
    print ("A:"+str(A))
    print("b1:" + str(b1))
    print("b2:" + str(b2))
    print("b3:" + str(b3))
    print("c1:" + str(c1))
    print("c2:" + str(c2))
    print("c3:" + str(c3))
    print("c4:" + str(c4))
    print("c5:" + str(c5))
    print("c6:" + str(c6))
    print("c7:" + str(c7))
    print("x1:" + str(x1))
    print("x2:" + str(x2))
    print("x3:" + str(x3))
    print("x4:" + str(x4))
    print("x5:" + str(x5))
    print("x13:"+ str(x13))
    print("x14:" + str(x14))
    print("x15:" + str(x15))
    print ("cost time: "+str((end-start))+' s')
    flag = 0

