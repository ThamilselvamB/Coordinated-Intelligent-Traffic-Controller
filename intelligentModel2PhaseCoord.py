
import sys
import os
import time
import string
import math
from os.path import expanduser
import numpy as np

prevCmdOutputFour = ('Options for the verification:\n  Generating no trace\n  Search order is breadth first\n  Using conservative space optimisation\n  Seed is 1571542488\n  State space representation uses minimal constraint systems\n\x1b[2K\nVerifying formula 1 at line 5\n -- Throughput: 123540 states/sec, Load: 100 iterations\x1b[K\n -- Throughput: 209962 states/sec, Load: 90 iterations\x1b[K\n -- Throughput: 198543 states/sec, Load: 73 iterations\x1b[K\n\x1b[2K -- Formula is satisfied.\n(1080 runs)\nLearning statistics for best strategy: \n\tNumber of resets: 1\n\tNumber of iterations in last reset: 3\n\tNumber of iterations in total: 15\n\n\x1b[2K\nVerifying formula 2 at line 7\n -- Throughput: 89 states/sec, Load: 1 runs\x1b[K\n -- Throughput: 146341 states/sec, Load: 1 runs\x1b[K\n\x1b[2K -- Formula is satisfied.\n2 * trafficLight_1.GREEN_A + 6 * trafficLight_1.YELLOW + 10 * trafficLight_1.GREEN_B:\n[0]: (0,0) (0,0) (0,10) (0,10) (5,10) (5,0) (5,10) (10,10) (10,0) (10,10) (15,10) (15,0) (15,0) (60,0) (60,0) (60,10) (60,10) (65,10) (65,0) (65,10) (70,10) (70,0) (70,0) (100,0) (100,0) (100,10) (100,10) (105,10) (105,0) (105,10) (110,10) (110,0) (110,0) (140,0) (140,0) (140,10) (140,10) (145,10) (145,0) (145,10) (150,10) (150,0) (150,0) (180,0) (180,0) (180,10) (180,10) (185,10) (185,0) (185,10) (190,10) (190,0) (190,0) (220,0) (220,0) (220,10) (220,10) (225,10) (225,0) (225,10) (230,10) (230,0) (230,0) (300,0)\n\x1b[2K\nVerifying formula 3 at line 8\n -- Throughput: 89 states/sec, Load: 1 runs\x1b[K\n -- Throughput: 150501 states/sec, Load: 1 runs\x1b[K\n\x1b[2K -- Formula is satisfied.\n2 * trafficLight_2.GREEN_A + 6 * trafficLight_2.YELLOW + 10 * trafficLight_2.GREEN_B:\n[0]: (0,0) (0,0) (15,0) (15,0) (15,10) (15,10) (20,10) (20,0) (20,10) (25,10) (25,0) (25,10) (30,10) (30,0) (30,0) (70,0) (70,0) (70,10) (70,10) (75,10) (75,0) (75,10) (80,10) (80,0) (80,0) (110,0) (110,0) (110,10) (110,10) (115,10) (115,0) (115,10) (120,10) (120,0) (120,0) (150,0) (150,0) (150,10) (150,10) (155,10) (155,0) (155,10) (160,10) (160,0) (160,0) (190,0) (190,0) (190,10) (190,10) (195,10) (195,0) (195,10) (200,10) (200,0) (200,0) (230,0) (230,0) (230,10) (230,10) (235,10) (235,0) (235,10) (240,10) (240,0) (240,0) (300,0)\n\x1b[2K\nVerifying formula 4 at line 9\n -- Throughput: 89 states/sec, Load: 1 runs\x1b[K\n -- Throughput: 151770 states/sec, Load: 1 runs\x1b[K\n\x1b[2K -- Formula is satisfied.\n2 * trafficLight_3.GREEN_A + 6 * trafficLight_3.YELLOW + 10 * trafficLight_3.GREEN_B:\n[0]: (0,0) (0,0) (30,0) (30,0) (30,10) (30,10) (35,10) (35,0) (35,10) (40,10) (40,0) (40,10) (45,10) (45,0) (45,0) (80,0) (80,0) (80,10) (80,10) (85,10) (85,0) (85,10) (90,10) (90,0) (90,0) (120,0) (120,0) (120,10) (120,10) (125,10) (125,0) (125,10) (130,10) (130,0) (130,0) (160,0) (160,0) (160,10) (160,10) (165,10) (165,0) (165,10) (170,10) (170,0) (170,0) (200,0) (200,0) (200,10) (200,10) (205,10) (205,0) (205,10) (210,10) (210,0) (210,0) (240,0) (240,0) (240,10) (240,10) (245,10) (245,0) (245,10) (250,10) (250,0) (250,0) (300,0)\n\x1b[2K\nVerifying formula 5 at line 10\n -- Throughput: 88 states/sec, Load: 1 runs\x1b[K\n -- Throughput: 158081 states/sec, Load: 1 runs\x1b[K\n\x1b[2K -- Formula is satisfied.\n2 * trafficLight_4.GREEN_A + 6 * trafficLight_4.YELLOW + 10 * trafficLight_4.GREEN_B:\n[0]: (0,0) (0,0) (45,0) (45,0) (45,2) (45,2) (50,2) (50,0) (50,2) (55,2) (55,0) (55,2) (60,2) (60,0) (60,0) (90,0) (90,0) (90,2) (90,2) (95,2) (95,0) (95,2) (100,2) (100,0) (100,0) (130,0) (130,0) (130,2) (130,2) (135,2) (135,0) (135,2) (140,2) (140,0) (140,0) (170,0) (170,0) (170,2) (170,2) (175,2) (175,0) (175,2) (180,2) (180,0) (180,0) (210,0) (210,0) (210,2) (210,2) (215,2) (215,0) (215,2) (220,2) (220,0) (220,0) (250,0) (250,0) (250,2) (250,2) (255,2) (255,0) (255,2) (260,2) (260,0) (260,0) (300,0)\n')
prevCmdOutputFive = ('Options for the verification:\n  Generating no trace\n  Search order is breadth first\n  Using conservative space optimisation\n  Seed is 1571542488\n  State space representation uses minimal constraint systems\n\x1b[2K\nVerifying formula 1 at line 5\n -- Throughput: 123540 states/sec, Load: 100 iterations\x1b[K\n -- Throughput: 209962 states/sec, Load: 90 iterations\x1b[K\n -- Throughput: 198543 states/sec, Load: 73 iterations\x1b[K\n\x1b[2K -- Formula is satisfied.\n(1080 runs)\nLearning statistics for best strategy: \n\tNumber of resets: 1\n\tNumber of iterations in last reset: 3\n\tNumber of iterations in total: 15\n\n\x1b[2K\nVerifying formula 2 at line 7\n -- Throughput: 89 states/sec, Load: 1 runs\x1b[K\n -- Throughput: 146341 states/sec, Load: 1 runs\x1b[K\n\x1b[2K -- Formula is satisfied.\n2 * trafficLight_1.GREEN_A + 6 * trafficLight_1.YELLOW + 10 * trafficLight_1.GREEN_B:\n[0]: (0,0) (0,0) (0,10) (0,10) (5,10) (5,0) (5,10) (10,10) (10,0) (10,10) (15,10) (15,0) (15,0) (60,0) (60,0) (60,10) (60,10) (65,10) (65,0) (65,10) (70,10) (70,0) (70,0) (100,0) (100,0) (100,10) (100,10) (105,10) (105,0) (105,10) (110,10) (110,0) (110,0) (140,0) (140,0) (140,10) (140,10) (145,10) (145,0) (145,10) (150,10) (150,0) (150,0) (180,0) (180,0) (180,10) (180,10) (185,10) (185,0) (185,10) (190,10) (190,0) (190,0) (220,0) (220,0) (220,10) (220,10) (225,10) (225,0) (225,10) (230,10) (230,0) (230,0) (300,0)\n\x1b[2K\nVerifying formula 3 at line 8\n -- Throughput: 89 states/sec, Load: 1 runs\x1b[K\n -- Throughput: 150501 states/sec, Load: 1 runs\x1b[K\n\x1b[2K -- Formula is satisfied.\n2 * trafficLight_2.GREEN_A + 6 * trafficLight_2.YELLOW + 10 * trafficLight_2.GREEN_B:\n[0]: (0,0) (0,0) (15,0) (15,0) (15,10) (15,10) (20,10) (20,0) (20,10) (25,10) (25,0) (25,10) (30,10) (30,0) (30,0) (70,0) (70,0) (70,10) (70,10) (75,10) (75,0) (75,10) (80,10) (80,0) (80,0) (110,0) (110,0) (110,10) (110,10) (115,10) (115,0) (115,10) (120,10) (120,0) (120,0) (150,0) (150,0) (150,10) (150,10) (155,10) (155,0) (155,10) (160,10) (160,0) (160,0) (190,0) (190,0) (190,10) (190,10) (195,10) (195,0) (195,10) (200,10) (200,0) (200,0) (230,0) (230,0) (230,10) (230,10) (235,10) (235,0) (235,10) (240,10) (240,0) (240,0) (300,0)\n\x1b[2K\nVerifying formula 4 at line 9\n -- Throughput: 89 states/sec, Load: 1 runs\x1b[K\n -- Throughput: 151770 states/sec, Load: 1 runs\x1b[K\n\x1b[2K -- Formula is satisfied.\n2 * trafficLight_3.GREEN_A + 6 * trafficLight_3.YELLOW + 10 * trafficLight_3.GREEN_B:\n[0]: (0,0) (0,0) (30,0) (30,0) (30,10) (30,10) (35,10) (35,0) (35,10) (40,10) (40,0) (40,10) (45,10) (45,0) (45,0) (80,0) (80,0) (80,10) (80,10) (85,10) (85,0) (85,10) (90,10) (90,0) (90,0) (120,0) (120,0) (120,10) (120,10) (125,10) (125,0) (125,10) (130,10) (130,0) (130,0) (160,0) (160,0) (160,10) (160,10) (165,10) (165,0) (165,10) (170,10) (170,0) (170,0) (200,0) (200,0) (200,10) (200,10) (205,10) (205,0) (205,10) (210,10) (210,0) (210,0) (240,0) (240,0) (240,10) (240,10) (245,10) (245,0) (245,10) (250,10) (250,0) (250,0) (300,0)\n\x1b[2K\nVerifying formula 5 at line 10\n -- Throughput: 88 states/sec, Load: 1 runs\x1b[K\n -- Throughput: 158081 states/sec, Load: 1 runs\x1b[K\n\x1b[2K -- Formula is satisfied.\n2 * trafficLight_4.GREEN_A + 6 * trafficLight_4.YELLOW + 10 * trafficLight_4.GREEN_B:\n[0]: (0,0) (0,0) (45,0) (45,0) (45,2) (45,2) (50,2) (50,0) (50,2) (55,2) (55,0) (55,2) (60,2) (60,0) (60,0) (90,0) (90,0) (90,2) (90,2) (95,2) (95,0) (95,2) (100,2) (100,0) (100,0) (130,0) (130,0) (130,2) (130,2) (135,2) (135,0) (135,2) (140,2) (140,0) (140,0) (170,0) (170,0) (170,2) (170,2) (175,2) (175,0) (175,2) (180,2) (180,0) (180,0) (210,0) (210,0) (210,2) (210,2) (215,2) (215,0) (215,2) (220,2) (220,0) (220,0) (250,0) (250,0) (250,2) (250,2) (255,2) (255,0) (255,2) (260,2) (260,0) (260,0) (300,0)\n')
prevCmdOutputTwo = ('Options for the verification:\n  Generating no trace\n  Search order is breadth first\n  Using conservative space optimisation\n  Seed is 1571642961\n  State space representation uses minimal constraint systems\n\x1b[2K\nVerifying formula 1 at line 5\n -- Throughput: 99702 states/sec, Load: 100 iterations\x1b[K\n -- Throughput: 184675 states/sec, Load: 94 iterations\x1b[K\n -- Throughput: 172843 states/sec, Load: 82 iterations\x1b[K\n -- Throughput: 168314 states/sec, Load: 71 iterations\x1b[K\n\x1b[2K -- Formula is satisfied.\n(990 runs)\nLearning statistics for best strategy: \n\tNumber of resets: 0\n\tNumber of iterations in last reset: 1\n\tNumber of iterations in total: 1\n\n\x1b[2K\nVerifying formula 2 at line 7\n -- Throughput: 67 states/sec, Load: 1 runs\x1b[K\n -- Throughput: 146868 states/sec, Load: 1 runs\x1b[K\n\x1b[2K -- Formula is satisfied.\n2 * trafficLight_1.GREEN_A + 6 * trafficLight_1.YELLOW + 10 * trafficLight_1.GREEN_B:\n[0]: (0,0) (0,0) (0,10) (0,10) (5,10) (5,0) (5,6) (10,6) (10,0) (10,2) (15,2) (15,0) (15,0) (75,0) (75,0) (75,2) (75,2) (80,2) (80,0) (80,2) (85,2) (85,0) (85,0) (125,0) (125,0) (125,2) (125,2) (130,2) (130,0) (130,2) (135,2) (135,0) (135,0) (175,0) (175,0) (175,2) (175,2) (180,2) (180,0) (180,2) (185,2) (185,0) (185,0) (225,0) (225,0) (225,2) (225,2) (230,2) (230,0) (230,2) (235,2) (235,0) (235,0) (275,0) (275,0) (275,2) (275,2) (280,2) (280,0) (280,2) (285,2) (285,0) (285,0) (400,0)\n\x1b[2K\nVerifying formula 3 at line 8\n -- Throughput: 67 states/sec, Load: 1 runs\x1b[K\n -- Throughput: 152808 states/sec, Load: 1 runs\x1b[K\n\x1b[2K -- Formula is satisfied.\n2 * trafficLight_2.GREEN_A + 6 * trafficLight_2.YELLOW + 10 * trafficLight_2.GREEN_B:\n[0]: (0,0) (0,0) (15,0) (15,0) (15,2) (15,2) (20,2) (20,0) (20,2) (25,2) (25,0) (25,2) (30,2) (30,0) (30,0) (85,0) (85,0) (85,2) (85,2) (90,2) (90,0) (90,2) (95,2) (95,0) (95,0) (135,0) (135,0) (135,2) (135,2) (140,2) (140,0) (140,2) (145,2) (145,0) (145,0) (185,0) (185,0) (185,2) (185,2) (190,2) (190,0) (190,2) (195,2) (195,0) (195,0) (235,0) (235,0) (235,2) (235,2) (240,2) (240,0) (240,2) (245,2) (245,0) (245,0) (285,0) (285,0) (285,2) (285,2) (290,2) (290,0) (290,2) (295,2) (295,0) (295,0) (400,0)\n\x1b[2K\nVerifying formula 4 at line 9\n -- Throughput: 67 states/sec, Load: 1 runs\x1b[K\n -- Throughput: 153846 states/sec, Load: 1 runs\x1b[K\n\x1b[2K -- Formula is satisfied.\n2 * trafficLight_3.GREEN_A + 6 * trafficLight_3.YELLOW + 10 * trafficLight_3.GREEN_B:\n[0]: (0,0) (0,0) (30,0) (30,0) (30,2) (30,2) (35,2) (35,0) (35,2) (40,2) (40,0) (40,2) (45,2) (45,0) (45,0) (95,0) (95,0) (95,2) (95,2) (100,2) (100,0) (100,2) (105,2) (105,0) (105,0) (145,0) (145,0) (145,2) (145,2) (150,2) (150,0) (150,2) (155,2) (155,0) (155,0) (195,0) (195,0) (195,2) (195,2) (200,2) (200,0) (200,2) (205,2) (205,0) (205,0) (245,0) (245,0) (245,2) (245,2) (250,2) (250,0) (250,2) (255,2) (255,0) (255,0) (295,0) (295,0) (295,2) (295,2) (300,2) (300,0) (300,2) (305,2) (305,0) (305,0) (400,0)\n\x1b[2K\nVerifying formula 5 at line 10\n -- Throughput: 67 states/sec, Load: 1 runs\x1b[K\n -- Throughput: 154195 states/sec, Load: 1 runs\x1b[K\n\x1b[2K -- Formula is satisfied.\n2 * trafficLight_4.GREEN_A + 6 * trafficLight_4.YELLOW + 10 * trafficLight_4.GREEN_B:\n[0]: (0,0) (0,0) (45,0) (45,0) (45,2) (45,2) (50,2) (50,0) (50,2) (55,2) (55,0) (55,2) (60,2) (60,0) (60,0) (105,0) (105,0) (105,2) (105,2) (110,2) (110,0) (110,2) (115,2) (115,0) (115,0) (155,0) (155,0) (155,2) (155,2) (160,2) (160,0) (160,2) (165,2) (165,0) (165,0) (205,0) (205,0) (205,2) (205,2) (210,2) (210,0) (210,2) (215,2) (215,0) (215,0) (255,0) (255,0) (255,2) (255,2) (260,2) (260,0) (260,2) (265,2) (265,0) (265,0) (305,0) (305,0) (305,2) (305,2) (310,2) (310,0) (310,2) (315,2) (315,0) (315,0) (400,0)\n\x1b[2K\nVerifying formula 6 at line 11\n -- Throughput: 67 states/sec, Load: 1 runs\x1b[K\n -- Throughput: 147505 states/sec, Load: 1 runs\x1b[K\n\x1b[2K -- Formula is satisfied.\n2 * trafficLight_5.GREEN_A + 6 * trafficLight_5.YELLOW + 10 * trafficLight_5.GREEN_B:\n[0]: (0,0) (0,0) (60,0) (60,0) (60,2) (60,2) (65,2) (65,0) (65,2) (70,2) (70,0) (70,2) (75,2) (75,0) (75,0) (115,0) (115,0) (115,2) (115,2) (120,2) (120,0) (120,2) (125,2) (125,0) (125,0) (165,0) (165,0) (165,2) (165,2) (170,2) (170,0) (170,2) (175,2) (175,0) (175,0) (215,0) (215,0) (215,2) (215,2) (220,2) (220,0) (220,2) (225,2) (225,0) (225,0) (265,0) (265,0) (265,2) (265,2) (270,2) (270,0) (270,2) (275,2) (275,0) (275,0) (315,0) (315,0) (315,2) (315,2) (320,2) (320,0) (320,2) (325,2) (325,0) (325,0) (400,0)\n')
home = expanduser("~")
rootDir = os.path.abspath(os.getcwd())
pathToModels = rootDir+"/models/"
experimentId = [4,5,44,55,2]

