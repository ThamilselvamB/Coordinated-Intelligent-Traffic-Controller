#!/usr/bin/env python
# Eclipse SUMO, Simulation of Urban MObility; see https://eclipse.org/sumo
# Copyright (C) 2009-2019 German Aerospace Center (DLR) and others.
# This program and the accompanying materials
# are made available under the terms of the Eclipse Public License v2.0
# which accompanies this distribution, and is available at
# http://www.eclipse.org/legal/epl-v20.html
# SPDX-License-Identifier: EPL-2.0

# @file    detectorData.py
# @author  Lena Kalleske
# @author  Daniel Krajzewicz
# @author  Michael Behrisch
# @author  Jakob Erdmann
# @date    2009-03-26
# @version $Id$

# @ modified for research purpose Thamilselvam B
# @date 2019-08-01

from __future__ import absolute_import
from __future__ import print_function
import numpy as np
import os
import sys
import optparse
import csv
import time
import matplotlib.pyplot as plt
# user's python files
from intelligentModel2PhaseCoord import callUppaalStratego
import detectorData
import generateRouteForTwenty
import calculateWaitingTime
import plottingPurpose

# we need to import python modules from the $SUMO_HOME/tools directory
if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")
from sumolib import checkBinary  # noqa
import traci  # noqa

# loop and area detectors
areaDetectorFifty = detectorData.areaDetectorFifty
areaDetectorFiftySeqIndex = detectorData.areaDetectorFiftySeqIndex
loopDetectorFifity = detectorData.loopDetectorFifity
loopDetectorFiftySeqIndex = detectorData.loopDetectorFiftySeqIndex
loopAreaDetectorFifity = detectorData.loopAreaDetectorFifity
throughputLoopDetectors = detectorData.throughputLoopDetectors

totalWaitingTime = np.zeros(20,dtype=int)
tolSum =[]
phaseNS = np.zeros(20,dtype=int)
phaseWE = np.zeros(20,dtype=int) + 2
phaseToNS = np.zeros(20,dtype=int) + 1
phaseToEW = np.zeros(20,dtype=int) + 3
ic_minGreen = np.zeros(20,dtype=int) + 8
yellow = np.zeros(20,dtype=int) + 4
timeInPhase = np.zeros(20,dtype=int)
nextPhase = np.zeros(20,dtype=int)
phase = np.zeros(20,dtype=int)
count_time = [False] * 20
phaseTime = np.zeros(20,dtype=int)


# intelligent variable declaration
previousPhase = np.zeros(20,dtype=int)
maximumTimer_A = np.zeros(20,dtype=int) + 40
maximumTimer_B = np.zeros(20,dtype=int) + 40
loadCapacity = [15,20,25,30,35,45,55,75,100,120]
maxGreenTimeforLoad = [50,60,70,90,100,110,120,130,140,150]
intelligentTimer = [20,25,30,35,40,45,45,50,50,50]

trafficLightId = detectorData.trafficLightId

