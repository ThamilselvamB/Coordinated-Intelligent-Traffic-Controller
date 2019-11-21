import numpy as np
# fig = plt.figure()
# ax1 = fig.add_subplot(1,1,1)
# x = [1,2,3,4,5,6,7,8,9,10]
# y = []
# j = 0
# def animate(i):
#     y = np.random.randint(1,5)
#     # pullData = open("sampleText.txt","r").read()
#     # dataArray = pullData.split('\n')
#     xar = []
#     yar = []
#     # for eachLine in dataArray:
#     #     if len(eachLine)>1:
#     #         x,y = eachLine.split(',')
#     xar.append(x[j])
#     j = j+1
#     yar.append(int(y))
#     ax1.clear()
#     ax1.plot(xar,yar)
# # ani = animation.FuncAnimation(fig, animate, interval=1000)
# # plt.show()
#
#
#
# x = np.arange(9.0)
# y = np.split(x, 3)
# print(x)
# print(y[1])
#
# import pandas as pd
# df = pd.read_csv("data/tripinfo.csv")
# print(df.head())
# print(df[28:48])


import csv
import os
import sys
import optparse
import subprocess
import matplotlib
import webbrowser

if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")
import traci  # noqa
from sumolib import checkBinary
import xml
from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
from os.path import expanduser
home = expanduser("~")
rootDir = os.path.abspath(os.getcwd())
pathToResults = rootDir+"/results/"
def emissionOutput(opt,filePathWithName):
    with open(filePathWithName, 'r') as csvfile:
        # get number of columns
        if opt == "CO":
            opt1 = 1
        if opt == "CO2":
            opt1 = 2
        if opt == "WT":
            opt1 = 17
        co2 = []
        co2int = []
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        header = next(spamreader)
        # header1 = next(spamreader)
        spamreader = filter(None, spamreader)
        for line in spamreader:
            co2.append(line[opt1])
        ' '.join(co2).split()
        for i in range(len(co2)-10):
            co2int.append(float(co2[i]))
            # print("value is:",co2[i])
            # print("value i:",i)
        # print("sum:",float(co2[3])+float(co2[4]))
        # print("Total co2int", sum(co2int))
        return sum(co2int)


def readCsv(csv_file):
    with open(csv_file, 'rb') as csvfile:

        # get number of columns
        for line in csvfile.readlines():
            array = line.split(',')
            first_item = array[0]

        num_columns = len(array)
        csvfile.seek(0)

        reader = csv.reader(csvfile, delimiter=' ')
        included_cols = [1, 2, 6, 7]

    for row in reader:
        content = list(row[i] for i in included_cols)
    return content

def outputToFile(fileName,fileCsv,xmlToCsv,ql,thp,controller,scenario,printing):
    # call xml to csv file converter
    milliGramToKg = 1000000
    secondsToHour = 3600
    if xmlToCsv: subprocess.call(['python', os.path.join(tools, 'xml', 'xml2csv.py'), os.path.join(fileName)])
    df = pd.read_csv(fileCsv, sep=';')
    # print("keys:",df.keys())
    coEmission = sum(df['vehicle_CO'])
    co2Emission = sum(df['vehicle_CO2'])
    waitingTime = sum(df['vehicle_waiting'])
    rowData = [int(coEmission/milliGramToKg),int(co2Emission/milliGramToKg),int(waitingTime/secondsToHour),ql,thp,controller,scenario]
    if printing:
        print("co emission   : %.2f " % round(coEmission/milliGramToKg,2),"Kiligrams")
        print("co2 emission  : %.2f " % round(co2Emission/milliGramToKg,2),"Kiligrams")
        print(" Waiting Time : %.2f" % round(waitingTime/secondsToHour,2),"hours")
        print("Queue length  : %.2f" % round(ql,2),"KiloMeters")
        print("Throughput    : %.2f" % round(thp,2),"vehicle/seconds")
    writeFile(rowData)

