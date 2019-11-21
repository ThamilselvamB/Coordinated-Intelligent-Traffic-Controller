import numpy as np
import pandas as pd
import csv
import os
import sys
import optparse
import subprocess
import matplotlib
import webbrowser

from matplotlib import pyplot as plt
from matplotlib import style
if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")
import traci  # noqa
from sumolib import checkBinary
import xml
# print("data:",np.arange(3,61,3))
# fixed =[ 7.00138889 , 7.54666667,  5.00027778,  2.13222222,  6.085 ,      9.63166667,
#   1.93666667 , 5.01361111 , 4.20277778 , 5.33972222 , 3.28027778,  7.32611111,
#   8.02833333 , 4.69277778 , 1.78  ,      8.21833333 , 3.80277778,  2.86166667,
#  14.62555556 ,11.70111111]
# print(fixed)
# tr =[]
# for i in range(21):
#     tr.append("Trf-"+str(i+1))
#
# print(tr)
testing = [4.85,5.83,4.18,2.4,7.16,7.16,3.57,3.85,4.05,6.23,5.23,10.28,10.99,3.89,2.73,8.15,7.09,5.02,5.03,10.02]
print(sum(testing))

#
#
# #---------------------------------------------------------------------------------------------------------------
# def tripInfoWaitingTime():
#     subprocess.call(
#         ['python', os.path.join(tools, 'xml', 'xml2csv.py'), os.path.join("results", "Fixed-Time.xml")])
#     dfFixed = pd.read_csv("results/Fixed-Time.csv", sep=';')
#     wt = dfFixed["tripinfo_waitingTime"]
#     print(wt)
#     print("Tripfile Waiting time:",sum(wt / 3600))
#
# def writingFile(data,colNumber):
#     csvinputlist = ['results/file1.csv']
#     csvinput = csvinputlist
#     headers = ['A', 'B', 'C']  # continue for as many column that are in the file
#     df = pd.DataFrame(data,columns = ['Name','Hello'])
#     # df['A{}'.format(colNumber)] =data
#     # for i, csvinput in enumerate(csvinputlist):
#     #     reader = pd.read_csv(csvinput, header=None, names=headers)
#     #     df['A{}'.format(i + 1)] = reader['B']
#
#     df.to_csv('results/constructed.csv')
#     # dataFrame = {}
#     # df = pd.DataFrame(data)
#     # df.to_csv("results/Testing.csv")
#     # dfFixed = pd.read_csv("results/Testing.csv")

def removeMoreYellow(phaseData):
    data1 = list(phaseData)
    firstIndex = 0
    # print("data original:", data1)
    count = 0
    counting = 0
    for i in range(len(data1)):
        if data1[i] == 3:
            counting = counting +1
            firstIndex = i
            break
    for i in range(firstIndex, len(data1)):
        if data1[i] == 3:
            count = count + 1
        if data1[i] != 3:
            break
    print("count:",count)
    print("index:", firstIndex)
    # next phase after yellow
    nextphase = data1[firstIndex+count+1]
    if count > 5:
        for i in range(count-4):
            data1.pop(firstIndex+count-i)
            data1.insert(firstIndex+count-i,nextphase)

    return np.asarray(data1)


def removeMoreYellow1(phaseData):
    data1 = list(phaseData)
    firstIndex = 0
    # print("data original:", data1)
    count = 0
    counting = []
    for i in range(len(data1)):
        if data1[i]== 3:
            count += 1
        if count>5 and data1[i] == 3:
            data1[i]= 2

    return np.asarray(data1)
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

