# detector data

areaDetectorFifty = [
    ["T1L0", "T1L1","T1R0", "T1R1", "T1R2", "T1R3", "T1R4", "T1R5", "T1R6", "T1U0", "T1U1", "T1U2", "T1U3", "T1D0"],
    ["T2L0", "T2L1", "T2L2", "T2L3", "T2L4", "T2L5", "T2L6", "T2R0", "T2R1", "T2R2", "T2R3", "T2R4", "T2U0", "T2D0", "T2D1", "T2D2", "T2D3"],
    ["T3L0", "T3L1", "T3L2", "T3L3", "T3R0", "T3R1", "T3R2", "T3R3", "T3R4", "T3R5", "T3U0", "T3D0", "T3D1"],
    ["T4L0", "T4L1", "T4R0", "T4R1", "T4U0", "T4U1", "T4D0", "T4D1"],
    ["T18L0", "T18R0", "T18U0", "T18U1", "T18D0", "T18D1", "T18D2"],
    ["T5L0", "T5L1", "T5L2", "T5L3", "T5L4", "T5L5", "T5L6", "T5L7", "T5L8", "T5L9", "T5R0","T5R1", "T5U0", "T5U1", "T5D0", "T5D1", "T5D2","T5D3"], # 6 traffic light
    ["T6L0", "T6L1", "T6L2", "T6L3", "T6L4", "T6R0", "T6R1", "T6U0", "T6U0", "T6D0", "T6D1", "T6D2"],
    ["T7L0", "T7L1", "T7L2", "T7R0", "T7R1", "T7R2", "T7U0", "T7U1", "T7D0", "T7D1", "T7D2"],
    ["T8L0", "T8L1", "T8R0", "T8R1", "T8R2", "T8U0", "T8D0", "T8D1"],
    ["T9L0", "T9L1", "T9L2", "T9L3", "T9R0", "T9R1", "T9R2", "T9R3", "T9U0", "T9U1", "T9U2", "T9U3", "T9D0", "T9D1","T9D2", "T9D3", "T9D4"], # 10th traffic light

    ["T10L0", "T10L1", "T10R0", "T10R1", "T10U0", "T10U1", "T10D0", "T10D1", "T10D2", "T10D3"],
    ["T11L0", "T11R0", "T11R1", "T11U0", "T11U1","T11U2", "T11U3", "T11D0", "T11D1"], # 12th tl
    ["T12L0","T12L1", "T12R0", "T12R1", "T12U0", "T12U1", "T12U2", "T12D0", "T12D1", "T12D2", "T12D3", "T12D4", "T12D5"], # 13th tl len = 13
    ["T14L0", "T14L1", "T14R0", "T14R1", "T14R2", "T14R3", "T14U0", "T14U1", "T14U2", "T14U3", "T14U4", "T14U5","T14D0", "T14D1", "T14D2", "T14D3"],
    ["T15L0", "T15L1", "T15R0", "T15R1", "T15R2", "T15U0", "T15U1", "T15U2", "T15D0", "T15D1", "T15D2"],
    ["T16L0", "T16L1", "T16L2", "T16L3", "T16L4", "T16L5", "T16L6", "T16L7", "T16L8", "T16L9", "T16L10", "T16L11", "T16L12", "T16R0", "T16R1", "T16R2", "T16R3", "T16R4", "T16R5", "T16R6", "T16R7",
     "T16U0", "T16U1", "T16U2", "T16U3", "T16U4", "T16U5", "T16U6", "T16U7","T16D0", "T16D1", "T16D2", "T16D3", "T16D4", "T16D5", "T16D6", "T16D7", "T16D8"], # 16th tl
    ["T17L0", "T17L1", "T17L2", "T17L3", "T17L4","T17L5","T17L6","T17L7","T17L8","T17L9","T17L10", "T17R0", "T17R1", "T17R2", "T17U0", "T17U1", "T17D0", "T17D1", "T17D2", "T17D3", "T17D4", "T17D5"], # 17th tl len = 22
    ["T19L0", "T19L1", "T19L2", "T19L3", "T19R0","T19R1","T19R2", "T19U0", "T19U1", "T19D0", "T19D1", "T19D2", "T19D3"],
    ["T13L0", "T13L1", "T13L2", "T13R0", "T13R1", "T13U0", "T13U1", "T13D0", "T13D1", "T13D2", "T13D3", "T13D4","T13D5", "T13D6"],
    ["T20L0", "T20L1", "T20L2", "T20L3", "T20R0", "T20U0", "T20U1", "T20D0", "T20D1", "T20D2", "T20D3", "T20D4","T20D5"]

]