# define some parameters here
strategoTrafficLightModelFour = pathToModels + "CoordinationFour.xml"
strategoQueryFour = pathToModels + "CoordinationFour.q"
strategoTrafficLightModelFive = pathToModels + "CoordinationFive.xml"
strategoQueryFive = pathToModels + "CoordinationFive.q"
strategoTrafficLightModelFourFour = pathToModels + "CoordinationFourFour.xml"
strategoQueryFourFour = pathToModels + "CoordinationFour.q"
strategoTrafficLightModelFiveFive = pathToModels + "coordinationFiveFive.xml"
strategoQueryFiveFive = pathToModels + "CoordinationFive.q"
strategoTrafficLightModelTwo = pathToModels + "CoordinationTwo.xml"
strategoQueryTwo = pathToModels + "CoordinationTwo.q"

strategoLearningMet = "3"
strategoSuccRuns = "20" # 50
strategoGoodRuns = "20" # 50
strategoMaxRuns = "50" # 100
strategoEvalRuns = "10"
strategoMaxIterations = "100" # 200
def runStratego(get_stretego, args, query,coordinationSet):
    # print ('calling stratego with command: ' + com + args + query )
    start_time = time.time()
    f = os.popen(get_stretego+args+query)
    out = f.read()
    if (" Formula is NOT satisfied" or "\nOut of memory" )in out:
        print("No strategy now")
        if(coordinationSet == 4 or coordinationSet == 44):
            out = prevCmdOutputFour
        if (coordinationSet == 5 or coordinationSet == 55):
            out = prevCmdOutputFive
        if (coordinationSet == 2):
            out = prevCmdOutputTwo
    total_time = time.time() - start_time
    return total_time, out

