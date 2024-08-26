# -*- coding: utf-8 -*- #

from AriaPy import *
from pep_run_version import *
import sys
import enum
import pythoncom
import pyHook
import threading
import csv

# use to decide whether or not to continue the program
# 1 continue run , 0 stop
# key "Q" can stop program and collect data
flag = 1


def onKeyboardEvent(event):
    global flag
    # 监听键盘事件
    print "MessageName:", event.MessageName
    print "Ascii:", event.Ascii, chr(event.Ascii)
    print "Key:", event.Key
    print "KeyID:", event.KeyID
    if event.Key == "Q":
        flag = 0
    # 同鼠标事件监听函数的返回值
    return True


def control_Stop():
    # 创建一个“钩子”管理对象
    hm = pyHook.HookManager()
    # 监听所有键盘事件
    hm.KeyDown = onKeyboardEvent
    # 设置键盘“钩子”
    hm.HookKeyboard()
    # 进入循环，如不手动关闭，程序将一直处于监听状态
    pythoncom.PumpMessages()


# -----main function-----

# create thread for listening keyboardEvent
t1 = threading.Thread(target=control_Stop)
t1.setDaemon(True)
t1.start()

# init robot
Aria_init()
parser = ArArgumentParser(sys.argv)
parser.loadDefaultArguments()
robot = ArRobot()
con = ArRobotConnector(parser, robot)
if not Aria_parseArgs():
    Aria_logOptions()
    Aria_exit(1)

if not con.connectRobot():
    print "Could not connect to robot, exiting"
    Aria_exit(1)
robot.runAsync(1)
sonar = ArSonarDevice()
robot.addRangeDevice(sonar)
# import membrane
# step by step simulation
step = False

# nr of simulation steps
nrSteps = 2 # -2 == undefined, -1 == unlimited

robot.enableMotors()
# use for collecting data
sheet = []