areaDetectorFiftySeqIndex = [[0, 1, 2, 8, 9, 13, 13, 14],
                             [0, 7, 7, 11, 12, 13, 13, 15],
                             [0, 4, 4, 10, 10, 11, 11, 13],
                             [0, 2, 2, 4, 4, 6, 6, 8],
                             [0, 1, 1, 2, 2, 4, 4, 7],
                             [0, 6, 10, 12, 12,14, 14, 17], # 6th tl
                             [0, 5, 5, 7, 7, 9, 9, 12],
                             [0, 3, 3, 6, 6, 8, 8, 10],
                             [0, 2, 2, 5, 5, 6, 6, 11],
                             [0, 3, 4, 8, 8, 10, 12, 14], # 10th tl len 17
                             [0, 2, 2, 4, 4, 6, 6, 8],

                             [0, 1, 1, 3, 3, 5, 7, 9], # 12th tl
                             [0, 1, 2, 4, 4, 6, 7, 11], # 13th tl

                             [0, 2, 2, 6, 6, 12, 12, 16],
                             [0, 2, 2, 5, 5, 8, 8, 11],
                             [0, 10, 13, 19, 21, 27, 29, 35],
                             [0, 9, 11, 14, 14, 16, 16, 22], #17th tl

                             [0, 4, 4, 7, 7, 9, 9, 13],
                             [0, 3, 3, 5, 5, 7, 7, 15],
                             [0, 4, 4, 5, 5, 7, 7, 13]

                             ]

loopDetectorFifity = [
    ["T1L0L", "T1R0L", "T1U0L", "T1D0L"],
    ["T2L0L", "T2R0L", "T2U0L", "T2D0L"],
    ["T3L0L", "T3R0L", "T3U0L", "T3D0L"],
    ["T4L0L", "T4L1L", "T4R0L", "T4U0L", "T4D0L"],
    ["T18L0L", "T18R0L", "T18U0L", "T18D0L"],
    ["T5L0L", "T5R0L", "T5U0L", "T5U1L", "T5D0L", "T5D1L"],
    ["T6L0L", "T6R0L", "T6U0L", "T6D0L"],
    ["T7L0L", "T7R0L", "T7U0L", "T7D0L"],
    ["T8L0L", "T8R0L", "T8U0L", "T8D0L"],
    ["T9L0L", "T9R0L", "T9U0L", "T9D0L"],
    ["T10L0L", "T10R0L", "T10U0L", "T10D0L"],
    ["T11L0L", "T11R0L", "T11U0L", "T11D0L"],
    ["T12L0L", "T12R0L", "T12U0L", "T12D0L"],
    ["T14L0L", "T14R0L", "T14U0L", "T14D0L"],
    ["T15L0L", "T15R0L", "T15U0L", "T15D0L"],
    ["T16L0L", "T16R0L", "T16U0L", "T16D0L"],
    ["T17L0L", "T17R0L", "T17U0L", "T17D0L"],
    ["T19L0L", "T19R0L", "T19U0L", "T19D0L"],
    ["T13L0L", "T13R0L", "T13U0L", "T13D0L"],
    ["T20L0L", "T20R0L", "T20U0L", "T20D0L"]
]

loopDetectorFiftySeqIndex = [[0, 1, 1, 2, 2, 3, 3, 4],
                             [0, 1, 1, 2, 2, 3, 3, 4],
                             [0, 1, 1, 2, 2, 3, 3, 4],
                             [0, 2, 2, 3, 3, 4, 4, 5],
                             [0, 1, 1, 2, 2, 3, 3, 4],
                             [0, 1, 1, 2, 2, 4, 4, 6],
                             [0, 1, 1, 2, 2, 3, 3, 4],
                             [0, 1, 1, 2, 2, 3, 3, 4],
                             [0, 1, 1, 2, 2, 3, 3, 4],
                             [0, 1, 1, 2, 2, 3, 3, 4],
                             [0, 1, 1, 2, 2, 3, 3, 4],

                             [0, 1, 1, 2, 2, 3, 3, 4],
                             [0, 1, 1, 2, 2, 3, 3, 4],

                             [0, 1, 1, 2, 2, 3, 3, 4],
                             [0, 1, 1, 2, 2, 3, 3, 4],
                             [0, 1, 1, 2, 2, 3, 3, 4],
                             [0, 1, 1, 2, 2, 3, 3, 4],

                             [0, 1, 1, 2, 2, 3, 3, 4],
                             [0, 1, 1, 2, 2, 3, 3, 4],
                             [0, 1, 1, 2, 2, 3, 3, 4]

                             ]