def listToStringWithoutBrackets(list1):
    return str(list1).replace('[','').replace(']','')

def removeMoreYellow(phaseData):
    data1 = list(phaseData)
    firstIndex = 0
    # print("data original:", data1)
    count = 0
    for i in range(len(data1)):
        if data1[i] == 3:
            firstIndex = i
            break
    for i in range(firstIndex, len(data1)):
        if data1[i] == 3:
            count = count + 1
        if data1[i] != 3:
            break
    nextphase = data1[firstIndex + count + 1]
    if count > 5:
        for i in range(count - 4):
            data1.pop(firstIndex + count - i)
            data1.insert(firstIndex + count - i, nextphase)
    return np.asarray(data1)


def convertPhase(pythonToUppaal):
    phaseNow = 2
    if pythonToUppaal == 0:
        phaseNow = 1
    if pythonToUppaal == 2:
        phaseNow = 3
    if pythonToUppaal == 3:
        phaseNow = 2
    return [phaseNow]
def createModelFour(master_model, experimentId,areaJam,areaArriv,greenTimer,redTimer,maxB,maxA,prevPhase):
    fo = open(master_model, "r+")
    str_model = fo.read()
    fo.close()

    greenTimer1 = [greenTimer[0]]
    greenTimer2 = [greenTimer[1]]
    greenTimer3 = [greenTimer[2]]
    greenTimer4 = [greenTimer[3]]

    redTimer1 = [redTimer[0]]
    redTimer2 = [redTimer[1]]
    redTimer3 = [redTimer[2]]
    redTimer4 = [redTimer[3]]

    traffic_light1 = [1]
    traffic_light2 = [2]
    traffic_light3 = [3]
    traffic_light4 = [4]
    tfl_jammed_cars_1 = areaJam[0:4]
    tfl_jammed_cars_2 = areaJam[4:8]
    tfl_jammed_cars_3 = areaJam[8:12]
    tfl_jammed_cars_4 = areaJam[12:16]

    tfl_arrived_cars_1 = areaArriv[0:4]
    tfl_arrived_cars_2 = areaArriv[4:8]
    tfl_arrived_cars_3 = areaArriv[8:12]
    tfl_arrived_cars_4 = areaArriv[12:16]

    trf_max_A_1 = [maxA[0]]
    trf_max_A_2 = [maxA[1]]
    trf_max_A_3 = [maxA[2]]
    trf_max_A_4 = [maxA[3]]
    trf_max_B_1 = [maxB[0]]
    trf_max_B_2 = [maxB[1]]
    trf_max_B_3 = [maxB[2]]
    trf_max_B_4 = [maxB[3]]
    all_in_one_trf1 = str(traffic_light1 + tfl_jammed_cars_1 + tfl_arrived_cars_1 +  greenTimer1 + redTimer1+ trf_max_A_1 + trf_max_B_1 + convertPhase(prevPhase[0]))
    all_in_one_trf2 = str(traffic_light2 + tfl_jammed_cars_2 + tfl_arrived_cars_2 +  greenTimer2 + redTimer2+trf_max_A_2 + trf_max_B_2 + convertPhase(prevPhase[1]))
    all_in_one_trf3 = str(traffic_light3 + tfl_jammed_cars_3 + tfl_arrived_cars_3 +  greenTimer3 + redTimer3+trf_max_A_3 + trf_max_B_3 + convertPhase(prevPhase[2]))
    all_in_one_trf4 = str(traffic_light4 + tfl_jammed_cars_4 + tfl_arrived_cars_4 +  greenTimer4 + redTimer4+trf_max_A_4 + trf_max_B_4 + convertPhase(prevPhase[3]))

    toReplace = "//TRAFFIC_LIGHT_1"
    value = "trafficLight_1 = TL_model(" + listToStringWithoutBrackets(all_in_one_trf1) + ");"
    str_model = str.replace(str_model, toReplace, value, 1)

    toReplace = "//TRAFFIC_LIGHT_2"
    value = "trafficLight_2 = TL_model(" + listToStringWithoutBrackets(all_in_one_trf2) + ");"
    str_model = str.replace(str_model, toReplace, value, 1)

    toReplace = "//TRAFFIC_LIGHT_3"
    value = "trafficLight_3 = TL_model(" + listToStringWithoutBrackets(all_in_one_trf3) + ");"
    str_model = str.replace(str_model, toReplace, value, 1)

    toReplace = "//TRAFFIC_LIGHT_4"
    value = "trafficLight_4 = TL_model(" + listToStringWithoutBrackets(all_in_one_trf4) + ");"
    str_model = str.replace(str_model, toReplace, value, 1)

    modelName = pathToModels + "tl" + str(experimentId) + ".xml"
    text_file = open(modelName, "w")
    text_file.write(str_model)
    text_file.close()
    return modelName