class TrafficLight:
    totalWaitingTime = 0 ; totalQueueLength = 0 ; totalCo2Emission = 0 ; totalCoEmission = 0

    def __init__(self, trlId, areaDetectors,loopDetectors,loopAreaDetectors,sInd,sIndLoop,debug):
        self.trlId = trlId
        self.areaDetectors = areaDetectors
        self.loopDetectors = loopDetectors
        self.loopAreaDetectors = loopAreaDetectors
        self.sIndex = sInd
        self.sIndexLoop = sIndLoop
        self.debug = debug
        self.direction_A = 0
        self.direction_B = 0

    def getData(self,func, dets):
        numDet = len(dets)
        res = [0] * numDet
        for deti in range(0, numDet):
            res[deti] = func(dets[deti])
        return res

    # get the arrival car list
    def getArrivalCars(self):
        indx = self.sIndex
        carsArrival = self.getData(traci.lanearea.getLastStepVehicleNumber, self.areaDetectors)
        carArrival = [ sum(carsArrival[indx[0]:indx[1]]),sum(carsArrival[indx[2]:indx[3]])
                       ,sum(carsArrival[indx[4]:indx[5]]),sum(carsArrival[indx[6]:indx[7]])]
        self.direction_A = sum(carArrival[0:2])
        self.direction_B = sum(carArrival[2:4])
        if self.debug:
            print("In Intersection %s: Arrival cars [Left Right Up Down]:%s"%(self.trlId,carArrival))
        return carArrival

    # get the jammed car list
    def getJammedCars(self):
        indx = self.sIndex
        carsJammed = self.getData(traci.lanearea.getLastStepHaltingNumber, self.areaDetectors)
        carJammed = [sum(carsJammed[indx[0]:indx[1]]), sum(carsJammed[indx[2]:indx[3]])
            , sum(carsJammed[indx[4]:indx[5]]), sum(carsJammed[indx[6]:indx[7]])]
        if self.debug:
            print("In Intersection %s: Jammed cars [Left Right Up Down]:%s" % (self.trlId, carJammed))
        return carJammed

        # get the waiting car list

    def getWaitingCars(self):
        indx = self.sIndex
        carsWaiting = self.getData(traci.lanearea.getLastStepHaltingNumber, self.areaDetectors)
        carWaiting = [sum(carsWaiting[indx[0]:indx[2]]), sum(carsWaiting[indx[2]:indx[4]])
            , sum(carsWaiting[indx[4]:indx[6]]), sum(carsWaiting[indx[6]::])]
        self.totalWaitingTime += sum(carWaiting)
        if self.debug:
            print("In Intersection %s: Jammed cars [Left Right Up Down]:%s" % (self.trlId, carWaiting))
        return carWaiting
    # get the jammed cars length in meters
    def getJammedCarsLength(self):
        indx = self.sIndex
        carsJammedLength = self.getData(traci.lanearea.getJamLengthMeters, self.areaDetectors)
        carJammedLength = [sum(carsJammedLength[indx[0]:indx[2]]), sum(carsJammedLength[indx[2]:indx[4]])
            , sum(carsJammedLength[indx[4]:indx[6]]), sum(carsJammedLength[indx[6]::])]
        self.totalQueueLength += sum(carJammedLength)
        if self.debug:
            print("In Intersection %s: Jammed cars Length [Left Right Up Down]:%s" % (self.trlId, carJammedLength))
        return carJammedLength

    # getting loop detector data for loop controller
    def getLoopDetectorData(self):
        indx = self.sIndexLoop
        carsCrossed = self.getData(traci.inductionloop.getLastStepVehicleNumber, self.loopDetectors)
        carsCrossedNow = [sum(carsCrossed[indx[0]:indx[1]]), sum(carsCrossed[indx[2]:indx[3]])
            , sum(carsCrossed[indx[4]:indx[5]]), sum(carsCrossed[indx[6]:indx[7]])]
        if self.debug:
            print("In Intersection %s: Loop detector data [Left Right Up Down]:%s" % (self.trlId, carsCrossedNow))
        return carsCrossedNow

    # minor road small lenght area detector data
    def getLoopAreaDetectorData(self):
        carsLoopArea = self.getData(traci.lanearea.getLastStepVehicleNumber, self.loopAreaDetectors)
        if self.debug:
            print("In Intersection %s: loop area detectors [Up Down]:%s" % (self.trlId, carsLoopArea))
        return carsLoopArea

    def dataForLoopController(self):
        cData = np.hstack( (self.getLoopDetectorData(),self.getLoopAreaDetectorData()) )
        return cData

    # Co2 and Co  emission calculation
    def getEmission(self):
        indx = self.sIndex
        emissionOutCo2 = 0
        emissionOutCo = 0
        carsCo2Emission = self.getData(traci.lanearea.getLastStepVehicleIDs, self.areaDetectors)
        out = list(sum(carsCo2Emission, ()))
        for i in range(len(out)):
            emissionOutCo2 += traci.vehicle.getCO2Emission(out[i])
            emissionOutCo += traci.vehicle.getCOEmission(out[i])
        self.totalCo2Emission += emissionOutCo2
        self.totalCoEmission += emissionOutCo
        if self.debug:
            pass
            # print("In Intersection %s: Co2 Emission (mg):%s" % (self.trlId, self.totalCo2Emission))
            # print("In Intersection %s: Co Emission (mg):%s" % (self.trlId, self.totalCoEmission))
        return emissionOutCo2,emissionOutCo


    def dataForIntelligentController(self):
        cIData = np.hstack(( self.getArrivalCars(),self.getJammedCars()))
        cIJammedLength = self.getJammedCarsLength()
        self.getEmission()
        return cIData,cIJammedLength