loopAreaDetectorFifity = [
    ["T1U0LA", "T1D0LA"], ["T2U0LA", "T2D0LA"], ["T3U0LA", "T3D0LA"], ["T4U0LA", "T4D0LA"],
    ["T18U0LA", "T18D0LA"], ["T5U0LA", "T5U1LA"], ["T6U0LA", "T6D0LA"], ["T7U0LA", "T7D0LA"], ["T8U0LA", "T8D0LA"],
    ["T9U0LA", "T9D0LA"], ["T10U0LA", "T10D0LA"], ["T11U0LA", "T11D0LA"], ["T12U0LA", "T12D0LA"],
    ["T14U0LA", "T14D0LA"], ["T15D0LA", "T15D1LA"], ["T16U0LA", "T16D0LA"],
    ["T17U0LA", "T17D0LA"], ["T19U0LA", "T19D0LA"], ["T13U0LA", "T13D0LA"], ["T20U0LA", "T20D0LA"]
]

# throughputLoopDetectors = []
throughputLoopDetectors = ["T1L0TP", "T1R0TP", "T1U0TP", "T1D0TP", "T2L0TP", "T2R0TP", "T2U0TP", "T2U1TP", "T2D0TP",
                           "T3L0TP", "T3L1TP", "T3R0TP", "T3R1TP", "T3U0TP", "T3D0TP", "T4L0TP", "T4L1TP", "T4R0TP",
                           "T4R1TP", "T4U0TP", "T4U1TP", "T4D0TP", "T4D1TP",
                           "T5L0TP", "T5R0TP", "T5U0TP", "T5D0TP", "T6L0TP", "T6R0TP", "T6U0TP", "T6U1TP", "T6D0TP",
                           "T6D1TP", "T7L0TP", "T7L1TP", "T7L2TP", "T7R0TP", "T7R1TP", "T7U0TP", "T7U1TP", "T7D0TP",
                           "T8L0TP", "T8L1TP", "T8L2TP", "T8R0TP", "T8R1TP", "T8R2TP", "T8R3TP", "T8R4TP", "T8U0TP",
                           "T8D0TP", "T9L0TP", "T9L1TP", "T9L2TP", "T9R0TP", "T9R1TP", "T9R2TP", "T9R3TP", "T9U0TP",
                           "T9D0TP", "T10L0TP", "T10L1TP", "T10R0TP", "T10R1TP", "T10U0TP", "T10D0TP",
                           "T11L0TP", "T11R0TP", "T11R1TP", "T11U0TP", "T11U1TP", "T11D0TP", "T11D1TP", "T12L0TP",
                           "T12R0TP", "T12U0TP", "T12U1TP", "T12D0TP", "T12D1TP", "T13L0TP", "T13R0TP", "T13U0TP",
                           "T13U1TP", "T13D0TP", "T13D1TP",
                           "T14L0TP", "T14L1TP", "T14R0TP", "T14R1TP", "T14U0TP", "T14U1TP", "T14D0TP", "T14D1TP",
                           "T15L0TP", "T15L1TP", "T15R0TP", "T15U0TP", "T15D0TP", "T16L0TP", "T16R0TP", "T16U0TP",
                           "T16U1TP", "T16D0TP", "T16D1TP",
                           "T17L0TP", "T17L1TP", "T17R0TP", "T17R1TP", "T17U0TP", "T17U1TP", "T17D0TP", "T17D1TP",
                           "T18L0TP", "T18R0TP", "T18U0TP", "T18U1TP", "T18D0TP", "T18D1TP", "T19L0TP", "T19R0TP",
                           "T19U0TP", "T19U1TP", "T19D0TP", "T19D1TP",
                           "T20L0TP", "T20L1TP", "T20R0TP", "T20R1TP"]