def createModelFive(master_model, experimentId,areaJam,areaArriv,greenTimer,redTimer,maxB,maxA,prevPhase):
    fo = open(master_model, "r+")
    str_model = fo.read()
    fo.close()
    greenTimer1 = [greenTimer[4]]
    greenTimer2 = [greenTimer[5]]
    greenTimer3 = [greenTimer[6]]
    greenTimer4 = [greenTimer[7]]
    greenTimer5 = [greenTimer[8]]

    redTimer1 = [redTimer[4]]
    redTimer2 = [redTimer[5]]
    redTimer3 = [redTimer[6]]
    redTimer4 = [redTimer[7]]
    redTimer5 = [redTimer[8]]

    traffic_light1 = [1]
    traffic_light2 = [2]
    traffic_light3 = [3]
    traffic_light4 = [4]
    traffic_light5 = [5]
    tfl_jammed_cars_1 = areaJam[16:20]
    tfl_jammed_cars_2 = areaJam[20:24]
    tfl_jammed_cars_3 = areaJam[24:28]
    tfl_jammed_cars_4 = areaJam[28:32]
    tfl_jammed_cars_5 = areaJam[32:36]

    tfl_arrived_cars_1 = areaArriv[16:20]
    tfl_arrived_cars_2 = areaArriv[20:24]
    tfl_arrived_cars_3 = areaArriv[24:28]
    tfl_arrived_cars_4 = areaArriv[28:32]
    tfl_arrived_cars_5 = areaArriv[32:36]

    trf_max_A_1 = [maxA[4]]
    trf_max_A_2 = [maxA[5]]
    trf_max_A_3 = [maxA[6]]
    trf_max_A_4 = [maxA[7]]
    trf_max_A_5 = [maxA[8]]
    trf_max_B_1 = [maxB[4]]
    trf_max_B_2 = [maxB[5]]
    trf_max_B_3 = [maxB[6]]
    trf_max_B_4 = [maxB[7]]
    trf_max_B_5 = [maxB[8]]
    all_in_one_trf1 = str(
        traffic_light1 + tfl_jammed_cars_1 + tfl_arrived_cars_1 + greenTimer1 + redTimer1 + trf_max_A_1 + trf_max_B_1 + convertPhase(
            prevPhase[4]))
    all_in_one_trf2 = str(
        traffic_light2 + tfl_jammed_cars_2 + tfl_arrived_cars_2 + greenTimer2 + redTimer2 + trf_max_A_2 + trf_max_B_2 + convertPhase(
            prevPhase[5]))
    all_in_one_trf3 = str(
        traffic_light3 + tfl_jammed_cars_3 + tfl_arrived_cars_3 + greenTimer3 + redTimer3 + trf_max_A_3 + trf_max_B_3 + convertPhase(
            prevPhase[6]))
    all_in_one_trf4 = str(
        traffic_light4 + tfl_jammed_cars_4 + tfl_arrived_cars_4 + greenTimer4 + redTimer4 + trf_max_A_4 + trf_max_B_4 + convertPhase(
            prevPhase[7]))
    all_in_one_trf5 = str(
        traffic_light5 + tfl_jammed_cars_5 + tfl_arrived_cars_5 + greenTimer5 + redTimer5 + trf_max_A_5 + trf_max_B_5+
        convertPhase(prevPhase[8]))

    toReplace = "//TRAFFIC_LIGHT_1"
    value = "trafficLight_1 = TL_model(" + listToStringWithoutBrackets(all_in_one_trf1) + ");"
    str_model = str.replace(str_model, toReplace, value, 1)

    toReplace = "//TRAFFIC_LIGHT_2"
    value = "trafficLight_2 = TL_model(" + listToStringWithoutBrackets(all_in_one_trf2) + ");"
    str_model = str.replace(str_model, toReplace, value, 1)

    toReplace = "//TRAFFIC_LIGHT_3"
    value = "trafficLight_3 = TL_model(" + listToStringWithoutBrackets(all_in_one_trf3) + ");"
    str_model = str.replace(str_model, toReplace, value, 1)

    toReplace = "//TRAFFIC_LIGHT_4"
    value = "trafficLight_4 = TL_model(" + listToStringWithoutBrackets(all_in_one_trf4) + ");"
    str_model = str.replace(str_model, toReplace, value, 1)

    toReplace = "//TRAFFIC_LIGHT_5"
    value = "trafficLight_5 = TL_model(" + listToStringWithoutBrackets(all_in_one_trf5) + ");"
    str_model = str.replace(str_model, toReplace, value, 1)

    modelName = pathToModels + "tl" + str(experimentId) + ".xml"
    text_file = open(modelName, "w")
    text_file.write(str_model)
    text_file.close()
    return modelName