def CoandCo2(fileName,fileCsv,xmlToCsv,printing):
    # call xml to csv file converter
    milliGramToKg = 1000000
    secondsToHour = 3600
    if xmlToCsv: subprocess.call(['python', os.path.join(tools, 'xml', 'xml2csv.py'), os.path.join(fileName)])
    df = pd.read_csv(fileCsv, sep=';')
    # print("keys:",df.keys())
    coEmission = sum(df['vehicle_CO'])
    co2Emission = sum(df['vehicle_CO2'])
    print("Hi:",co2Emission)
    # waitingTime = sum(df['vehicle_waiting'])
    rowData = [int(coEmission/milliGramToKg),int(co2Emission/milliGramToKg)]
    if printing:
        print("co emission   : %.2f " % round(coEmission/milliGramToKg,2),"Kiligrams")
        print("co2 emission  : %.2f " % round(co2Emission/milliGramToKg,2),"Kiligrams")
        # print(" Waiting Time : %.2f" % round(waitingTime/secondsToHour,2),"hours")
        # print("Queue length  : %.2f" % round(ql,2),"KiloMeters")
        # print("Throughput    : %.2f" % round(thp,2),"vehicle/seconds")
    writeFile(rowData)

def barChartGraph(fixed,actuated,intelligent):
    # width of the bars
    trfficLights = ['Trf-1', 'Trf-2', 'Trf-3', 'Trf-4', 'Trf-5', 'Trf-6', 'Trf-7', 'Trf-8', 'Trf-9', 'Trf-10', 'Trf-11', 'Trf-12', 'Trf-13', 'Trf-14', 'Trf-15', 'Trf-16', 'Trf-17', 'Trf-18', 'Trf-19', 'Trf-20', 'Trf-21']
    barWidth = 0.25
    mean = [np.around(fixed).mean(),np.around(actuated).mean(),np.around(intelligent).mean()]
    pos = np.arange((20))
    fig, (barChart) = plt.subplots(1, 1)
    barChart.bar(np.arange(20), np.around(fixed),barWidth,label="Fixed-Time",color='red')
    barChart.bar(pos+barWidth, np.around(actuated),barWidth, label="Actuated", color='blue')
    barChart.bar(pos + barWidth+barWidth, np.around(intelligent), barWidth, label="Intelligent", color='green')
    # plt.bar(np.arange(3, 61, 3), np.around(intelligent),width = barWidth,capsize=7, label="Intelligent", color='green')    barChart.legend()
    barChart.legend()
    barChart.set_xlabel('Signalised Intersections')
    barChart.set_ylabel('Waiting Time (Hours)')
    plt.sca(barChart)
    plt.xticks(pos,trfficLights)
    barChart.axhline(mean[0], color='r', linestyle='--',label="Mean Value(Fixed-Time)")
    barChart.axhline(mean[1], color='b', linestyle='--',label="Mean Value(Actuated)")
    barChart.axhline(mean[2], color='g', linestyle='--',label="Mean Value(Intelligent)")
    barChart.set_title('Cumulative Waiting Time')
    barChart.legend()
    barChart.plot()
    # call scatter plot data


    plt.show()
def examplePlot(fixed,actuated,intelligent,barChart):
    # width of the bars
    trfficLights = ['Trf-1', 'Trf-2', 'Trf-3', 'Trf-4', 'Trf-5', 'Trf-6', 'Trf-7', 'Trf-8', 'Trf-9', 'Trf-10', 'Trf-11',
                    'Trf-12', 'Trf-13', 'Trf-14', 'Trf-15', 'Trf-16', 'Trf-17', 'Trf-18', 'Trf-19', 'Trf-20', 'Trf-21']
    barWidth = 0.25
    mean = [np.around(fixed).mean(), np.around(actuated).mean(), np.around(intelligent).mean()]
    pos = np.arange(len(fixed))
    # fig, (scatterChart, lineChart,barChart) = pltNow.subplots(3, 1)
    barChart.plot(pos, fixed, alpha=0.8,label="Fixed-Time", color='red')
    barChart.plot(pos, actuated, alpha=0.8, label="Actuated", color='blue')
    barChart.plot(pos, intelligent, alpha=0.8, label="Intelligent", color='green')
    # plt.bar(np.arange(3, 61, 3), np.around(intelligent),width = barWidth,capsize=7, label="Intelligent", color='green')    barChart.legend()
    # barChart.legend()
    # barChart.set_xlabel('Signalised Intersections')
    # barChart.set_ylabel('Waiting Time (Hour)')
    # plt.sca(barChart)
    # plt.xticks(pos, trfficLights)
    # barChart.axhline(mean[0], color='r', linestyle='--', label="Mean Value(Fixed-Time)")
    # barChart.axhline(mean[1], color='b', linestyle='--', label="Mean Value(Actuated)")
    # barChart.axhline(mean[2], color='g', linestyle='--', label="Mean Value(Intelligent)")
    barChart.set_title('Cumulative Waiting Time')
    barChart.legend()
    barChart.plot()
    plt.show()