trafficLightId_1 = "1795602693"
trafficLightId_2 = "cluster_1795602698_440340101"
trafficLightId_3 = "cluster_5705300443_5707374694"
trafficLightId_4 = "cluster_1795602697_440015660_cluster_1830940470_1830940523"
trafficLightId_5 = "3298363480"
trafficLightId_6 = "cluster_1795625115_1795625117"
trafficLightId_7 = "cluster_1795593252_1795660548_1795660551_429411527"
trafficLightId_8 = "cluster_1795660545_429411937"
trafficLightId_9 = "cluster_1795660539_429411934"
trafficLightId_10 = "gneJ1"
trafficLightId_11 = "cluster_1795331917_1795331933_1795331951_1795331966_1812421829_1812421850"
trafficLightId_12 = "cluster_1795331914_1795331946"
trafficLightId_13 = "cluster_1794167825_1794502216_1794502217_325100428"
trafficLightId_14 = "cluster_1781899625_1781899631_1781899653_1781899657_1781899661_1785973104_1785973109_1785977741"
trafficLightId_15 = "cluster_1785867743_1785954129_1830940563"
trafficLightId_16 = "cluster_1782753352_1782753365_cluster_1782753348_1812355769_cluster_1782753361_1812355760"
trafficLightId_17 = "cluster_1467956792_1467956793_1467956795_1467956807_1467956810_1788572633"
trafficLightId_18 = "cluster_1779233835_1779233836_1779233837_1779233845_1779233846_1779233849"
trafficLightId_19 = "cluster_1827200290_1827200304"
trafficLightId_20 = "cluster_1779290710_1779290714_1779290730_1779290747_1779290749_1779290751_1779290760_1779290763_1779290765_1794363667_429001648_429001650_429438542"

trafficLightId = [trafficLightId_1,trafficLightId_2,trafficLightId_3,trafficLightId_4,trafficLightId_5,trafficLightId_6,trafficLightId_7,trafficLightId_8,trafficLightId_9,trafficLightId_10,
                  trafficLightId_11,trafficLightId_12,trafficLightId_13,trafficLightId_14,trafficLightId_15,trafficLightId_16,trafficLightId_17,trafficLightId_18,trafficLightId_19,trafficLightId_20]


# def runStratego(com, args, query):
#     # print ('calling stratego with command: ' + com + args + query )
#     # start_time = time.time()
#     f = os.popen(com+args+query)
#     out = f.read()
#     # total_time = time.time() - start_time
#     return out

# t = np.arange(0.0, 2.0, 0.01)
# s = 1 + np.sin(2 * np.pi * t)
# # ysample = random.sample(range(0, 500), 250)
# # print("ysample:",ysample)
# xdata = []
# ydata = []
# x1data = []
# y1data = []
#
# def oneTimePlotIntialization(x_end,y_end):
#     plt.show()
#     axes = plt.gca()
#     axes.set_xlim(0, x_end)
#     axes.set_ylim(0, y_end)
#     line, = axes.plot(xdata, ydata, 'r-')
#     line1, = axes.plot(x1data, y1data, 'g-')
#     return line,line1
#
# def plotGraph(x_data,y_data,x1_data,y1_data,line,line1):
#
#     xdata.append(x_data)
#     ydata.append(y_data)
#
#     x1data.append(x1_data)
#     y1data.append(y1_data)
#
#     line.set_xdata(xdata)
#     line.set_ydata(ydata)
#
#
#     line1.set_xdata(x1data)
#     line1.set_ydata(y1data)
#
#     plt.draw()
#     plt.pause(1e-17)
#     time.sleep(0.1)

def extend(ext, bound, extTime):
    ext = ext + extTime
    return ext