def createModelFourFour(master_model, experimentId,areaJam,areaArriv,greenTimer,redTimer,maxB,maxA,prevPhase):
    fo = open(master_model, "r+")
    str_model = fo.read()
    fo.close()
    greenTimer1 = [greenTimer[9]]
    greenTimer2 = [greenTimer[10]]
    greenTimer3 = [greenTimer[11]]
    greenTimer4 = [greenTimer[12]]

    redTimer1 = [redTimer[9]]
    redTimer2 = [redTimer[10]]
    redTimer3 = [redTimer[11]]
    redTimer4 = [redTimer[12]]

    traffic_light1 = [1]
    traffic_light2 = [2]
    traffic_light3 = [3]
    traffic_light4 = [4]
    tfl_jammed_cars_1 = areaJam[36:40]
    tfl_jammed_cars_2 = areaJam[40:44]
    tfl_jammed_cars_3 = areaJam[44:48]
    tfl_jammed_cars_4 = areaJam[48:52]

    tfl_arrived_cars_1 = areaArriv[36:40]
    tfl_arrived_cars_2 = areaArriv[40:44]
    tfl_arrived_cars_3 = areaArriv[44:48]
    tfl_arrived_cars_4 = areaArriv[48:52]
    trf_max_A_1 = [maxA[9]]
    trf_max_A_2 = [maxA[10]]
    trf_max_A_3 = [maxA[11]]
    trf_max_A_4 = [maxA[12]]
    trf_max_B_1 = [maxB[9]]
    trf_max_B_2 = [maxB[10]]
    trf_max_B_3 = [maxB[11]]
    trf_max_B_4 = [maxB[12]]
    all_in_one_trf1 = str(
        traffic_light1 + tfl_jammed_cars_1 + tfl_arrived_cars_1 + greenTimer1 + redTimer1 + trf_max_A_1 + trf_max_B_1 + convertPhase(
            prevPhase[9]))
    all_in_one_trf2 = str(
        traffic_light2 + tfl_jammed_cars_2 + tfl_arrived_cars_2 + greenTimer2 + redTimer2 + trf_max_A_2 + trf_max_B_2 + convertPhase(
            prevPhase[10]))
    all_in_one_trf3 = str(
        traffic_light3 + tfl_jammed_cars_3 + tfl_arrived_cars_3 + greenTimer3 + redTimer3 + trf_max_A_3 + trf_max_B_3 + convertPhase(
            prevPhase[11]))
    all_in_one_trf4 = str(
        traffic_light4 + tfl_jammed_cars_4 + tfl_arrived_cars_4 + greenTimer4 + redTimer4 + trf_max_A_4 + trf_max_B_4 + convertPhase(
            prevPhase[12]))
    toReplace = "//TRAFFIC_LIGHT_1"
    value = "trafficLight_1 = TL_model(" + listToStringWithoutBrackets(all_in_one_trf1) + ");"
    str_model = str.replace(str_model, toReplace, value, 1)

    toReplace = "//TRAFFIC_LIGHT_2"
    value = "trafficLight_2 = TL_model(" + listToStringWithoutBrackets(all_in_one_trf2) + ");"
    str_model = str.replace(str_model, toReplace, value, 1)

    toReplace = "//TRAFFIC_LIGHT_3"
    value = "trafficLight_3 = TL_model(" + listToStringWithoutBrackets(all_in_one_trf3) + ");"
    str_model = str.replace(str_model, toReplace, value, 1)

    toReplace = "//TRAFFIC_LIGHT_4"
    value = "trafficLight_4 = TL_model(" + listToStringWithoutBrackets(all_in_one_trf4) + ");"
    str_model = str.replace(str_model, toReplace, value, 1)
    modelName = pathToModels + "tl" + str(experimentId) + ".xml"
    text_file = open(modelName, "w")
    text_file.write(str_model)
    text_file.close()
    return modelName