def readFromFile(fileName):
    with open(fileName, 'r') as f:
        reader = csv.reader(f)
        your_list = list(reader)
    return np.array(your_list,dtype=float)


def writeFile(row):
    # create file(if no file) and append data
    with open('trafficWaiting.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(row)
    csvFile.close()

def convertToScatter(fileFixed,fileActuated,fileIntelligent,xmlToCsv,groupbyName,operationOnGroup):
    if xmlToCsv: subprocess.call(['python', os.path.join(tools, 'xml', 'xml2csv.py'), os.path.join("results","Fixed-TimeTripfile.xml")])
    if xmlToCsv: subprocess.call(
        ['python', os.path.join(tools, 'xml', 'xml2csv.py'), os.path.join("results", "ActuatedTripfile.xml")])
    if xmlToCsv: subprocess.call(
        ['python', os.path.join(tools, 'xml', 'xml2csv.py'), os.path.join("results", "IntelligentTripfile.xml")])
    dfFixed = pd.read_csv(fileFixed,sep=';')
    dfActuated = pd.read_csv(fileActuated, sep=';')
    dfIntelligent = pd.read_csv(fileIntelligent, sep=';')
    timePerCarsArrival1 = dfFixed[operationOnGroup]
    timePerCarsArrival2 = dfActuated[operationOnGroup]
    timePerCarsArrival3 = dfIntelligent[operationOnGroup]
    print(sum(timePerCarsArrival1))
    fixedWaitingTime = timePerCarsArrival1.values.tolist()
    actuatedWaitingTime = timePerCarsArrival2.values.tolist()
    intelliegntWaitingTime = timePerCarsArrival3.values.tolist()
    return fixedWaitingTime,actuatedWaitingTime,intelliegntWaitingTime

# def convertToScatter():
#     pass
def writingPlottingData(data,controller,case):
    indexex = ['Case1Low','Case1Mid','Case1High','Case2','Case3','Case4']
    df = pd.read_csv("results/"+controller+".csv")
    # print(df)
    df[case] = pd.Series(data)
    df.to_csv("results/"+controller+".csv",index=False)


def plottingFigure(case,xmlToscatter):
    controllers= ['Fixed-Time','Actuated','Intelligent']
    if xmlToscatter:
        operationOnGroup = "tripinfo_waitingTime"
        for control in controllers:
            subprocess.call(['python', os.path.join(tools, 'xml', 'xml2csv.py'), os.path.join("results", control+"Tripfile.xml")])
        # for control in controllers:
        dfFixed = pd.read_csv("results/Fixed-TimeTripfile.csv", sep=';')
        dfActuated = pd.read_csv("results/ActuatedTripfile.csv", sep=';')
        dfIntelligent = pd.read_csv("results/IntelligentTripfile.csv", sep=';')
        timePerCarsArrival1 = dfFixed[operationOnGroup]
        timePerCarsArrival2 = dfActuated[operationOnGroup]
        timePerCarsArrival3 = dfIntelligent[operationOnGroup]
        fixedWaitingTime = timePerCarsArrival1.values.tolist()
        actuatedWaitingTime = timePerCarsArrival2.values.tolist()
        intelliegntWaitingTime = timePerCarsArrival3.values.tolist()
        writingPlottingData(fixedWaitingTime,"Fixed-TimeScatter",case)
        writingPlottingData(actuatedWaitingTime,"ActuatedScatter",case)
        writingPlottingData(intelliegntWaitingTime,"IntelligentScatter",case)
    colors = ("red", "blue", "green")
    scatterParams = ("Vehicle Ids", "Waiting time (Seconds)", "Individual Vehicle Delay")
    lineParams = ("Time(15 seconds)", "Waiting time (Seconds)", "Waiting Time")
    barParams = ("Signalised Intersections","Waiting Time (Hour)","Cumulative Waiting Time")
    trfficLights = ['Trf-1', 'Trf-2', 'Trf-3', 'Trf-4', 'Trf-5', 'Trf-6', 'Trf-7', 'Trf-8', 'Trf-9', 'Trf-10', 'Trf-11', 'Trf-12', 'Trf-13', 'Trf-14', 'Trf-15', 'Trf-16', 'Trf-17', 'Trf-18', 'Trf-19', 'Trf-20', 'Trf-21']
    barWidth = (0.25,0.50,0.75)
    barWidthNow = 0.25
    scatterdata =[]
    linedata = []
    bardata = []
    # collect data from file
    for controller in controllers:
        scatterData = pd.read_csv("results/"+controller+"Scatter.csv")
        lineData = pd.read_csv("results/" + controller + "Line.csv")
        barData = pd.read_csv("results/" + controller + "Bar.csv")
        scatterdata.append(tuple([np.arange(len(scatterData)),scatterData[case]]))
        linedata.append(tuple([np.arange(len(lineData)/30),reduceSize(lineData[case].tolist(),30)]))
        bardata.append(tuple([np.arange(len(barData)),barData[case]]))
    fig, (scatterChart, lineChart,barChart) = plt.subplots(3, 1)
    # plot case wise plot

    for data, color, group in zip(scatterdata, colors, controllers):
        x,y = data
        scatterChart.scatter(x, y, alpha=0.8, c=color, edgecolors='none', s=10, label=group)
        scatterChart.set_xlabel(scatterParams[0])
        scatterChart.set_ylabel(scatterParams[1])
        scatterChart.set_title(scatterParams[2], x=0.88)
        plt.legend(loc=2)
    for data, color, group in zip(linedata, colors, controllers):
        x,y = data
        lineChart.plot(x, y, alpha=0.8, c=color, label=group)
        lineChart.set_xlabel(lineParams[0])
        lineChart.set_ylabel(lineParams[1])
        lineChart.set_title(lineParams[2], x=0.88)
        plt.legend(loc=2)
    for data, color, group, bar in zip(bardata, colors, controllers,barWidth):
        x,y = data
        barChart.bar(x+bar, y,barWidthNow, color=color, label=group)
        barChart.set_xlabel(barParams[0])
        barChart.set_ylabel(barParams[1])
        barChart.set_title(barParams[2],x=0.88)
        plt.sca(barChart)
        plt.xticks(np.arange(20)+0.25, trfficLights)
        # plt.legend(loc=2)
    plt.show()




















    # examplePlot(linedata[0][case],linedata[1][case],linedata[2][case],lineChart)
    # barChartGraph(bardata[0][case],bardata[1][case],bardata[2][case],barChart)
    # plotexample(linedata[case], colors, controllers, True, params[0], params[1], params[2])
    # print("df[]",df['Case1Low'])
    # print(df)
    # print("list items",(linedata[0]['Case1Low']))




# Python program to count max heaps with n distinct keys

MAXN = 105 # maximum value of n here

# dp[i] = number of max heaps for i distinct integers
dp = [0]*MAXN

# nck[i][j] = number of ways to choose j elements
#			 form i elements, no order */
nck = [[0 for i in range(MAXN)] for j in range(MAXN)]

# log2[i] = floor of logarithm of base 2 of i
log2 = [0]*MAXN

# to calculate nCk
def choose(n, k):
	if (k > n):
		return 0
	if (n <= 1):
		return 1
	if (k == 0):
		return 1

	if (nck[n][k] != -1):
		return nck[n][k]

	answer = choose(n - 1, k - 1) + choose(n - 1, k)
	nck[n][k] = answer
	return answer


# calculate l for give value of n
def getLeft(n):
	if (n == 1):
		return 0

	h = log2[n]

	# max number of elements that can be present in the
	# hth level of any heap
	numh = (1 << h) #(2 ^ h)

	# number of elements that are actually present in
	# last level(hth level)
	# (2^h - 1)
	last = n - ((1 << h) - 1)

	# if more than half-filled
	if (last >= (numh // 2)):
		return (1 << h) - 1 # (2^h) - 1
	else:
		return (1 << h) - 1 - ((numh // 2) - last)


# find maximum number of heaps for n
def numberOfHeaps(n):
	if (n <= 1):
		return 1

	if (dp[n] != -1):
		return dp[n]

	left = getLeft(n)
	ans = (choose(n - 1, left) * numberOfHeaps(left)) * (numberOfHeaps(n - 1 - left))
	dp[n] = ans
	return ans


# function to initialize arrays
def solve(n):
	for i in range(n+1):
		dp[i] = -1

	for i in range(n+1):
		for j in range(n+1):
			nck[i][j] = -1

	currLog2 = -1
	currPower2 = 1

	# for each power of two find logarithm
	for i in range(1,n+1):
		if (currPower2 == i):
			currLog2 += 1
			currPower2 *= 2
		log2[i] = currLog2
	return numberOfHeaps(n)



# This code is contributed by ankush_953


if __name__ == "__main__":
    # data = removeMo
    # controllerName = ['Fixed-Time','Actuated','Intelligent']
    # choice = 1
    # coAndCo2 = []
    # # outputToFile("results/" + controllerName[choice] + ".xml", "results/" + controllerName[choice] + ".csv", True, True)
    # for i in controllerName:
    #     coAndCo2.append(CoandCo2("results/"+i+".xml","results/"+i+".csv",True,True))
    # print("Co and Co2 Output",coAndCo2)

    # fixed = readFromFile("results/Fixed-TimeBar.csv")[0]
    # act = readFromFile("results/ActuatedBar.csv")[0]
    # intel = readFromFile("results/IntelligentBar.csv")[0]
    # barChartGraph(fixed,act,intel)
    # Driver code
    # n = 12
    # print(solve(n))

    # plottingFigure('Case3',True)

# # ----------------- Single bar chart  graph ----------------------------------------------------------
#     case = "Case3"
#     controllers= ['Fixed-Time','Actuated','Intelligent']
#     scatterdata = []
#     linedata = []
#     bardata = []
#     for controller in controllers:
#         scatterData = pd.read_csv("results/" + controller + "Scatter.csv")
#         lineData = pd.read_csv("results/" + controller + "Line.csv")
#         barData = pd.read_csv("results/" + controller + "Bar.csv")
#         scatterdata.append(tuple([np.arange(len(scatterData)), scatterData[case]]))
#         linedata.append(tuple([np.arange(len(lineData)), lineData[case]]))
#         bardata.append(tuple([np.arange(len(barData)), barData[case]]))
#     barChartGraph(bardata[0][1],bardata[1][1],bardata[2][1])
#
# #------------------------single line chart graph and scatter plot ----------------------------------------------
#     colors = ("red", "blue", "green")
#     scatterParams = ("Vehicle Ids", "Waiting time (Seconds)", "Individual Vehicle Delay")
#     lineParams = ("Time(seconds)", "Waiting time (Seconds)", "Waiting Time")
#     plotexample(scatterdata, colors, controllers, True, scatterParams[0], scatterParams[1], scatterParams[2])
#     plotexample(linedata, colors, controllers, False, lineParams[0], lineParams[1], lineParams[2])
#
# # ---------------------------------end -----------------------------------------------------------------------

    lineData = pd.read_csv("results/" + 'Intelligent' + "Line.csv")
    print(reduceSize(lineData['Case3'].tolist(),10))
    print(len(reduceSize(lineData['Case3'].tolist(), 10)))
    print((reduceSize(np.arange(120),20)))
    params = ("Vehicle Ids", "Waiting time (Hour)", "Individual Vehicle Delay")
    cases = ['Case1Low','Case1Mid','Case1High','Case2','Case3','Case4']
    for case in cases:
        plottingFigure(case, True)
        # writingPlottingData(np.arange(100000)*3,'IntelligentScatter',case)