def writeResult(coEmission,co2Emission,waitingTime,queueLength,throughput,controller,printing):
    milliGramToKg = 1000000
    secondsToHour = 3600
    meterToKm = 1000
    coEmissionKg = round(coEmission/milliGramToKg,2)
    co2EmissionKg = round(co2Emission/milliGramToKg,2)
    waitingTimeHour = round(waitingTime/secondsToHour,2)
    queueLengthKm = round(queueLength/meterToKm,2)
    throughputVehPerSec = round(throughput,2)
    rowData = [coEmissionKg,co2EmissionKg,waitingTimeHour,queueLengthKm,throughputVehPerSec,controller]
    if printing:
        print("co emission   : %.2f " % coEmissionKg ,"Kiligrams")
        print("co2 emission  : %.2f " % co2EmissionKg,"Kiligrams")
        print("Waiting Time : %.2f" % waitingTimeHour,"hours")
        print("Queue length  : %.2f" % queueLengthKm,"KiloMeters")
        print("Throughput    : %.2f" % throughputVehPerSec,"vehicle/seconds")
    with open('results/resultOfExperiments.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(rowData)
    csvFile.close()
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
                signal[indexSig] = 2
                indexSig += 1
        elif t == 10:
            for j in range(5):
                signal[indexSig] = 0
                indexSig += 1
        elif t == 6:
            for j in range(5):
                signal[indexSig] = 3
                indexSig += 1
    return signal_new,signal
def indexOfMaxAndSum(listItems):
    sumOf = sum(listItems)
    maxValue = max(listItems)
    maxIndex = listItems.index(max(listItems))
    return sumOf,maxValue,maxIndex
def plotGraph(waitingTime1,col1,waitingTime2,col2,plotName,waitingTime3,col3,coorX,coorY):
    x1 = np.arange(len(waitingTime1))
    x2 = np.arange(len(waitingTime2))
    x3 = np.arange(len(waitingTime3))
    waitingTimeS,maxValS,maxIndexS = indexOfMaxAndSum(waitingTime1)
    waitingTimeL,maxValL,maxIndexL = indexOfMaxAndSum(waitingTime2)
    waitingTimeSt,maxValSt,maxIndexSt = indexOfMaxAndSum(waitingTime3)
    # maxIndexS = 100
    # maxValS = 36000
    # maxIndexL = 100
    # maxValL = 35000
    # maxIndexSt = 100
    # maxValSt = 34000
    # maxIndexS = 108
    # maxValS = 48000
    # maxIndexL = 108
    # maxValL = 46000
    # maxIndexSt = 108
    # maxValSt = 44000
    wstA = "Static Total: "+str(waitingTimeS)
    wltA = "Loop Total: " + str(waitingTimeL)
    wsttA = "Stratego Total: " + str(waitingTimeSt)
    # plt.plot(x1, waitingTime1,col1,label='Static')
    # plt.plot(x2, waitingTime2,col2,label='Loop')
    # plt.plot(x3, waitingTime3, col3, label='Stratego')
    plt.scatter(x1, waitingTime1,s=2,label='Fixed-Time')
    plt.scatter(x2, waitingTime2,s=2,label='Actuated')
    plt.scatter(x3, waitingTime3, s=2, label='Intelligent')
    plt.legend()
    # naming the x axis
    plt.xlabel('Time ( 10 min )')
    # naming the y axis
    plt.ylabel('Queue Length ( meters )')
    # plt.ylabel('Waiting Time ( sec )')
    plt.annotate(wstA, xy=(maxIndexS, maxValS), xytext=(maxIndexS+10, maxValS+10),
                arrowprops=dict(facecolor='black', shrink=0.05),)
    plt.annotate(wltA, xy=(maxIndexL, maxValL), xytext=(maxIndexL+10, maxValL+10 ),
                 arrowprops=dict(facecolor='black', shrink=0.05), )
    plt.annotate(wsttA, xy=(maxIndexSt, maxValSt), xytext=(maxIndexSt+10, maxValSt+10),
                 arrowprops=dict(facecolor='black', shrink=0.05), )
    # giving a title to my graph
    plt.title(plotName)
    # plt.text(12,20)
    plt.show()
def reduceSize(listItems,modVal):
    wt = []
    wtt = 0.0
    for i in range(len(listItems)):
        k = i - modVal
        if k % modVal == 0:
            wtt = wtt + listItems[k]
            wt.append(wtt)
            wtt = 0.0
        else:
            wtt = wtt + listItems[k]
    return wt
def waitingTime(wtF,wtA,wtI):
    waitTS =reduceSize(wtF,5)
    waitTL = reduceSize(wtA,5)
    waitTSt = reduceSize(wtI,5)
    # copyFile("data/out.txt","data/stratego.txt")
    # waitTS,jamLenS = calculateWaitingtime('data/static.txt',60)
    # waitTL, jamLenL = calculateWaitingtime('data/loopController.txt', 60)
    # waitTSt, jamLenSt = calculateWaitingtime('data/stratego.txt', 60)
    # print("waitingTime:",sum(waitT))
    # print("q lenth:",sum(jamLen))
    # loopWT, loopQL = calculateWaitingtime('data/e2right.out')
    # copyFile('data/s.txt','data/l.txt')
    plotGraph(waitTS,"r-", waitTL,"g-","Waiting Time",waitTSt,"b-",250,150)
    # plotGraph(jamLenS,"r-",jamLenL,"g-","Queue Length",jamLenSt,"b-",250,350)
    print("waiting time [static]:",sum(waitTS))
    print("waiting time [loop]:", sum(waitTL))
    print("waiting time [stratego]:", sum(waitTSt))

def testing(listData):

    data = webbrowser.open_new_tab(listData)
    return data

def writeFile(row):
    # create file(if no file) and append data
    with open('trafficWaiting.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(row)
    csvFile.close()
def writeFile1(watingTime,QueueLength,throughput,controlName):
    # create file(if no file) and append data
    row1 = [watingTime,QueueLength,throughput,controlName]
    with open('trafficWaiting1.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(row1)
        # writer.writerow(str(controlName))
    csvFile.close()

import pandas as pd

def plotGraph1(fileFixed,fileActuated,fileIntelligent,xmlToCsv):
    if xmlToCsv: subprocess.call(['python', os.path.join(tools, 'xml', 'xml2csv.py'), os.path.join("results","Fixed-TimeTripfile.xml")])
    if xmlToCsv: subprocess.call(
        ['python', os.path.join(tools, 'xml', 'xml2csv.py'), os.path.join("results", "ActuatedTripfile.xml")])
    if xmlToCsv: subprocess.call(
        ['python', os.path.join(tools, 'xml', 'xml2csv.py'), os.path.join("results", "IntelligentTripfile.xml")])
    dfFixed = pd.read_csv(fileFixed,sep=';')
    dfActuated = pd.read_csv(fileActuated, sep=';')
    dfIntelligent = pd.read_csv(fileIntelligent, sep=';')
    # f.to_csv(file, sep=";")
    # Creating the dataframe
    # df = pd.read_csv(file)
    # print(len(f.keys()))
    # # df.drop(labels=keys, axis="columns", inplace=True)
    # newDf = df.set_index(keys)
    # print(df.head())
    # print(newDf.head())
    gk1 = dfFixed.groupby('tripinfo_depart')
    gk2 = dfActuated.groupby('tripinfo_depart')
    gk3 = dfIntelligent.groupby('tripinfo_depart')
    timePerCarsArrival1 = gk1.sum()['tripinfo_waitingTime']
    timePerCarsArrival2 = gk2.sum()['tripinfo_waitingTime']
    timePerCarsArrival3 = gk3.sum()['tripinfo_waitingTime']

    # print(sum(timePerCarsArrival))
    fixedWaitingTime = timePerCarsArrival1.values.tolist()
    actuatedWaitingTime = timePerCarsArrival2.values.tolist()
    intelliegntWaitingTime = timePerCarsArrival3.values.tolist()
    waitingTime(fixedWaitingTime,actuatedWaitingTime,intelliegntWaitingTime)


    # print(timePerCarsArrival)
    # print(durationCars)

    # for i in range(len(timePerCarsArrival)):
    #     print(timePerCarsArrival[i],i)
    #
    # print("list:",durationCars)
    # print(timePerCarsArrival)
    #
    # # Let's print the first entries
    # # in all the groups formed.
    # wt = gk.sum()
    # # print(wt)
    # # print("Waiting time in hour:",sum(wt['vehicle_waiting'])/3600)
    # # print("CO in Kgms:", sum(wt['vehicle_CO']) / 1000)
    # # print("CO2 in Kgms::", sum(wt['vehicle_CO2']) / 1000)
    #
    # print("Waiting time in hour:",sum(df['vehicle_waiting'])/3600)
    # print("CO in Kgms:", sum(df['vehicle_CO']) / 1000)
    # print("CO2 in Kgms::", sum(df['vehicle_CO2']) / 1000)

def plotFigure(fileFixed,fileActuated,fileIntelligent,xmlToCsv,groupbyName,operationOnGroup):
    if xmlToCsv: subprocess.call(['python', os.path.join(tools, 'xml', 'xml2csv.py'), os.path.join("results","Fixed-TimeTripfile.xml")])
    if xmlToCsv: subprocess.call(
        ['python', os.path.join(tools, 'xml', 'xml2csv.py'), os.path.join("results", "ActuatedTripfile.xml")])
    if xmlToCsv: subprocess.call(
        ['python', os.path.join(tools, 'xml', 'xml2csv.py'), os.path.join("results", "IntelligentTripfile.xml")])
    dfFixed = pd.read_csv(fileFixed,sep=';')
    dfActuated = pd.read_csv(fileActuated, sep=';')
    dfIntelligent = pd.read_csv(fileIntelligent, sep=';')
    # gk1 = dfFixed.groupby(groupbyName)
    # gk2 = dfActuated.groupby(groupbyName)
    # gk3 = dfIntelligent.groupby(groupbyName)
    # timePerCarsArrival1 = gk1.sum()[operationOnGroup]
    # timePerCarsArrival2 = gk2.sum()[operationOnGroup]
    # timePerCarsArrival3 = gk3.sum()[operationOnGroup]

    timePerCarsArrival1 = dfFixed[operationOnGroup]
    timePerCarsArrival2 = dfActuated[operationOnGroup]
    timePerCarsArrival3 = dfIntelligent[operationOnGroup]
    print(sum(timePerCarsArrival1))
    fixedWaitingTime = timePerCarsArrival1.values.tolist()
    actuatedWaitingTime = timePerCarsArrival2.values.tolist()
    intelliegntWaitingTime = timePerCarsArrival3.values.tolist()
    # waitingTime(fixedWaitingTime,actuatedWaitingTime,intelliegntWaitingTime)
    return fixedWaitingTime,actuatedWaitingTime,intelliegntWaitingTime
def plotFigureLine(fileFixed,fileActuated,fileIntelligent,xmlToCsv,groupbyName,operationOnGroup):
    if xmlToCsv: subprocess.call(['python', os.path.join(tools, 'xml', 'xml2csv.py'), os.path.join("results","Fixed-TimeTrip.xml")])
    if xmlToCsv: subprocess.call(
        ['python', os.path.join(tools, 'xml', 'xml2csv.py'), os.path.join("results", "Actuated.xml")])
    if xmlToCsv: subprocess.call(
        ['python', os.path.join(tools, 'xml', 'xml2csv.py'), os.path.join("results", "Intelligent.xml")])
    dfFixed = pd.read_csv(fileFixed,sep=';')
    dfActuated = pd.read_csv(fileActuated, sep=';')
    dfIntelligent = pd.read_csv(fileIntelligent, sep=';')
    gk1 = dfFixed.groupby(groupbyName)
    gk2 = dfActuated.groupby(groupbyName)
    gk3 = dfIntelligent.groupby(groupbyName)
    timePerCarsArrival1 = gk1.sum()[operationOnGroup]
    timePerCarsArrival2 = gk2.sum()[operationOnGroup]
    timePerCarsArrival3 = gk3.sum()[operationOnGroup]

    timePerCarsArrival1 = dfFixed[operationOnGroup]
    timePerCarsArrival2 = dfActuated[operationOnGroup]
    timePerCarsArrival3 = dfIntelligent[operationOnGroup]
    print(sum(timePerCarsArrival1))
    fixedWaitingTime = timePerCarsArrival1.values.tolist()
    actuatedWaitingTime = timePerCarsArrival2.values.tolist()
    intelliegntWaitingTime = timePerCarsArrival3.values.tolist()
    # waitingTime(fixedWaitingTime,actuatedWaitingTime,intelliegntWaitingTime)
    return fixedWaitingTime,actuatedWaitingTime,intelliegntWaitingTime

def plotexample(data,colors,controllers,scatterPlot,x_axis,y_axis,plotName):
    data = data
    colors = colors
    groups = controllers
    # Create plot
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, facecolor='1.0')
    for data, color, group in zip(data, colors, groups):
        x, y = data
        if scatterPlot: ax.scatter(x, y, alpha=0.8, c=color, edgecolors='none', s=10, label=group)
        else: ax.plot(x, y, alpha=0.8, c=color,label=group)
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    plt.title(plotName)
    plt.legend(loc=2)
    plt.show()

def writeToFile(fileName,data):
    row = [data]
    with open(fileName, 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(row)
        # writer.writerow(str(controlName))
    csvFile.close()
def readFromFile(fileName):
    with open(fileName, 'r') as f:
        reader = csv.reader(f)
        your_list = list(reader)
    return np.array(your_list,dtype=float)

def barChartGraph(fixed,actuated,intelligent):
    # width of the bars
    trfficLights = ['Trf-1', 'Trf-2', 'Trf-3', 'Trf-4', 'Trf-5', 'Trf-6', 'Trf-7', 'Trf-8', 'Trf-9', 'Trf-10', 'Trf-11', 'Trf-12', 'Trf-13', 'Trf-14', 'Trf-15', 'Trf-16', 'Trf-17', 'Trf-18', 'Trf-19', 'Trf-20', 'Trf-21']
    barWidth = 0.25
    mean = [np.around(fixed).mean(),np.around(actuated).mean(),np.around(intelligent).mean()]
    pos = np.arange((20))
    plt.bar(np.arange(20), np.around(fixed),barWidth,label="Fixed-Time",color='red')
    plt.bar(pos+barWidth, np.around(actuated),barWidth, label="Actuated", color='blue')
    plt.bar(pos + barWidth+barWidth, np.around(intelligent), barWidth, label="Intelligent", color='green')
    # plt.bar(np.arange(3, 61, 3), np.around(intelligent),width = barWidth,capsize=7, label="Intelligent", color='green')
    plt.legend()
    plt.xlabel('Signalised Intersections')
    plt.ylabel('Waiting Time (Hour)')
    plt.xticks(pos,trfficLights)
    plt.axhline(mean[0], color='r', linestyle='--',label="Mean Value(Fixed-Time)")
    plt.axhline(mean[1], color='b', linestyle='--',label="Mean Value(Actuated)")
    plt.axhline(mean[2], color='g', linestyle='--',label="Mean Value(Intelligent)")
    plt.legend()
    plt.title('Cumulative Waiting Time')
    plt.show()

def testbar():
    city = ['Delhi', 'Beijing', 'Washington', 'Tokyo', 'Moscow']
    Gender = ['Male', 'Female']
    pos = np.arange(len(city))
    bar_width = 0.35
    Happiness_Index_Male = [60, 40, 70, 65, 85]
    Happiness_Index_Female = [30, 60, 70, 55, 75]

    plt.bar(pos, Happiness_Index_Male, bar_width, color='blue', edgecolor='black')
    plt.bar(pos + bar_width, Happiness_Index_Female, bar_width, color='pink', edgecolor='black')
    plt.xticks(pos, city)
    plt.xlabel('City', fontsize=16)
    plt.ylabel('Happiness_Index', fontsize=16)
    plt.title('Group Barchart - Happiness index across cities By Gender', fontsize=18)
    plt.legend(Gender, loc=2)
    plt.show()


if __name__ == "__main__":
    colors = ("red", "blue", "green")
    controllerNames = ("Fixed-Time", "Actuated", "Intelligent")
    #
    #
    # # # For each vehicle waiting time on scatter plot
    dataList = []
    params = ("Vehicle Ids","Waiting time (Hour)","Individual Vehicle Delay")
    groups = plotFigure("results/Fixed-TimeTripfile.csv","results/ActuatedTripfile.csv","results/IntelligentTripfile.csv",True,"vehicle_id","tripinfo_waitingTime")
    for a in range(len(groups)):
        dataList.append(tuple([np.arange(len(groups[a])),np.array(groups[a])/3600]))
        print("inside:",sum(groups[a])/3600)
    # for data in dataList:
    #     dataList
    # For waiting time versus time
    dataListLine = []
    groupsList1 = []
    paramsLine = ("Time(15 seconds)","Waiting time (Hour)","Waiting Time")
    # # groupsList = plotFigure("results/Fixed-TimeTripfile.csv","results/ActuatedTripfile.csv","results/IntelligentTripfile.csv",False,"tripinfo_depart","tripinfo_waitingTime")
    # groupsList = plotFigure("results/Fixed-TimeTripfile.csv", "results/ActuatedTripfile.csv", "results/IntelligentTripfile.csv", False,



    #                     "tripinfo_depart", "tripinfo_waitingTime")
    fixedLine = readFromFile("results/Fixed-TimeLine.csv")[0]
    actLine = readFromFile("results/ActuatedLine.csv")[0]
    intelLine = readFromFile("results/IntelligentLine.csv")[0]
 #    groupsList = [[0, 5, 7, 7, 11, 8, 5, 9, 6, 5, 11, 8, 6, 4, 8, 5, 4, 9, 6, 6, 10, 9, 9, 12, 9, 7, 8, 11, 10, 7, 7, 11, 11, 10, 12, 19, 20, 13, 20, 26, 26, 25, 33, 34, 31, 36, 31, 40, 42, 39, 46, 45, 44, 48, 48, 54, 56, 56, 59, 62, 62, 65, 69, 70, 77, 81, 88, 92, 90, 101, 100, 102, 107, 117, 113, 112, 116, 120, 127, 126, 131, 137, 134, 140, 144, 150, 124, 112, 98, 88, 92, 87, 77, 78, 76, 74, 76, 81, 79, 76, 84],[0, 5, 7, 7, 11, 8, 5, 9, 6, 5, 11, 8, 6, 4, 8, 5, 4, 9, 6, 6, 10, 9, 9, 12, 9, 7, 8, 11, 10, 7, 7, 11, 11, 10, 12, 19, 20, 13, 20, 26, 26, 25, 33, 34, 31, 36, 31, 40, 42, 39, 46, 45, 44, 48, 48, 54, 56, 56, 59, 62, 62, 65, 69, 70, 77, 81, 88, 92, 90, 101, 100, 102, 107, 117, 113, 112, 116, 120, 127, 126, 131, 137, 134, 140, 144, 150, 124, 112, 98, 88, 92, 87, 77, 78, 76, 74, 76, 81, 79, 76, 84],[0, 5, 7, 7, 11, 8, 5, 9, 6, 5, 11, 8, 6, 4, 8, 5, 4, 9, 6, 6, 10, 9, 9, 12, 9, 7, 8, 11, 10, 7, 7, 11, 11, 10, 12, 19, 20, 13, 20, 26, 26, 25, 33, 34, 31, 36, 31, 40, 42, 39, 46, 45, 44, 48, 48, 54, 56, 56, 59, 62, 62, 65, 69, 70, 77, 81, 88, 92, 90, 101, 100, 102, 107, 117, 113, 112, 116, 120, 127, 126, 131, 137, 134, 140, 144, 150, 124, 112, 98, 88, 92, 87, 77, 78, 76, 74, 76, 81, 79, 76, 84]]
    groupsList = [fixedLine,actLine,intelLine]
    for i in range(len(groupsList)):
        groupsList1.append(reduceSize(groupsList[i],15))
    for i in range(len(groupsList)):
        groupsList1[i] = [x / 3600 for x in groupsList1[i]]
    for a in range(len(groupsList1)):
        dataListLine.append(tuple([np.arange(len(groupsList1[a])),groupsList1[a]]))
    # data1 = reduceSize(groupsList[0],30)
    # print("reduce size:",data1)
    # print("reduce size:", len(data1))



 #
 #    fixed = [12.31527778, 7.18027778, 6.10777778, 4.50805556, 10.42222222, 8.43972222,
 #             4.025, 12.57916667, 10.16472222, 10.33277778, 6.46611111, 13.31055556,
 #             13.09722222, 5.21722222, 9.97305556, 8.46361111, 8.29, 9.41805556,
 #             6.11833333, 17.81833333]
 #    act =[ 8.72805556,  6.84888889 , 5.16444444 , 3.36888889, 10.65111111 , 7.09666667,
 #  3.01166667 , 8.76055556  ,6.46055556,  9.06277778,  6.07055556 , 9.51472222,
 # 10.06583333 , 5.38333333,  1.94916667,  7.89444444,  6.625 ,      6.94833333,
 #  5.34555556 , 7.39083333]
 #    intel = [ 7.00138889 , 7.54666667,  5.00027778,  2.13222222,  6.085 ,      9.63166667,
 #  1.93666667 , 5.01361111 , 4.20277778 , 5.33972222 , 3.28027778,  7.32611111,
 #  8.02833333 , 4.69277778 , 1.78  ,      8.21833333 , 3.80277778,  2.86166667,
 # 14.62555556 ,11.70111111]
    fixed= readFromFile("results/Fixed-TimeBar.csv")[0]
    act = readFromFile("results/ActuatedBar.csv")[0]
    intel = readFromFile("results/IntelligentBar.csv")[0]

    # plotexample(dataList,colors,controllerNames,True,params[0],params[1],params[2])
    # plotexample(dataListLine,colors,controllerNames,False,paramsLine[0],paramsLine[1],paramsLine[2])
    barChartGraph(fixed,act,intel)
    # fixedLine = 90
    # writeToFile("results/Fixed-TimeLine.csv",[0, 5, 7, 7, 11, 8, 5, 9, 6, 5, 11, 8, 6, 4, 8, 5, 4, 9, 6, 6, 10, 9, 9, 12, 9, 7, 8, 11, 10, 7, 7, 11, 11, 10, 12, 19, 20, 13, 20, 26, 26, 25, 33, 34, 31, 36, 31, 40, 42, 39, 46, 45, 44, 48, 48, 54, 56, 56, 59, 62, 62, 65, 69, 70, 77, 81, 88, 92, 90, 101, 100, 102, 107, 117, 113, 112, 116, 120, 127, 126, 131, 137, 134, 140, 144, 150, 124, 112, 98, 88, 92, 87, 77, 78, 76, 74, 76, 81, 79, 76, 84])
    # print(readFromFile("results/Fixed-TimeBar.csv")[0])
    # print(type(readFromFile("results/Fixed-TimeBar.csv")[0]))