def createModelFiveFive(master_model, experimentId,areaJam,areaArriv,greenTimer,redTimer,maxB,maxA,prevPhase):
    fo = open(master_model, "r+")
    str_model = fo.read()
    fo.close()
    greenTimer1 = [greenTimer[13]]
    greenTimer2 = [greenTimer[14]]
    greenTimer3 = [greenTimer[15]]
    greenTimer4 = [greenTimer[16]]
    greenTimer5 = [greenTimer[17]]

    redTimer1 = [redTimer[13]]
    redTimer2 = [redTimer[14]]
    redTimer3 = [redTimer[15]]
    redTimer4 = [redTimer[16]]
    redTimer5 = [redTimer[17]]

    traffic_light1 = [1]
    traffic_light2 = [2]
    traffic_light3 = [3]
    traffic_light4 = [4]
    traffic_light5 = [5]
    tfl_jammed_cars_1 = areaJam[52:56]
    tfl_jammed_cars_2 = areaJam[56:60]
    tfl_jammed_cars_3 = areaJam[60:64]
    tfl_jammed_cars_4 = areaJam[64:68]
    tfl_jammed_cars_5 = areaJam[68:72]

    tfl_arrived_cars_1 = areaArriv[52:56]
    tfl_arrived_cars_2 = areaArriv[56:60]
    tfl_arrived_cars_3 = areaArriv[60:64]
    tfl_arrived_cars_4 = areaArriv[64:68]
    tfl_arrived_cars_5 = areaArriv[68:72]
    trf_max_A_1 = [maxA[13]]
    trf_max_A_2 = [maxA[14]]
    trf_max_A_3 = [maxA[15]]
    trf_max_A_4 = [maxA[16]]
    trf_max_A_5 = [maxA[17]]
    trf_max_B_1 = [maxB[13]]
    trf_max_B_2 = [maxB[14]]
    trf_max_B_3 = [maxB[15]]
    trf_max_B_4 = [maxB[16]]
    trf_max_B_5 = [maxB[17]]
    all_in_one_trf1 = str(
        traffic_light1 + tfl_jammed_cars_1 + tfl_arrived_cars_1 + greenTimer1 + redTimer1 + trf_max_A_1 + trf_max_B_1 + convertPhase(
            prevPhase[13]))
    all_in_one_trf2 = str(
        traffic_light2 + tfl_jammed_cars_2 + tfl_arrived_cars_2 + greenTimer2 + redTimer2 + trf_max_A_2 + trf_max_B_2 + convertPhase(
            prevPhase[14]))
    all_in_one_trf3 = str(
        traffic_light3 + tfl_jammed_cars_3 + tfl_arrived_cars_3 + greenTimer3 + redTimer3 + trf_max_A_3 + trf_max_B_3 + convertPhase(
            prevPhase[15]))
    all_in_one_trf4 = str(
        traffic_light4 + tfl_jammed_cars_4 + tfl_arrived_cars_4 + greenTimer4 + redTimer4 + trf_max_A_4 + trf_max_B_4 + convertPhase(
            prevPhase[16]))
    all_in_one_trf5 = str(
        traffic_light5 + tfl_jammed_cars_5 + tfl_arrived_cars_5 + greenTimer5 + redTimer5 + trf_max_A_5 + trf_max_B_5 +
        convertPhase(prevPhase[17]))

    toReplace = "//TRAFFIC_LIGHT_1"
    value = "trafficLight_1 = TL_model(" + listToStringWithoutBrackets(all_in_one_trf1) + ");"
    str_model = str.replace(str_model, toReplace, value, 1)

    toReplace = "//TRAFFIC_LIGHT_2"
    value = "trafficLight_2 = TL_model(" + listToStringWithoutBrackets(all_in_one_trf2) + ");"
    str_model = str.replace(str_model, toReplace, value, 1)

    toReplace = "//TRAFFIC_LIGHT_3"
    value = "trafficLight_3 = TL_model(" + listToStringWithoutBrackets(all_in_one_trf3) + ");"
    str_model = str.replace(str_model, toReplace, value, 1)

    toReplace = "//TRAFFIC_LIGHT_4"
    value = "trafficLight_4 = TL_model(" + listToStringWithoutBrackets(all_in_one_trf4) + ");"
    str_model = str.replace(str_model, toReplace, value, 1)

    toReplace = "//TRAFFIC_LIGHT_5"
    value = "trafficLight_5 = TL_model(" + listToStringWithoutBrackets(all_in_one_trf5) + ");"
    str_model = str.replace(str_model, toReplace, value, 1)



    modelName = pathToModels + "tl" + str(experimentId) + ".xml"
    text_file = open(modelName, "w")
    text_file.write(str_model)
    text_file.close()
    return modelName

def createModelTwo(master_model, experimentId,areaJam,areaArriv,greenTimer,redTimer,maxB,maxA,prevPhase):
    fo = open(master_model, "r+")
    str_model = fo.read()
    fo.close()
    greenTimer1 = [greenTimer[18]]
    greenTimer2 = [greenTimer[19]]
    redTimer1 = [redTimer[18]]
    redTimer2 = [redTimer[19]]
    traffic_light1 = [1]
    traffic_light2 = [2]
    tfl_jammed_cars_1 = areaJam[72:76]
    tfl_jammed_cars_2 = areaJam[76:80]
    tfl_arrived_cars_1 = areaArriv[72:76]
    tfl_arrived_cars_2 = areaArriv[76:80]
    trf_max_A_1 = [maxA[18]]
    trf_max_A_2 = [maxA[19]]
    trf_max_B_1 = [maxB[18]]
    trf_max_B_2 = [maxB[19]]
    all_in_one_trf1 = str(
        traffic_light1 + tfl_jammed_cars_1 + tfl_arrived_cars_1 + greenTimer1 + redTimer1 + trf_max_A_1 + trf_max_B_1 + convertPhase(
            prevPhase[18]))
    all_in_one_trf2 = str(
        traffic_light2 + tfl_jammed_cars_2 + tfl_arrived_cars_2 + greenTimer2 + redTimer2 + trf_max_A_2 + trf_max_B_2 + convertPhase(
            prevPhase[19]))
    toReplace = "//TRAFFIC_LIGHT_1"
    value = "trafficLight_1 = TL_model(" + listToStringWithoutBrackets(all_in_one_trf1) + ");"
    str_model = str.replace(str_model, toReplace, value, 1)

    toReplace = "//TRAFFIC_LIGHT_2"
    value = "trafficLight_2 = TL_model(" + listToStringWithoutBrackets(all_in_one_trf2) + ");"
    str_model = str.replace(str_model, toReplace, value, 1)

    modelName = pathToModels + "tl" + str(experimentId) + ".xml"
    text_file = open(modelName, "w")
    text_file.write(str_model)
    text_file.close()
    return modelName

# convert string of ['(0,10)'] ==> [0,10] integer element
def convertIntegerList(first1):
    # if first1
    first = first1.replace("['(", '')
    first = first.replace(")']", '')
    first = first.replace("'", '')
    first = first.replace(" ", '')
    first = first.split(",")
    for i in range(len(first)):
        first[i] = int(first[i])
    return first