#     def loopController(trlId, phaseNS, phaseToNS, phaseWE, phaseToEW, maxGreenNS, maxGreenEW, yellow, ic_minGreen,
#                        phaseNow, timeInPhaseNow, phaseTimeNow, count_timeNow, nextPhaseNow, loopDet, areaDet):
#         # print("I am here Max green time:",trlId,maxGreenEW[trlId], maxGreenNS[trlId])
#         # print("Current green time: pahse ",phaseNow,timeInPhaseNow)
#         if phaseNow == phaseNS[trlId] or phaseNow == phaseWE[trlId]:  # we controll the green time
#             traci.trafficlights.setPhaseDuration(trafficLightId[trlId], 5000)
#         loopDetInfo = loopDet
#         areDetInfo = areaDet
#         if phaseNow == phaseNS[trlId]:  # Green in B direction
#             if timeInPhaseNow >= maxGreenNS[trlId] or phaseTimeNow <= 0:
#                 # Goto yellow
#                 traci.trafficlights.setPhase(trafficLightId[trlId], phaseToEW[trlId])
#                 phaseNow = phaseToEW[trlId]
#                 nextPhaseNow = phaseWE[trlId]
#                 timeInPhaseNow = 0
#             else:  # Check if we shoud extend the phase timer
#                 phaseTimeNow -= 1
#                 if loopDetInfo[2] >= 1 or loopDetInfo[3] >= 1:
#                     phaseTimeNow = extend(phaseTimeNow, maxGreenNS[trlId], 4.0)
#                 cars_on_AreDet = sum(areDetInfo) > 0
#                 if cars_on_AreDet:  # Make sure the time ticks while we stay in one phase
#                     phaseTimeNow += 1
#             timeInPhaseNow += 1
#         elif phaseNow == phaseWE[trlId]:  # Green in A direction
#             if timeInPhaseNow >= maxGreenEW[trlId] or phaseTimeNow <= 0:
#                 # Goto yellow
#                 traci.trafficlights.setPhase(trafficLightId[trlId], phaseToNS[trlId])
#                 phaseNow = phaseToNS[trlId]
#                 nextPhaseNow = phaseNS[trlId]
#                 timeInPhaseNow = 0
#             else:
#                 cars_on_AreDet = sum(areDetInfo) > 0
#                 if loopDetInfo[2] == 1 or loopDetInfo[3] == 1 or cars_on_AreDet:
#                     count_timeNow = True
#                 if count_timeNow:  # This phase is the resting phase
#                     if loopDetInfo[0] == 1 or loopDetInfo[2] == 1:
#                         phaseTimeNow = extend(phaseTimeNow, maxGreenEW[trlId], 4.0)
#                     if loopDetInfo[0] == 1 or loopDetInfo[1] == 1:
#                         phaseTimeNow = extend(phaseTimeNow, maxGreenEW[trlId], 4.0)
#                     timeInPhaseNow += 1
#                     phaseTimeNow -= 1
#         else:  # In yellow
#             if timeInPhaseNow == yellow[trlId]:
#                 # At the end of yellow the timeing variables are reset, the min green time is 10
#                 timeInPhaseNow = 0
#                 phaseTimeNow = ic_minGreen[trlId]
#                 phaseNow = nextPhaseNow
#                 traci.trafficlights.setPhase(trafficLightId[trlId], phaseNow)
#                 # traci.trafficlights.setPhaseDuration(idTL, 60)
#                 count_timeNow = False
#             else:
#                 timeInPhaseNow += 1
#         # if options.debug:
#         #     print("Using the loop controller")
#         #     print("Phase in loop controller: ", phase)
#         #     print_dets_state("ic_infLoopDet", ic_loopDet, ic_infLoopDet)
#         #     print_dets_state("ic_infAreDet", ic_areDet, ic_infAreDet)
#         #     print("MaxGreeninA:" + str(timeInPhase))
#         #     print("MaxGreeninA:" + str(phaseTime))
#         #     print(phase)
#
#         phase[trlId] = phaseNow
#         nextPhase[trlId] = nextPhaseNow
#         phaseTime[trlId] = phaseTimeNow
#         timeInPhase[trlId] = timeInPhaseNow
#         count_time[trlId] = count_timeNow
#
#         # return phaseNow
#
#
# def loopControllerTest(trlId, phaseNS, phaseToNS, phaseWE, phaseToEW, maxGreenNS, maxGreenEW, yellow, ic_minGreen,
#                        phaseNow, timeInPhaseNow, phaseTimeNow, count_timeNow, nextPhaseNow, loopDet, areaDet):
#     # print("I am here Max green time:",trlId,maxGreenEW[trlId], maxGreenNS[trlId])
#     # print("Current green time: pahse ",phaseNow,timeInPhaseNow)
#     if phaseNow == phaseNS[trlId] or phaseNow == phaseWE[trlId]:  # we controll the green time
#         traci.trafficlights.setPhaseDuration(trafficLightId[trlId], 5000)
#     loopDetInfo = loopDet
#     areDetInfo = areaDet
#     if phaseNow == phaseWE[trlId]:  # Green in B direction
#         if timeInPhaseNow >= maxGreenEW[trlId] or phaseTimeNow <= 0:
#             # Goto yellow
#             traci.trafficlights.setPhase(trafficLightId[trlId], phaseToNS[trlId])
#             phaseNow = phaseToNS[trlId]
#             nextPhaseNow = phaseNS[trlId]
#             timeInPhaseNow = 0
#         else:  # Check if we shoud extend the phase timer
#             phaseTimeNow -= 1
#             if loopDetInfo[0] >= 1 or loopDetInfo[1] >= 1:
#                 phaseTimeNow = extend(phaseTimeNow, maxGreenEW[trlId], 4.0)
#             cars_on_AreDet = sum(areDetInfo) > 0
#             if cars_on_AreDet:  # Make sure the time ticks while we stay in one phase
#                 phaseTimeNow += 1
#         timeInPhaseNow += 1
#     elif phaseNow == phaseNS[trlId]:  # Green in A direction
#         if timeInPhaseNow >= maxGreenNS[trlId] or phaseTimeNow <= 0:
#             # Goto yellow
#             traci.trafficlights.setPhase(trafficLightId[trlId], phaseToEW[trlId])
#             phaseNow = phaseToEW[trlId]
#             nextPhaseNow = phaseWE[trlId]
#             timeInPhaseNow = 0
#         else:
#             cars_on_AreDet = sum(areDetInfo) > 0
#             if loopDetInfo[0] == 1 or loopDetInfo[1] == 1 or cars_on_AreDet:
#                 count_timeNow = True
#             if count_timeNow:  # This phase is the resting phase
#                 if loopDetInfo[2] == 1 or loopDetInfo[3] == 1:
#                     phaseTimeNow = extend(phaseTimeNow, maxGreenNS[trlId], 4.0)
#                 if loopDetInfo[2] == 1 or loopDetInfo[3] == 1:
#                     phaseTimeNow = extend(phaseTimeNow, maxGreenNS[trlId], 4.0)
#                 timeInPhaseNow += 1
#                 phaseTimeNow -= 1
#     else:  # In yellow
#         if timeInPhaseNow == yellow[trlId]:
#             # At the end of yellow the timeing variables are reset, the min green time is 10
#             timeInPhaseNow = 0
#             phaseTimeNow = ic_minGreen[trlId]
#             phaseNow = nextPhaseNow
#             traci.trafficlights.setPhase(trafficLightId[trlId], phaseNow)
#             # traci.trafficlights.setPhaseDuration(idTL, 60)
#             count_timeNow = False
#         else:
#             timeInPhaseNow += 1
#     # if options.debug:
#     #     print("Using the loop controller")
#     #     print("Phase in loop controller: ", phase)
#     #     print_dets_state("ic_infLoopDet", ic_loopDet, ic_infLoopDet)
#     #     print_dets_state("ic_infAreDet", ic_areDet, ic_infAreDet)
#     #     print("MaxGreeninA:" + str(timeInPhase))
#     #     print("MaxGreeninA:" + str(phaseTime))
#     #     print(phase)
#
#     phase[trlId] = phaseNow
#     nextPhase[trlId] = nextPhaseNow
#     phaseTime[trlId] = phaseTimeNow
#     timeInPhase[trlId] = timeInPhaseNow
#     count_time[trlId] = count_timeNow

    # return phaseNow

# def strategoTrafficLight(trfficLightId,nextPhaseInfo,strategoLocalTimer):
#     if nextPhaseInfo == "0":
#         traci.trafficlight.setPhase(trfficLightId, 2)
#         strategoLocalTimer = strategoLocalTimer - 1
#     if nextPhaseInfo == "1":
#         traci.trafficlight.setPhase(trfficLightId, 0)
#         strategoLocalTimer = strategoLocalTimer - 1
#     if nextPhaseInfo == "2":
#         traci.trafficlight.setPhase(trfficLightId, 3)
#         strategoLocalTimer = strategoLocalTimer - 1
#     return strategoLocalTimer