while flag:
    start = time.clock()
    system = readInputFile("./ew.pep")
    numSonar = robot.getNumSonar()
    sonarReading = []
    # collect one group data
    one_sheet = []
    for i in range(0, numSonar):
        sonarReading.append(robot.getSonarReading(i).getRange())
        if sonarReading[i] > 1000:
            sonarReading[i] = 1000
        # store 16 sonar datas
        one_sheet.append('%d' % sonarReading[i])
        sonarReading[i] = -1 * sonarReading[i] + 1000

    ######################################设置参数#############################################
    s_Dist = max(sonarReading[0], sonarReading[7])  # 左墙s0，右墙s7
    ref_Dist = 700
    k_Dist = -0.1 if s_Dist == sonarReading[0] else 0.1
    s_Avoid = sonarReading[3] if s_Dist == sonarReading[0] else sonarReading[4]
    s_Fw = sonarReading[2] if s_Dist == sonarReading[0] else sonarReading[5]
    s_Bw = sonarReading[13] if s_Dist == sonarReading[0] else sonarReading[10]
    k_Heading = -0.5 if s_Dist == sonarReading[0] else 0.5
    alpha = 1.25
    gamma = 0.75
    ##########################################################################################

    # membrane input
    #  sonar value
    for p_object in system.variables:
        if p_object.name == 'S1':
            system.variables[system.variables.index(p_object)].value = sonarReading[0]
        if p_object.name == 'S2':
            system.variables[system.variables.index(p_object)].value = sonarReading[1]
        if p_object.name == 'S3':
            system.variables[system.variables.index(p_object)].value = sonarReading[2]
        if p_object.name == 'S4':
            system.variables[system.variables.index(p_object)].value = sonarReading[3]
        if p_object.name == 'S5':
            system.variables[system.variables.index(p_object)].value = sonarReading[4]
        if p_object.name == 'S6':
            system.variables[system.variables.index(p_object)].value = sonarReading[5]
        if p_object.name == 'S7':
            system.variables[system.variables.index(p_object)].value = sonarReading[6]
        if p_object.name == 'S8':
            system.variables[system.variables.index(p_object)].value = sonarReading[7]
        if p_object.name == 'S9':
            system.variables[system.variables.index(p_object)].value = sonarReading[8]
        if p_object.name == 'S10':
            system.variables[system.variables.index(p_object)].value = sonarReading[9]
        if p_object.name == 'S11':
            system.variables[system.variables.index(p_object)].value = sonarReading[10]
        if p_object.name == 'S12':
            system.variables[system.variables.index(p_object)].value = sonarReading[11]
        if p_object.name == 'S13':
            system.variables[system.variables.index(p_object)].value = sonarReading[12]
        if p_object.name == 'S14':
            system.variables[system.variables.index(p_object)].value = sonarReading[13]
        if p_object.name == 'S15':
            system.variables[system.variables.index(p_object)].value = sonarReading[14]
        if p_object.name == 'S16':
            system.variables[system.variables.index(p_object)].value = sonarReading[15]
        # cruise speed
        #  if p_object.name == 'cruiseSpeedLeft':
        #      system.variables[system.variables.index(p_object)].value = 500
        #  if p_object.name == 'cruiseSpeedRight':
        #      system.variables[system.variables.index(p_object)].value = 500
        if p_object.name == 'CruiseSpeed':
            system.variables[system.variables.index(p_object)].value = 420
        if p_object.name == 'xf':
                system.variables[system.variables.index(p_object)].value = 1


        ##########################################################################################
        # 设置pep文件里用到的参数
        if p_object.name == 's_Dist':
            system.variables[system.variables.index(p_object)].value = s_Dist
        if p_object.name == 'ref_Dist':
            system.variables[system.variables.index(p_object)].value = ref_Dist
        if p_object.name == 'k_Dist':
            system.variables[system.variables.index(p_object)].value = k_Dist
        if p_object.name == 's_Avoid':
            system.variables[system.variables.index(p_object)].value = s_Avoid
        if p_object.name == 's_Fw':
            system.variables[system.variables.index(p_object)].value = s_Fw
        if p_object.name == 's_Bw':
            system.variables[system.variables.index(p_object)].value = s_Bw
        # if p_object.name == 'k_Heading':
            # system.variables[system.variables.index(p_object)].value = k_Heading
        if p_object.name == 'alpha':
            system.variables[system.variables.index(p_object)].value = alpha
        if p_object.name == 'gamma':
            system.variables[system.variables.index(p_object)].value = gamma
        if p_object.name == 'a':
            system.variables[system.variables.index(p_object)].value = a
        if p_object.name == 'C0':
            system.variables[system.variables.index(p_object)].value = C0

    ##########################################################################################

    # start membrane simulate
    system.simulate(stepByStepConfirm=step, maxSteps=nrSteps)

    # get speed value
    for p_object in system.variables:
        if p_object.name == 'Spl':
            leftSpeed = p_object.value
        if p_object.name == 'Spr':
            rightSpeed = p_object.value

        # if p_object.name == 'cruisespeedleft':
        #     cruisespeedleft = p_object.value
        # if p_object.name == 'cruisespeedright':
        #     cruisespeedright = p_object.value
        if p_object.name == 'cruiseSpeed':
            cruiseSpeed = p_object.value
        if p_object.name == 'SD':
            SD = p_object.value
        if p_object.name == 'XC':
            XC = p_object.value
        if p_object.name == 'XH':
            XH = p_object.value

    for p_object in system.enzymes:
        # if p_object.name == 'e0':
        #     e0 = p_object.value
        if p_object.name == 'e1':
            e1 = p_object.value
        if p_object.name == 'e2':
            e2 = p_object.value
        if p_object.name == 'e3':
            e3 = p_object.value


    # add leftSpeed and rightSpeed
    one_sheet.append('%f' % leftSpeed)
    one_sheet.append('%f' % rightSpeed)

    # print 'leftSpeed:%d'%leftSpeed
    # print 'rightSpeed:%d'%rightSpeed
    robot.lock()

    robot_leftSpeed = robot.getLeftVel()
    robot_rightSpeed = robot.getRightVel()
    robot_trans_speed = robot.getVel()
    robot_rot_speed = robot.getRotVel()

    robot.setVel2(leftSpeed, rightSpeed)
    robot.unlock()
    ArUtil_sleep(50)

    # store robot true speed
    one_sheet.append('%f' % robot_leftSpeed)
    one_sheet.append('%f' % robot_rightSpeed)
    one_sheet.append('%f' % robot_trans_speed)
    one_sheet.append('%f' % robot_rot_speed)

    ##    print 'robot_leftSpeed:%d'%robot_leftSpeed
    ##    print 'robot_rightSpeed:%d'%robot_rightSpeed
    ##    print 'robot_trans_speed:%d'%robot_trans_speed
    ##    print 'robot_rot_speed:%d'%robot_rot_speed

    end = time.clock()
    print("----------------------------")
    # print end - start
    print "leftSpeed:%d | rightSpeed:%d"%(leftSpeed,rightSpeed)
    print "XC:%d |XH:%d" % (XC, XH)
    #print "k_Heading:%d % (k_Heading)

   #print "SD:%d" % (SD)
    # print "cruisespeedleft:%d | cruisespeedright:%d"%(cruisespeedleft,cruisespeedright)
    # print " e1=%d e2=%d e3=%d cruiseSpeed=%d SWL_temp=%d SWR_temp=%d"%(e1,e2,e3,cruiseSpeed,SWL_temp,SWR_temp)
    # print
    # add time data
    one_sheet.append('%f' % (end - start))
    sheet.append(one_sheet)
# write data
writeFileObj = open('ew10.csv', 'w')
writer = csv.writer(writeFileObj)
for row in sheet:
    writer.writerow(row)
writeFileObj.close()

Aria_exit(0)