# converting output into meaningful array elements
def convertStringListToIntList(listItemInString,key_element):
    originalOutput_split = list(listItemInString)
    # remove timing information and get output
    originalOutput_split = str(originalOutput_split[1]).split(' ')
    start = 0;
    step = 0
    for i in originalOutput_split:
        if i == key_element:
            start = step
            break
        else:
            step += 1
    reqOutput = originalOutput_split[start::]
    listItemInStringProcessing = reqOutput
    intItems = [0] * len(reqOutput)
        # processing the output and extract relevant information
    for i in range(len(reqOutput)):
        listItemInStringProcessing[i] = str(reqOutput[i]).split(',')
        listItemInStringProcessing[i] = str(listItemInStringProcessing[i])
    for j in range(len(listItemInStringProcessing)-1):
        intItems[j] = convertIntegerList(listItemInStringProcessing[j])
    return intItems

# extract strategy from array list
def extractStrategy(time_phase_list,timeInfo):
    var1 =time_phase_list[2][1]
    strategy = []

    var1 = time_phase_list[2][0]
    var2 = time_phase_list[2] [1]
    for i in range(len(time_phase_list)-2):
        var1 = time_phase_list[i][0]
        var2 = time_phase_list[i+1][0]
        var3 = time_phase_list[i+1][1]
        # print("var1:",var1)
        if var1 < var2:
            total = list(zip([var2], [var3]))
            strategy.append(total)
    return  strategy

def extractPhaseTime(phaseString):
        phase = "1"
        inc = 0
        while(1):
            if phaseString[inc][0][1] == 10:
                phase = "2"
                break
            if phaseString[inc][0][1] == 2:
                phase = "0"
                break
            if phaseString[inc][0][1] == 6:
                phase = "1"
                break
            else:
                inc = inc + 1
        return phase,phaseString[inc][0][0]

def outputStringToindividualOne(string1,startString):
    originalOutput_split = list(string1)
    # remove timing information and get output
    originalOutput_split = str(originalOutput_split[1]).split(' ')
    start = 0; end = 0;
    step = 0
    stepEnd = 0
    for i in originalOutput_split:
        if i == startString:
            start = step
            break
        else:
            step += 1
    reqOutput = originalOutput_split[start::]
    return  reqOutput

def outputStringToindividual(string1,startString,endLength):
    start = 0;
    step = 0
    for i in string1:
        if i == startString:
            start = step
            break
        else:
            step += 1
    reqOutput = string1[start+1:start+endLength]
    listItemInStringProcessing = reqOutput
    intItems = [0] * len(reqOutput)
    # processing the output and extract relevant information
    for i in range(len(reqOutput)):
        listItemInStringProcessing[i] = str(reqOutput[i]).split(',')
        listItemInStringProcessing[i] = str(listItemInStringProcessing[i])
    for j in range(len(listItemInStringProcessing)):
        intItems[j] = convertIntegerList(listItemInStringProcessing[j])
    return  intItems


def convertTimeIntoSignal(signalInfowithTime,signalTime):
    new_k = []
    signal_new = []
    indexSig = 0
    for i in range(len(signalInfowithTime)):
        for elem in signalInfowithTime:
            if elem not in new_k:
                if elem[1] != 0:
                    new_k.append(elem)
    for i in range(len(new_k) - 1):
        prev = new_k[i]
        if i < len(new_k):
            cur = new_k[i + 1]
        else:
            cur = new_k[i]
        if prev[0] != cur[0]:
            signal_new.append(new_k[i+1])
        if prev[0] == cur[0]:
            signal_new.append(new_k[i])

    signal = np.arange(signalTime)
    for i in range(len(signal_new)):
        t = signal_new[i][1]
        if t == 2:
            for j in range(5):
                signal[indexSig] = np.int(0)
                indexSig += 1
        elif t == 10:
            for j in range(5):
                signal[indexSig] = np.int(2)
                indexSig += 1
        elif t == 6:
            for j in range(5):
                signal[indexSig] = np.int(3)
                indexSig += 1
    return signal_new,signal

def seperatorOutputFour(stringToBeProcessed):
    signalTime = 120
    stringLength = 60
    traffic_light = outputStringToindividualOne(stringToBeProcessed,'trafficLight_1.GREEN_B:\n[0]:')
    traffic_light_1 = outputStringToindividual(traffic_light,'trafficLight_1.GREEN_B:\n[0]:',stringLength)
    traffic_light_2 = outputStringToindividual(traffic_light,'trafficLight_2.GREEN_B:\n[0]:',stringLength)
    traffic_light_3 = outputStringToindividual(traffic_light,'trafficLight_3.GREEN_B:\n[0]:',stringLength)
    traffic_light_4 = outputStringToindividual(traffic_light,'trafficLight_4.GREEN_B:\n[0]:',stringLength)
    totalNext,nextPhase_1 = convertTimeIntoSignal(traffic_light_1,signalTime)
    totalNext,nextPhase_2 = convertTimeIntoSignal(traffic_light_2,signalTime)
    totalNext,nextPhase_3 = convertTimeIntoSignal(traffic_light_3,signalTime)
    totalNext,nextPhase_4 = convertTimeIntoSignal(traffic_light_4,signalTime)
    totalNextPhase = [nextPhase_1,nextPhase_2,nextPhase_3,nextPhase_4]
    # print("signal timing:",totalNextPhase[1])
    return totalNextPhase

def seperatorOutputFive(stringToBeProcessed):
    signalTime = 120
    stringLength = 60
    traffic_light = outputStringToindividualOne(stringToBeProcessed,'trafficLight_1.GREEN_B:\n[0]:')
    traffic_light_1 = outputStringToindividual(traffic_light,'trafficLight_1.GREEN_B:\n[0]:',stringLength)
    traffic_light_2 = outputStringToindividual(traffic_light,'trafficLight_2.GREEN_B:\n[0]:',stringLength)
    traffic_light_3 = outputStringToindividual(traffic_light,'trafficLight_3.GREEN_B:\n[0]:',stringLength)
    traffic_light_4 = outputStringToindividual(traffic_light,'trafficLight_4.GREEN_B:\n[0]:',stringLength)
    traffic_light_5 = outputStringToindividual(traffic_light,'trafficLight_5.GREEN_B:\n[0]:',stringLength)
    totalNext,nextPhase_1 = convertTimeIntoSignal(traffic_light_1,signalTime)
    totalNext,nextPhase_2 = convertTimeIntoSignal(traffic_light_2,signalTime)
    totalNext,nextPhase_3 = convertTimeIntoSignal(traffic_light_3,signalTime)
    totalNext,nextPhase_4 = convertTimeIntoSignal(traffic_light_4,signalTime)
    totalNext,nextPhase_5 = convertTimeIntoSignal(traffic_light_5,signalTime)
    totalNextPhase = [nextPhase_1,nextPhase_2,nextPhase_3,nextPhase_4,nextPhase_5]
    # print("signal timing:",totalNextPhase[1])
    return totalNextPhase

