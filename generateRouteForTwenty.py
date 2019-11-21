from __future__ import absolute_import
from __future__ import print_function

import os
import sys
import optparse
import subprocess
import random
#  "518.38,517.78 501.38,517.78"
# we need to import python modules from the directory
sys.path.append(os.path.join('c:', os.sep, 'usr', 'share', 'sumo', 'tools'))
from sumolib import checkBinary  # import library
import traci
import numpy as np


class Configuration:
    def __init__(self, cases):
        start = 1
        end = 109
        # majorRoad = 1500
        # minorRoad = 750
        # leftTurn = 100
        # crossRoad = 600

        self.cases=cases
        self.tcH = {}
        self.routeH = {}
        self.pH = {}
        if cases == "Case1Low":
            multiplier = 0.3
            majorRoad = 850
            minorRoad = 400
            leftTurn = 100
            crossRoad = 300
        if cases == "Case1Mid":
            multiplier = 0.6
            majorRoad = 850
            minorRoad = 400
            leftTurn = 100
            crossRoad = 300
        if cases == "Case1High":
            multiplier = 1.0
            majorRoad = 850
            minorRoad = 400
            leftTurn = 100
            crossRoad = 300
        if cases == "Case2":
            multiplier = 1.0
            majorRoad = 1600
            minorRoad = 1000
            leftTurn = 100
            crossRoad = 300
        if cases == "Case3":
            multiplier = 1.0
            majorRoad = 850
            minorRoad = 850
            leftTurn = 100
            crossRoad = 300
        if cases == "Case4":
            multiplier = 1.0
            majorRoad = 450
            minorRoad = 750
            leftTurn = 100
            crossRoad = 300

        self.pH1 = np.ones(4)*multiplier * majorRoad / 3600
        self.pH2 = np.ones(18) * multiplier * minorRoad / 3600
        self.pH3 = np.ones(8) * multiplier * crossRoad / 3600
        self.pH4 = np.ones(78) * multiplier * leftTurn / 3600
        self.pH = np.hstack((self.pH1 , self. pH2,self.pH3,self.pH4))
        self.routeH = []
        for i in range(start,end):
            self.routeH.append("route_"+str(i) )
        # self.routeH = ["route_1","route_2","route_3","route_4","route_1","route_1","route_1","route_1","route_1","route_1","route_1","route_1","route_1","route_1","route_1","route_1","route_1","route_1","route_1","route_1",
        #                "route_1","route_1","route_1","route_1","route_1","route_1","route_1","route_1","route_1","route_1","route_1","route_1","route_1","route_1","route_1","route_1","route_1","route_1","route_1","route_1"]

        # self.directions = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12','13','14','15','16','17','18','19','20','1A', '2A', '3A', '4A', '5A', '6A', '7A', '8A', '9A', '10A', '11A', '12A','13A','14A','15A','16A','17A','18A','19A','20A']
        # self.nrDirections = len(self.directions)