def getThroughput(func, dets):
    numDet = len(dets)
    res = [0] * numDet
    for deti in range(0,numDet):
        res[deti] = func(dets[deti])
    return res

# def motorWaiting(areaDetectors):
#     count = 0
#     vehicleIds = traci.lanearea.getLastStepVehicleIDs(areaDetectors)
#     motorId = traci.lanearea.getLastStepHaltingNumber(areaDetectors)
#     print("vehicle ids:",vehicleIds)
#     motorString = str(vehicleIds)
#     for i in vehicleIds:
#         if i.startswith("motorCycle",0,10):
#             count += 1
#     for j in vehicleIds:
#         print("vehicle waitng time:",traci.vehicle.getWaitingTime(j))
#     return count
# strategoTimer = [0,0,0,0,0]
# areaDetectors = [1,2,16,18]

greenTimer = np.arange(len(trafficLightId))
redTimer = np.arange(len(trafficLightId))


t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)
# ysample = random.sample(range(0, 500), 250)
# print("ysample:",ysample)
xdata = []
ydata = []
x1data = []
y1data = []

def oneTimePlotIntialization(x_end,y_end):
    plt.show()
    axes = plt.gca()
    axes.set_xlim(0, x_end)
    axes.set_ylim(0, y_end)
    line, = axes.plot(xdata, ydata, 'r-')
    line1, = axes.plot(x1data, y1data, 'g-')
    return line,line1

def plotGraph(x_data,y_data,x1_data,y1_data,line,line1):

    xdata.append(x_data)
    ydata.append(y_data)

    x1data.append(x1_data)
    y1data.append(y1_data)

    line.set_xdata(xdata)
    line.set_ydata(ydata)


    line1.set_xdata(x1data)
    line1.set_ydata(y1data)

    plt.draw()
    plt.pause(1e-17)
    time.sleep(0.1)

    # loop controllers

def extend(ext, bound, extTime):
    ext = ext + extTime
    return ext

def actuatedController(trlId, phaseNS, phaseToNS, phaseWE, phaseToEW, maxGreenNS, maxGreenEW, yellow, ic_minGreen,
                   phaseNow, timeInPhaseNow, phaseTimeNow, count_timeNow, nextPhaseNow, loopDet, areaDet):
    if phaseNow == phaseNS[trlId] or phaseNow == phaseWE[trlId]:  # we controll the green time
        traci.trafficlights.setPhaseDuration(trafficLightId[trlId], 5000)
    loopDetInfo = loopDet
    areDetInfo = areaDet
    if phaseNow == phaseWE[trlId]:  # Green in B direction
        if timeInPhaseNow >= maxGreenEW[trlId] or phaseTimeNow <= 0:
            # Goto yellow
            traci.trafficlights.setPhase(trafficLightId[trlId], phaseToNS[trlId])
            phaseNow = phaseToNS[trlId]
            nextPhaseNow = phaseNS[trlId]
            timeInPhaseNow = 0
        else:  # Check if we shoud extend the phase timer
            phaseTimeNow -= 1
            if loopDetInfo[0] >= 1 or loopDetInfo[1] >= 1:
                phaseTimeNow = extend(phaseTimeNow, maxGreenEW[trlId], 4.0)
            cars_on_AreDet = sum(areDetInfo) > 0
            if cars_on_AreDet:  # Make sure the time ticks while we stay in one phase
                phaseTimeNow += 1
        timeInPhaseNow += 1
    elif phaseNow == phaseNS[trlId]:  # Green in A direction
        if timeInPhaseNow >= maxGreenNS[trlId] or phaseTimeNow <= 0:
            # Goto yellow
            traci.trafficlights.setPhase(trafficLightId[trlId], phaseToEW[trlId])
            phaseNow = phaseToEW[trlId]
            nextPhaseNow = phaseWE[trlId]
            timeInPhaseNow = 0
        else:
            cars_on_AreDet = sum(areDetInfo) > 0
            if loopDetInfo[0] == 1 or loopDetInfo[1] == 1 or cars_on_AreDet:
                count_timeNow = True
            if count_timeNow:  # This phase is the resting phase
                if loopDetInfo[2] == 1 or loopDetInfo[3] == 1:
                    phaseTimeNow = extend(phaseTimeNow, maxGreenNS[trlId], 4.0)
                if loopDetInfo[2] == 1 or loopDetInfo[3] == 1:
                    phaseTimeNow = extend(phaseTimeNow, maxGreenNS[trlId], 4.0)
                timeInPhaseNow += 1
                phaseTimeNow -= 1
    else:  # In yellow
        if timeInPhaseNow == yellow[trlId]:
            # At the end of yellow the timeing variables are reset, the min green time is 10
            timeInPhaseNow = 0
            phaseTimeNow = ic_minGreen[trlId]
            phaseNow = nextPhaseNow
            traci.trafficlights.setPhase(trafficLightId[trlId], phaseNow)
            # traci.trafficlights.setPhaseDuration(idTL, 60)
            count_timeNow = False
        else:
            timeInPhaseNow += 1
    phase[trlId] = phaseNow
    nextPhase[trlId] = nextPhaseNow
    phaseTime[trlId] = phaseTimeNow
    timeInPhase[trlId] = timeInPhaseNow
    count_time[trlId] = count_timeNow

    # return phaseNow