def seperatorOutputTwo(stringToBeProcessed):
    signalTime = 120
    stringLength = 60
    traffic_light = outputStringToindividualOne(stringToBeProcessed,'trafficLight_1.GREEN_B:\n[0]:')
    traffic_light_1 = outputStringToindividual(traffic_light,'trafficLight_1.GREEN_B:\n[0]:',stringLength)
    traffic_light_2 = outputStringToindividual(traffic_light,'trafficLight_2.GREEN_B:\n[0]:',stringLength)
    totalNext,nextPhase_1 = convertTimeIntoSignal(traffic_light_1,signalTime)
    totalNext,nextPhase_2 = convertTimeIntoSignal(traffic_light_2,signalTime)
    totalNextPhase = [nextPhase_1,nextPhase_2]
    # print("signal timing:",totalNextPhase[1])
    return totalNextPhase

def callUppaalStratego(areaJam,areaArriv, greenTimer, redTimer,maxGreenB,maxGreenA,prevPhase ):
    stratego = home+'/stratego-3/bin-Linux/verifyta '
    # -------------------------------------- four model -----------------------------------------------------------------------------------------------
    newModelFour = createModelFour(strategoTrafficLightModelFour,experimentId[0],areaJam,areaArriv,greenTimer,redTimer,maxGreenB,maxGreenA,prevPhase)

    argsFour = newModelFour \
      + ' --learning-method ' + strategoLearningMet \
      + ' --good-runs ' + strategoSuccRuns \
      + ' --total-runs ' + strategoMaxRuns \
      + ' --runs-pr-state ' + strategoGoodRuns \
      + ' --eval-runs ' + strategoEvalRuns \
      + ' --max-iterations ' + strategoMaxIterations \
      + ' --filter 0 '
    cmdOutputFour = runStratego(stratego,argsFour,strategoQueryFour,experimentId[0]) # command line output
    print("Calling stratego for traffic light strategy four model")
    print("output like: this: \n",cmdOutputFour)
    phaseinfoFour = seperatorOutputFour(cmdOutputFour)
    # remYPhaseinfoFour = removeMoreYellow(phaseinfoFour)



    # -------------------------------------- five model -----------------------------------------------------------------------------------------------

    # traffic 5 coordination

    newModelFive = createModelFive(strategoTrafficLightModelFive, experimentId[1], areaJam,areaArriv,greenTimer,redTimer,maxGreenB,maxGreenA,prevPhase)
    print("Calling stratego for traffic light strategy five model ")
    argsFive = newModelFive \
               + ' --learning-method ' + strategoLearningMet \
               + ' --good-runs ' + strategoSuccRuns \
               + ' --total-runs ' + strategoMaxRuns \
               + ' --runs-pr-state ' + strategoGoodRuns \
               + ' --eval-runs ' + strategoEvalRuns \
               + ' --max-iterations ' + strategoMaxIterations \
               + ' --filter 0 '
    cmdOutputFive = runStratego(stratego, argsFive, strategoQueryFive,experimentId[1])  # command line output
    print("output like: this: \n", cmdOutputFive)
    phaseinfoFive = seperatorOutputFive(cmdOutputFive)

    # -------------------------------------- four four model -----------------------------------------------------------------------------------------------

    # # traffic 44 coordination
    newModelFourFour = createModelFourFour(strategoTrafficLightModelFourFour, experimentId[2], areaJam, areaArriv, greenTimer,redTimer,maxGreenB,maxGreenA,prevPhase)
    print("Calling stratego for traffic light strategy fourfour model")
    argsFourFour = newModelFourFour \
               + ' --learning-method ' + strategoLearningMet \
               + ' --good-runs ' + strategoSuccRuns \
               + ' --total-runs ' + strategoMaxRuns \
               + ' --runs-pr-state ' + strategoGoodRuns \
               + ' --eval-runs ' + strategoEvalRuns \
               + ' --max-iterations ' + strategoMaxIterations \
               + ' --filter 0 '

    cmdOutputFourFour = runStratego(stratego, argsFourFour, strategoQueryFourFour, experimentId[2])  # command line output
    print("output like: this: \n", cmdOutputFourFour)
    phaseinfoFourFour = seperatorOutputFour(cmdOutputFourFour)

    # -------------------------------------- five five model -----------------------------------------------------------------------------------------------

    # traffic 55 coordination
    newModelFiveFive = createModelFiveFive(strategoTrafficLightModelFiveFive, experimentId[3], areaJam, areaArriv, greenTimer,redTimer,maxGreenB,maxGreenA,prevPhase)
    print("Calling stratego for traffic light strategy fivefive model ")
    argsFiveFive = newModelFiveFive \
               + ' --learning-method ' + strategoLearningMet \
               + ' --good-runs ' + strategoSuccRuns \
               + ' --total-runs ' + strategoMaxRuns \
               + ' --runs-pr-state ' + strategoGoodRuns \
               + ' --eval-runs ' + strategoEvalRuns \
               + ' --max-iterations ' + strategoMaxIterations \
               + ' --filter 0 '
    cmdOutputFiveFive = runStratego(stratego, argsFiveFive, strategoQueryFiveFive, experimentId[3])  # command line output
    print("output like: this: \n", cmdOutputFiveFive)
    phaseinfoFiveFive = seperatorOutputFive(cmdOutputFiveFive)

    # --------------------------------------  two model -----------------------------------------------------------------------------------------------

    # traffic 2 coordination
    print("Calling stratego for traffic light strategy two model ")
    newModelTwo = createModelTwo(strategoTrafficLightModelTwo, experimentId[4], areaJam, areaArriv, greenTimer, redTimer,maxGreenB,maxGreenA,prevPhase)
    argsTwo = newModelTwo \
                   + ' --learning-method ' + strategoLearningMet \
                   + ' --good-runs ' + strategoSuccRuns \
                   + ' --total-runs ' + strategoMaxRuns \
                   + ' --runs-pr-state ' + strategoGoodRuns \
                   + ' --eval-runs ' + strategoEvalRuns \
                   + ' --max-iterations ' + strategoMaxIterations \
                   + ' --filter 0 '
    cmdOutputTwo = runStratego(stratego, argsTwo, strategoQueryTwo,experimentId[4])  # command line output
    print("output like: this: ", cmdOutputTwo)
    phaseinfoTwo = seperatorOutputTwo(cmdOutputTwo)
    phaseinfo = phaseinfoFour + phaseinfoFive + phaseinfoFourFour + phaseinfoFiveFive + phaseinfoTwo
    phaseInfoAfterYellowRemove = []
    for i in range(20):
        phaseInfoAfterYellowRemove.append(removeMoreYellow(phaseinfo[i]))

    return phaseInfoAfterYellowRemove


if __name__ == "__main__":

    areaJammed = [1, 1, 14, 3,1, 1, 14, 3,1, 1, 14, 3,1, 1, 14, 3,1, 3, 8, 12]
    areaArrived = [1, 1, 14, 3,1, 1, 14, 3,1, 1, 14, 3,1, 1, 14, 3,1, 1, 11, 7]

    greenTimer = 30
    redTimer = 40
    phase = callUppaalStratego(areaJammed,areaArrived,greenTimer,redTimer)
    print("phase: duration:",phase)