#<route id="route_1" edges="168277061#0 168277061#1 168277061#3 168277061#4 168275829 168275547#1 168275547#2 547236215#0 547236215#2 547236215#4 547236215#5 168278390#0 168278390#1 168278390#2 168278390#3 168278390#4 547560317 168278394 168278393#1 168278393#2 168274448#1 168244316#0 168244316#1 168244316#3 168244316#4 168244316#5 168244316#6 168108873#2"/>
def generate_routefileAhmFiftyOsm(cases, outputfile,randomSeed):
    random.seed(randomSeed)  # make tests reproducible
    N = 6500  # number of time steps
    cf = Configuration(cases)
    # print(cf.pH)
    v_Types = ['Bus','Auto','MotorCycle','Car']
    with open("twentyJunctionsAhm/"+outputfile, "w") as routes:
        totalCars = 0;
        print("""<routes>
    <vType id="Bus" accel="0.6" decel="3.5" sigma="0.5" length="14" minGap="1.0" maxSpeed="16.67" guiShape="bus" width="2.5" latAlignment="left" laneChangeModel="SL2015" lcStrategic="0.5" lcCooperative="0.0"/>
    <vType id="Auto" accel="0.7" decel="4.5" sigma="0.5" length="2.6" minGap="0.3" maxSpeed="16" guiShape="passenger/sedan" width="1.3" latAlignment="left" laneChangeModel="SL2015" lcStrategic="0.5" lcCooperative="0.0" />
    <vType id="MotorCycle" accel="0.9" decel="3.5" sigma="0.5" length="2" minGap="0.15" maxSpeed="17" guiShape="motorcycle" width="0.7" latAlignment="left" laneChangeModel="SL2015" lcStrategic="0.5" lcCooperative="0.0"/>
    <vType id="Car" accel="0.8" decel="4.5" sigma="0.5" length="4.5" minGap="0.5" maxSpeed="40" guiShape="passenger" width="2.5" latAlignment="left" laneChangeModel="SL2015" lcStrategic="0.5" lcCooperative="0.0"/>
	<route id="route_1" edges="168277061#0 168277061#1 168277061#3 168277061#4 168275829 168275547#1 168275547#2 547236215#0 547236215#2 -gneE2 gneE3 168244316#0 168244316#1 168244316#3 168244316#4 168244316#5 168244316#6 168108873#2"/>
	<route id="route_2" edges="168108881#1 168108881#3 168244311#1 168244311#2 168244311#4 168244311#5 168244311#6 168244311#7 gneE4 gneE2 168274455#3 168274455#4 168274455#5 168274455#7 547236211#0 547236211#2 547236211#4 168277066#0 168277066#1 168277066#3 168277066#4"/>
	<route id="route_3" edges="167187877#0 167187877#1 167187877#3 167187877#4 167187423#0 167187423#1 167187423#2 167187423#3 -597310870#3 -597310870#2 -597310870#1 -597310870#0 167186116#5 167186119 167178310#0 167178310#1 166851620#0 166851620#1 166851620#2 166851620#3 166851620#4 166851620#5 166851620#6 166479009#0 166479009#1 166478537 167452387#0 167452387#1 167452387#2 167452390#0 167452390#1 167452390#2 167450221 295981931 167449520#0 167449520#1 167449520#2 167449520#3 166481854 166482093#0 166482093#1 166482093#2 166458246#0 166458246#1 166458246#2 166458246#3 166482327#1 166482327#2 166482329#5 166482329#6 166482329#0 166482329#1 166483062#0 166483062#1 166483062#2 166483065 "/>
	<route id="route_4" edges="166483489 166483064 166483066#1 166482329#3 166482330#0 166482330#1 166458245#1 166458245#2 166458245#3 166479614 166481853 167449523#0 167449523#1 166463277 167450224#0 167452383#0 167452383#1 167452383#2 167452383#3 167452383#4 167452384#1 167452384#2 167452384#3 167452384#4 166478539 166479007 166851618#0 166851618#1 166851618#2 166851618#3 166851618#4 167179196#0 167179196#1 167179196#2 167179197 167187424#0 167187424#1 167187421#1 167187421#2 167187421#3 167187880#0 167187880#1 167187880#2 167187880#3 167187880#4 167187880#5"/>
	<route id="route_5" edges="-37573573#15 -37573573#14 -37573573#13 -37573573#12 -37573573#11 -37573573#10 -37573573#9 -37573573#8 -37573573#6 -37573570#2 -37573570#1 -37573570#0 -37573568#1 166735152#1 166735152#2 166735152#3 166735152#4 166735152#5 166746157#0"/>
	<route id="route_6" edges="166747528#1 166747528#2 166747528#3 166747526#0 166747526#1 166747526#2 166747526#3 166746156#0 166746156#1 166741559#0 166741559#1 166741559#2 166741559#3 37573568#1 37573570#0 37573570#1 37573570#2 37573573#6 37573573#8 37573573#9 37573573#10 37573573#11 37573573#12 37573573#13 37573573#14 37573573#15"/>
	<route id="route_7" edges="172156185#3 172156185#4 172156185#5 172156185#6 172156185#7 172156185#8 172156185#9 172156185#11 172156185#12 172156185#13 -37555813#9"/>
	<route id="route_8" edges="-330926753#0 37555813#8 37555813#9 -172156185#13 -172156185#12 -172156185#11 172156192#1 172156192#2 172156192#3 172156192#4 172156192#5 172156192#6 172156192#7 -172156185#5 -172156185#4 -172156185#3"/>
	<route id="route_9" edges="-172156185#0 36927022#1 36927022#2 36927022#3 36927022#4 36927022#5 36927022#6 36927022#7 36927022#8 36927022#9 36927022#10 36927022#12 36927022#13 36927022#14 36927022#15 36927022#16"/>
	<route id="route_10" edges="-167186118#2 -167186118#1 -167186118#0 -36927022#16 -36927022#15 -36927022#14 -36927022#13 -36927022#12 -36927022#10 -36927022#9 -326491697#2 -326491697#1 "/>
    <route id="route_11" edges="168280085#0 168280093#1 168280093#2 168280093#3 168280093#4 547236212#0 547236212#3 168282525#0 168282525#2 168282525#4 168282525#5 168282525#7 168282525#8 168282525#9 168282530 168282633 36927017#1"/>
	<route id="route_12" edges="-168282631#5 -168282631#4 -168282631#3 -168282631#2 -168282631#1 -168282631#0 -168282632#1 -168282632#0 -168282531 -168282525#9 -168282525#8 -168282525#7 -168282525#5 -168282525#4 -168282525#2 -168282525#0 -168282527 547236209#0 547236209#2 -168280085#7 -168280085#5 -168280085#3 -168280085#2 -168280085#1 -168280085#0"/>
	<route id="route_13" edges="gneE5 gneE7 gneE9 547560322#3 547560322#4 547560322#5 547560322#6 547560322#7 547560322#8 547560322#9 167463858#0 167463858#1 167463858#2 167463858#3 167463858#4 167463858#6 -336337523"/>
	<route id="route_14" edges="334995861 167463857#4 93713967#0 93713967#1 93713967#2 93713967#3 93713967#4 93713967#5 gneE8 gneE6"/>
	<route id="route_15" edges="310698683#1 310698680#2 167466938#1 167466938#3 167466938#4 167466938#5 85206623#1 85206623#2 85206623#3 36926043#14 166479008#0"/>
    <route id="route_16" edges="-36963394#3 -36963394#2 -166479008#0 -36926043#14 -85206623#3 -85206623#2 -85206623#1 167466940#1 167466940#2 167466940#4 167466940#5 167466940#6 168245052"/>
    <route id="route_17" edges="-334471479#1 -334471479#0 37142796#3 37142796#4 -37142795 36926042"/>
    <route id="route_18" edges="167466939#3 37142795 -37142796#4 -37142796#3 -37142796#2 -37142796#1"/>
    <route id="route_19" edges="174760081#4 334472641#1 334472641#2 166443833#0 166443833#1 166443833#2 166443833#3 36897745#0 36897745#1 -37358090#21 -37358090#20 -37358090#19 -37358090#18 -37358090#17 -37358090#15 -37358090#14"/>
    <route id="route_20" edges="167051092#6 37358090#14 37358090#15 37358090#17 37358090#18 37358090#19 37358090#20 37358090#21 -36897745#1 -36897745#0 -166443833#3 -166443833#2 -166443833#1 -166443833#0 -334472641#2"/>
    <route id="route_21" edges="36929318#5 166483066#1"/>
    <route id="route_22" edges="-168135414#2 -168135414#1 -168135414#0 681309247  "/>
    
    <route id="route_23" edges="168282529#0 168282529#1 168282529#3 -328730670#2 -328730670#1 -335736287 36927050#1 36927050#3 36927050#4"/>
    <route id="route_24" edges="-36927050#4 -36927050#3 -36927050#1 335736287 328730670#1 328730670#2 -168282529#3 -168282529#1"/>
    <route id="route_25" edges="-172156200#4 -172156200#3 -172156200#2 -600076511#1 -600076511#0 -599806219 "/> 
    <route id="route_26" edges="599806219 600076511#0 600076511#1 172156200#2 172156200#3 172156200#4"/>
    <route id="route_27" edges="167183554#4 323037140#0 323037140#1"/>
    <route id="route_28" edges="-323037140#3 -323037140#1 -323037140#0"/>
    <route id="route_29" edges="326491694#3 -168278675 -168277060#1 -168277060#0"/>
    <route id="route_30" edges="168278676#0 168278676#1 168278674 -167183554#5"/>
    
    <route id="route_31" edges="-172156200#4 37573573#15"/>
    <route id="route_32" edges="172156200#3 -37573573#14 "/>
    <route id="route_33" edges="37573573#14 172156200#4"/>
    <route id="route_34" edges="-37573573#15 -172156200#3"/>
    <route id="route_35" edges="-37573573#8 168277061#1"/>
    <route id="route_36" edges="37573573#6 168277066#4"/>
    <route id="route_37" edges="168277066#3 -37573573#6"/>
    <route id="route_38" edges="168277061#0 37573573#8"/>
    <route id="route_39" edges="172156185#5 -599806219"/>
    <route id="route_40" edges="172156192#7 600076511#0"/>
    <route id="route_41" edges="599806219 172156185#6"/>
    <route id="route_42" edges="-600076511#0 172156192#8"/>
    <route id="route_43" edges="172156185#9 168277061#3 -168278911#1"/>
    <route id="route_44" edges="-172156185#11 168277066#3"/>
    <route id="route_45" edges="168278909#1 168277066#1 172156185#11"/>
    <route id="route_46" edges="168277061#1 172156192#1"/>
    <route id="route_47" edges="36927022#13 323037140#1"/>
    <route id="route_48" edges="-36927022#14 -323037140#0"/>
    <route id="route_49" edges="323037140#0 -36927022#13"/>
    <route id="route_50" edges="-323037140#3 -323037140#1 36927022#14"/>
    <route id="route_51" edges="36927022#4 36927022#5 -572148897#5 -572148897#4 -572148897#3 36927022#9 36927022#10 -168277060#0 168275547#1 168275547#2 547236215#0"/>
    <route id="route_52" edges="-36927022#12 168278676#1"/>
    <route id="route_53" edges="168278676#0 36927022#12"/>
    <route id="route_54" edges="-168278675 -168277060#1 -36927022#10"/>
    <route id="route_55" edges="168280093#4 547236215#0"/>
    <route id="route_56" edges="547236209#2 547236211#0"/>
    <route id="route_57" edges="168274455#7 547236212#0"/>
    <route id="route_58" edges="168275547#2 -168280085#7"/>
    <route id="route_59" edges="168280093#1 -168282529#1"/>
    <route id="route_60" edges="-168280085#3 168282529#3"/>
    <route id="route_61" edges="168282529#0 168282529#1 168280085#3"/>
    <route id="route_62" edges="-168282529#3 -168280085#2"/>
    <route id="route_63" edges="168280085#0 36927050#3"/>
    <route id="route_64" edges="-168280085#1 -36927050#1"/>
    <route id="route_65" edges="-36927050#3 168280093#1"/>
    <route id="route_66" edges="36927050#1 -168280085#0"/>
    <route id="route_67" edges="gneE5 gneE3"/>
    <route id="route_68" edges="gneE8 gneE2"/>
    <route id="route_69" edges="-gneE2 gneE6"/>
    <route id="route_70" edges="gneE4 gneE7"/>
    <route id="route_71" edges="310698683#1 168244316#3"/>
    <route id="route_72" edges="167466940#6 168244311#4"/>
    <route id="route_73" edges="168244316#1 168245052"/>
    <route id="route_74" edges="168244311#2 310698680#2"/>
    <route id="route_75" edges="37142796#4 168244316#4"/>
    <route id="route_76" edges="37142795 168244311#2"/>
    <route id="route_77" edges="168244311#1 -37142795"/>
    <route id="route_78" edges="168244316#3 -37142796#4"/>
    <route id="route_79" edges="334472641#2 168108873#2"/>
    <route id="route_80" edges="-166443833#0 93548845#0"/>
    <route id="route_81" edges="168108881#1 166443833#0"/>
    <route id="route_82" edges="168279452#3 -334472641#2"/>
    <route id="route_83" edges="166735152#5 167187423#0 167187423#1 -37555831#11"/>
    <route id="route_84" edges="166746156#1 167187880#0 167187880#1"/>
    <route id="route_85" edges="167187421#3 166746157#0"/>
    <route id="route_86" edges="167187877#3 167187877#4 166741559#0 328735869"/>
    <route id="route_87" edges="172156185#13 -363982778#1"/>
    <route id="route_88" edges="37555813#9 -167179198#1 37555829#0"/>
    <route id="route_89" edges="-167179198#2 -37555813#9"/>
    <route id="route_90" edges="-363982778#3 -172156185#13"/>
    <route id="route_91" edges="334995855#1 168282530 166851620#0 -334995852#1"/>
    <route id="route_92" edges="-168282632#1 -168282632#0 167179196#0"/>
    <route id="route_93" edges="166851618#3 166851618#4 168282633"/>
    <route id="route_94" edges="167178310#1 -168282531 -168282525#9 -167183549#1"/>
    <route id="route_95" edges="547560322#8 547560322#9 166479009#0"/>
    <route id="route_96" edges="167463857#4"/>
    <route id="route_97" edges="166479007 167463858#0 "/>
    <route id="route_98" edges="166851620#4 166851620#5 -60521894#6"/>
    <route id="route_99" edges="85206623#2 85206623#3 36926043#14 166478537"/>
    <route id="route_100" edges="-166479008#0 166479007"/>
    <route id="route_101" edges="166478539 166479008#0"/>
    <route id="route_102" edges="166479009#1 -36926043#14 -36926043#13 -335011922#1"/>
    <route id="route_103" edges="-37358090#17 166458246#3 "/>
    <route id="route_104" edges="171996618#2 37358090#15 166458245#1 "/>
    <route id="route_105" edges="166482330#1 -37358090#15 -37358090#14"/>
    <route id="route_106" edges="166458246#2 37358090#17"/>
    <route id="route_107" edges="166483062#2 168135415#0"/>
    <route id="route_108" edges="166483064 168119166#0"/>
	<route id="route_109" edges="599806219 600076511#0 600076511#1 172156200#2 172156200#3 172156200#4"/>""",
              file=routes)
        lastVeh = 0
        vehNr = 0
        for i in range(N):
            for j in range(len(cf.routeH)):
                # d = cf.directions[j]
                if random.uniform(0, 1) < cf.pH[j]:
                    route = cf.routeH[j]
                    # cf.tcH[d] = cf.tcH[d] + 1
                    k = random.randint(0, 3)
                    if k == 0:
                        print('<vehicle id="%s_%i" type="Bus" route="%s" depart="%i" />' % (v_Types[k], vehNr, route, i),file=routes)
                        vehNr += 1
                    if k == 1:
                        print('<vehicle id="%s_%i" type="Auto" route="%s" depart="%i" />' % (v_Types[k], vehNr, route, i),
                              file=routes)
                        vehNr += 1
                    if k == 1:
                        print('<vehicle id="%s_%i" type="MotorCycle" route="%s" depart="%i" />' % (v_Types[k], vehNr, route, i),
                              file=routes)
                        vehNr += 1
                    if k == 3:
                        print('<vehicle id="%s_%i" type="Car" route="%s" depart="%i" />' % (v_Types[k], vehNr, route, i),
                              file=routes)
                        vehNr += 1
                    # print('<vehicle id="%s_%i" type="Auto" route="%s" depart="%i" />' % (
                    #     route, vehNr, route, i), file=routes)
                    # vehNr += 1
                    lastVeh = i
        print('<!-- totalCars="%i -->' % (vehNr), file=routes)
        print('<!-- CarsPerDirection="%s -->' % (str(cf.tcH)), file=routes)
        print("</routes>", file=routes)
        # print(cf.tcH)
        print("Total cars Generated:",vehNr)


def get_options():
    optParser = optparse.OptionParser()
    optParser.add_option("--cases", type="string", dest="cases", default="Case3")
    optParser.add_option("--output", type="string", dest="output", default="ahm2PhaseOsmFiftyLoop.rou.xml")
    options, args = optParser.parse_args()
    return options


# this is the main entry point of this script
if __name__ == "__main__":
    options = get_options()
    generate_routefileAhmFiftyOsm(options.cases, options.output,32)
    # generate_routefileSimple()