def writeFile(row):
    # create file(if no file) and append data
    with open('trafficWaiting.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(row)
    csvFile.close()
def loadMaximumActuated(load):
    if load == "Case1Low":
        maxGreenEW = np.zeros(20, dtype=int) + 25
        maxGreenNS = np.zeros(20, dtype=int) + 40
    if load == "Case1Mid":
        maxGreenEW = np.zeros(20, dtype=int) + 35
        maxGreenNS = np.zeros(20, dtype=int) + 55
    if load == "Case1High":
        maxGreenEW = np.zeros(20, dtype=int) + 55
        maxGreenNS = np.zeros(20, dtype=int) + 85
    if load == "Case2":
        maxGreenEW = np.zeros(20, dtype=int) + 50
        maxGreenNS = np.zeros(20, dtype=int) + 60
    if load == "Case3":
        maxGreenEW = np.zeros(20, dtype=int) + 40
        maxGreenNS = np.zeros(20, dtype=int) + 40
    if load == "Case4":
        maxGreenEW = np.zeros(20, dtype=int) + 65
        maxGreenNS = np.zeros(20, dtype=int) + 35

    return maxGreenEW,maxGreenNS
def emissionCalculation(vehicleList,mode):
    sum = 0
    for vehId in vehicleList:
        if mode == "CO":
            sum += traci.vehicle.getCOEmission(vehId)
        if mode == "CO2":
            sum += traci.vehicle.getCO2Emission(vehId)
        if mode == "WaitingTime":
            if traci.vehicle.getSpeed(vehId) < 0.1:
                sum += 1
    return sum
def run():
    """execute the TraCI control loop"""
    step = 0
    strategoTimerTicks = 0
    crossedCars = 0
    # load fixed and actuated timing for traffic light
    for i in range(len(trafficLightId)):
        traci.trafficlights.setProgram(trafficLightId[i],options.load)

    maxGreenEW,maxGreenNS = loadMaximumActuated(options.load)

    print("%s controller is working in %s now............." %(options.controller,options.load))
    totalWaitingTime = 0
    totalCo2 = 0.0
    totalCo = 0.0
    # line,line1 = oneTimePlotIntialization(3000,15)
    nextPhaseNow = np.arange(250).reshape(5,50)
    trafficLightObj = list()
    queueLength = 0
    waitingTime = 0
    carJam = []
    carArrv = []
    timeVerJammedCars =[]
    timeVerQueuedCars =[]
    totalCOemision = []
    totalCO2emision = []
    totalWaitingtimeFrom = []
    for i in range(20):
        trafficLightObj.append( TrafficLight(str(i), areaDetectorFifty[i], loopDetectorFifity[i], loopAreaDetectorFifity[i], areaDetectorFiftySeqIndex[i],loopDetectorFiftySeqIndex[i],False))
    # t1 = TrafficLight("1", areaDet, loopDet, loopArea, sIndex,sIndexLoop,False)
    # t2 = TrafficLight("1", areaDet, loopDet, loopArea, sIndex,sIndexLoop,False)
    # while traci.simulation.getMinExpectedNumber() > 0:
    currentIntelligentTimer = 20
    oneTimeRun = True
    previousPhase = np.zeros(20, dtype=int)
    currentLoad = 100
    stepPerLoad = []
    # while traci.simulation.getMinExpectedNumber() > 0:
    while step <= int(options.step):
        # traci.switch("static")
        # traci.simulationStep()
        # y = sum(t1.getJammedCars())
        # y1 = sum(t1.getArrivalCars())
        # # plotGraph(step, y, step, y1, line, line1)
        # intl, ql = t1.dataForIntelligentController()
        # print("Total waiting Time in Static:",t1.totalWaitingTime)
        # traci.switch("loop")
        traci.simulationStep()
        step = step + 1
        jamCarsOneStep = 0
        queueCarsOneStep = 0
# ------------------------- Output data ---------------------------------------------------------------------------
        for outdata in range(0, 20):
            jamCarsOneStep += sum(trafficLightObj[outdata].getWaitingCars())
            queueCarsOneStep += sum(trafficLightObj[outdata].getJammedCarsLength())
        timeVerJammedCars.append(jamCarsOneStep)
        timeVerQueuedCars.append(queueCarsOneStep)

        # -----------------------------------------------------------------------------------------------------
        throughput = getThroughput(traci.inductionloop.getLastStepVehicleNumber, throughputLoopDetectors)
        crossedCars = crossedCars+ sum(throughput)
        #------------------ Emission calculation ---------------------------------------
        vehIdsList = traci.vehicle.getIDList()
        totalCOemision.append(emissionCalculation(vehIdsList,"CO"))
        totalCO2emision.append(emissionCalculation(vehIdsList,"CO2"))
        totalWaitingtimeFrom.append(emissionCalculation(vehIdsList,"WaitingTime"))
        # # print("vehicle ids:",traci.vehicle.getIDList())
        # for vehId in vehIdsList:
        #     # print("Co2 emission:",traci.vehicle.getCO2Emission(vehId))
        #     # print("Co emission:", traci.vehicle.getCOEmission(vehId))
        #     totalCOemision.append(traci.vehicle.getCO2Emission(vehId))
        #     if traci.vehicle.getSpeed(vehId) < 0.1:
        #         print("Waiting time: ", traci.vehicle.getSpeed(vehId),vehId)

        # print("crossed cars",crossedCars)
        # print("\rCars passed count:  {}".format(crossedCars), end="")
        # print("\rTime Step        :  {}".format(step), end="")
        # print("\n")
        # for outdata in range(0,20):
        #     trafficLightObj[outdata].getJammedCarsLength()
        #     trafficLightObj[outdata].getArrivalCars()
        #     # trafficLightObj[outdata].getWaitingCars()
        #     # queueLength += trafficLightObj[outdata].totalQueueLength
        #     # waitingTime += trafficLightObj[outdata].totalWaitingTime
        #     # print("In Traffic light %s: %s Hours" %(outdata+1,trafficLightObj[outdata].totalWaitingTime))
        #     print("Traffic Light: %s Arrival Cars: %s " % (outdata+ 1 , trafficLightObj[outdata].getArrivalCars()))
        #     print("Traffic Light: %s Jammed Cars: %s " % (outdata + 1, trafficLightObj[outdata].getJammedCars()))
            # print("Traffic Light: %s waiting Cars: %s " % (outdata + 1, trafficLightObj[outdata].getWaitingCars()))
            # print("Traffic Light: %s Detector details: %s " % (outdata + 1, trafficLightObj[outdata].dataForLoopController()))
    #     #------------------------------------------------------------------------------------------------------

        # get the current loaded capacity

        if step % 100 == 0:

            for trfLgt in range(0, 20):
                loadInADirection = trafficLightObj[trfLgt].direction_A
                loadInBDirection = trafficLightObj[trfLgt].direction_B
                for lc in range(len(loadCapacity)):
                    if loadCapacity[lc] >= loadInADirection:
                        maximumTimer_A[trfLgt] = maxGreenTimeforLoad[lc]
                    if loadCapacity[lc] >= loadInBDirection:
                        maximumTimer_B[trfLgt] = maxGreenTimeforLoad[lc]
                        break
            for trf in range(len(trafficLightId)):
                currentLoad = currentLoad + sum(trafficLightObj[trf].getArrivalCars())
            stepPerLoad.append(currentLoad)
            for lc in range(len(loadCapacity)):
                if (loadCapacity[lc] * 30 ) >= currentLoad:
                    currentIntelligentTimer = intelligentTimer[lc]
                    currentLoad = 0
                    break
            # writing time step and load
        # ------------------------cheking purpose-----------------------------
        # for a in range(16, 17):
        #     print("cars arrival in %s is %s" % (a + 1, trafficLightObj[a].getArrivalCars()))
        #     print("cars jammed in %s is %s" % (a + 1, trafficLightObj[a].getJammedCars()))
        # print("loop dec value:",throughput)
        # print("crossed cars:",crossedCars)
        # arrr= trafficLightObj[0].getArrivalCars()
        # print("A direction Cars:",AreaOne_A)
        # print("B direction Cars:",AreaOne_B)


        # y1 = sum(t2.getJammedCars())
        # y1 = sum(t1.getArrivalCars())
        # intl,ql = t2.dataForIntelligentController()
        # print("Loop controller", t1.dataForLoopController())
        # t1.getEmission()
        # print("Inte controller",intl )
        # print("Inte controller length",ql )
        # print("Total waiting Time in Loop:",t2.totalWaitingTime)
        # print("Total waiting Time:",t1.totalQueueLength)

        # ------------------------------------ Loop Controller ------------------------------------------------------
        if options.controller == "Actuated":
         for i in range(20):

            loopDet1 = trafficLightObj[i].getLoopDetectorData()
            loopArea1 = trafficLightObj[i].getLoopAreaDetectorData()
            actuatedController(i,phaseNS,phaseToNS,phaseWE,phaseToEW,maxGreenNS,maxGreenEW,yellow,ic_minGreen,phase[i],timeInPhase[i],phaseTime[i],
                                count_time[i],nextPhase[i],loopDet1,loopArea1)
         if oneTimeRun:
            print("--------------Actuated controller is working now:------------ ")
            oneTimeRun = False

         # ------------------------------------ Intelligent Controller ------------------------------------------------------

         # calling intelligent controller
        if options.controller == "Intelligent":
         if oneTimeRun:
            print("--------------------------------Intelligent controller is working now:--------------------------------------")
            oneTimeRun = False
         for a in range(0,20):
            # print("cars arrival in %s is %s" %(a+1,trafficLightObj[a].getArrivalCars()))
            # print("cars jammed in %s is %s" %(a+1,trafficLightObj[a].getJammedCars()))
            carJam.append(trafficLightObj[a].getJammedCars())
            carArrv.append(trafficLightObj[a].getArrivalCars())

        # print("cars jammed list:",carJam)
         carsJam = []
         carsArrv = []
         for b in range(0,20):
            carsJam = carsJam + carJam[b]
            carsArrv = carsArrv + carArrv[b]
         carJam.clear()
         carArrv.clear()
         if strategoTimerTicks <= 0:
            nextPhaseNow = callUppaalStratego(carsJam,carsArrv,greenTimer,redTimer,maximumTimer_B,maximumTimer_A,previousPhase)
            print("Intelligent Timer : %s step: %s" % (currentIntelligentTimer,step))
            strategoTimerTicks = currentIntelligentTimer
            for a in range(0, 20):
                print("cars arrival,Jam in %s %s is %s phase:%s" %(a+1,trafficLightObj[a].getArrivalCars(),trafficLightObj[a].getJammedCars(),nextPhaseNow[a][0:20]))
                print("GreenTimer-A: %s GreenTimer-B: %s Max-A: %s Max-B: %s" %(redTimer[a],greenTimer[a],maximumTimer_A[a],maximumTimer_B[a]))
         else:
            for i in range(0,20):
                    traci.trafficlight.setPhase(trafficLightId[i], nextPhaseNow[i][strategoTimerTicks])
                    previousPhase[i] = nextPhaseNow[i][currentIntelligentTimer-3]
                    if nextPhaseNow[i][strategoTimerTicks] == 2:
                        greenTimer[i] += 1
                    if nextPhaseNow[i][strategoTimerTicks] == 0:
                        redTimer[i] += 1
                    if nextPhaseNow[i][strategoTimerTicks] == 3:
                        redTimer[i] = 0
                        greenTimer[i] = 0
            strategoTimerTicks -= 1

    traci.close()
    detWaitingTime = np.arange(20)
    detQueueLength = np.arange(20)
    #
    for i in range(20):
        print("In Traffic light %s: %s Hours" % (i + 1, trafficLightObj[i].totalWaitingTime))
        detWaitingTime[i] = trafficLightObj[i].totalWaitingTime
        detQueueLength[i] = trafficLightObj[i].totalQueueLength
    detWaitingTime = np.around(detWaitingTime / 3600,2)
    detQueueLength = np.around(detQueueLength/1000 ,2)
    print("Waiting time from detectors:",sum(detWaitingTime))
    print("Queue length from detectors:", sum(detQueueLength))
    print("time verses cars:",timeVerJammedCars)
    # writing required data into file
    plottingPurpose.writeToFile("trafficWaiting.csv", stepPerLoad)
    calculateWaitingTime.writingPlottingData(detWaitingTime,options.controller+"Bar",options.load)
    calculateWaitingTime.writingPlottingData(timeVerJammedCars,options.controller+"Line",options.load)
    plottingPurpose.writeResult(sum(totalCOemision), sum(totalCO2emision), sum(totalWaitingtimeFrom), sum(detQueueLength) * 1000, crossedCars / step, options.controller + options.step + "-" + options.load, True)
    sys.stdout.flush()


def get_options(controllerNameEx,cases):
    optParser = optparse.OptionParser()
    controllerName = ("Intelligent","Fixed-Time","Actuated")
    optParser.add_option("--nogui", action="store_true",
                         default=True, help="run the commandline version of sumo")
    optParser.add_option("--controller", type="string", dest="controller", default= controllerNameEx)
    optParser.add_option("--step", type="string", dest="step", default="7200")
    optParser.add_option("--load", type="string", dest="load", default=cases)
    options, args = optParser.parse_args()
    return options


# this is the main entry point of this script
if __name__ == "__main__":

    controllerName = ('Fixed-Time', 'Actuated','Intelligent')
    cases = ["Case1Low","Case1Mid","Case1High","Case2","Case3","Case4"]
    # controllerName = [controllerName[1],controllerName[2]]
    # cases = ['Case2','Case3','Case4']
    for c in cases:
        plottingPurpose.writeToFile("results/resultOfExperiments.csv", "----------------------------------------------------" + c +
                         "------------------------------------------------------")
        for i in controllerName:
            options = get_options(i,c)
    # this script has been called from the command line. It will start sumo as a
    # server, then connect and run
            if options.nogui:
                sumoBinary = checkBinary('sumo')
            else:
                sumoBinary = checkBinary('sumo-gui')
            # gerenate route for the cases
            generateRouteForTwenty.generate_routefileAhmFiftyOsm(c, "ahm2PhaseOsmFiftyLoop.rou.xml", 278)

    # first, generate the route file for this simulation
    # generate_routefile()

    # this is the normal way of using traci. sumo is started as a
    # subprocess and then the python script connects and runs
    # traci.start(["sumo", "-c", "sim1.sumocfg"], label="sim1")
    # traci.start(["sumo", "-c", "sim2.sumocfg"], label="sim2")
            traci.start([sumoBinary, "-c", "twentyJunctionsAhm/ahm2PhaseOsmLoop.sumocfg","--tripinfo-output", "results/"+options.controller+"Tripfile.xml"],label="static")
    # traci.start([sumoBinary, "-c", "twentyJunctionsAhm/ahm2PhaseOsmLoop.sumocfg", "--tripinfo-output",
    #              "twentyJunctionsAhm/tripinfoInte.xml", "--emission-output", "twentyJunctionsAhm/emiInte.xml"],label="loop")
            run()

