#!/usr/bin/python
'''
based on code from http://www.acmesystems.it/python_httpd
'''
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from os import curdir, sep
import json
import datetime

PORT_NUMBER = 9999

epoch = datetime.datetime.utcfromtimestamp(0)
#~ current = int(round(time.time() * 1000))
#~ set date for data series

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0



data_series = [
	#~ {"target": "upper_25", "datapoints": [[3, 1482274336930], [2, 1482274216930]]},
	{"target": "upper_25", "datapoints": [[3.0, 1482271114000000], [2.0, 1482271664000000], [1.0, 1450754280000000], [0.0, 1450754340000000], [1.0, 1450754400000000], [1.0, 1450754460000], [1.0, 1450754520000], [1.0, 1450754580000], [1.0, 1450754640000], [1.0, 1450754700000], [2.0, 1450754760000], [1.0, 1450754820000], [165.0, 1450754880000], [5.0, 1450754940000], [1.0, 1450755000000], [1.0, 1450755060000], [5.0, 1450755120000], [2.0, 1450755180000], [2.0, 1450755240000], [1.0, 1450755300000], [1.0, 1450755360000], [7.0, 1450755420000], [4.0, 1450755480000], [1.0, 1450755540000], [7.0, 1450755600000], [7.0, 1450755660000], [1.0, 1450755720000], [2.0, 1450755780000], [1.0, 1450755840000], [1.0, 1450755900000], [2.0, 1450755960000], [1.0, 1450756020000], [1.0, 1450756080000], [2.0, 1450756140000], [1.0, 1450756200000], [7.0, 1450756260000], [2.0, 1450756320000], [2.0, 1450756380000], [1.0, 1450756440000], [8.0, 1450756500000], [7.0, 1450756560000], [1.0, 1450756620000], [2.0, 1450756680000], [2.0, 1450756740000], [2.0, 1450756800000], [2.0, 1450756860000], [18.0, 1450756920000], [1.0, 1450756980000], [1.0, 1450757040000], [1.0, 1450757100000], [1.0, 1450757160000], [6.0, 1450757220000], [2.0, 1450757280000], [1.0, 1450757340000], [2.0, 1450757400000], [2.0, 1450757460000], [1.0, 1450757520000], [1.0, 1450757580000], [1.0, 1450757640000], [1.0, 1450757700000], [1.0, 1450757760000], [1.0, 1450757820000], [15.0, 1450757880000], [5.0, 1450757940000], [2.0, 1450758000000], [1.0, 1450758060000], [1.0, 1450758120000], [1.0, 1450758180000], [1.0, 1450758240000], [1.0, 1450758300000], [1.0, 1450758360000], [1.0, 1450758420000], [1.0, 1450758480000], [1.0, 1450758540000], [1.0, 1450758600000], [2.0, 1450758660000], [1.0, 1450758720000], [2.0, 1450758780000], [1.0, 1450758840000], [1.0, 1450758900000], [1.0, 1450758960000], [1.0, 1450759020000], [1.0, 1450759080000], [1.0, 1450759140000], [8.0, 1450759200000], [1.0, 1450759260000], [2.0, 1450759320000], [1.0, 1450759380000], [1.0, 1450759440000], [1.0, 1450759500000], [2.0, 1450759560000], [2.0, 1450759620000], [1.0, 1450759680000], [1.0, 1450759740000], [2.0, 1450759800000], [1.0, 1450759860000], [1.0, 1450759920000], [1.0, 1450759980000], [1.0, 1450760040000], [2.0, 1450760100000], [9.0, 1450760160000], [1.0, 1450760220000], [2.0, 1450760280000], [1.0, 1450760340000], [0.0, 1450760400000], [1.0, 1450760460000], [1.0, 1450760520000], [1.0, 1450760580000], [2.0, 1450760640000], [1.0, 1450760700000], [2.0, 1450760760000], [1.0, 1450760820000], [3.0, 1450760880000], [3.0, 1450760940000], [1.0, 1450761000000], [1.0, 1450761060000], [1.0, 1450761120000], [1.0, 1450761180000], [1.0, 1450761240000], [1.0, 1450761300000], [1.0, 1450761360000], [1.0, 1450761420000], [1.0, 1450761480000], [1.0, 1450761540000], [2.0, 1450761600000], [1.0, 1450761660000], [1.0, 1450761720000], [1.0, 1450761780000], [1.0, 1450761840000], [1.0, 1450761900000], [1.0, 1450761960000], [2.0, 1450762020000], [2.0, 1450762080000], [1.0, 1450762140000], [2.0, 1450762200000], [1.0, 1450762260000], [1.0, 1450762320000], [8.0, 1450762380000], [1.0, 1450762440000], [2.0, 1450762500000], [1.0, 1450762560000], [2.0, 1450762620000], [1.0, 1450762680000], [1.0, 1450762740000], [1.0, 1450762800000], [1.0, 1450762860000], [1.0, 1450762920000], [1.0, 1450762980000], [1.0, 1450763040000], [1.0, 1450763100000], [1.0, 1450763160000], [1.0, 1450763220000], [1.0, 1450763280000], [2.0, 1450763340000], [1.0, 1450763400000], [1.0, 1450763460000], [1.0, 1450763520000], [1.0, 1450763580000], [2.0, 1450763640000], [1.0, 1450763700000], [1.0, 1450763760000], [2.0, 1450763820000], [1.0, 1450763880000], [1.0, 1450763940000], [1.0, 1450764000000], [1.0, 1450764060000], [2.0, 1450764120000], [2.0, 1450764180000], [5.0, 1450764240000], [2.0, 1450764300000], [1.0, 1450764360000], [2.0, 1450764420000], [1.0, 1450764480000], [2.0, 1450764540000], [1.0, 1450764600000], [2.0, 1450764660000], [1.0, 1450764720000], [1.0, 1450764780000], [1.0, 1450764840000], [2.0, 1450764900000], [1.0, 1450764960000], [1.0, 1450765020000], [1.0, 1450765080000], [1.0, 1450765140000], [1.0, 1450765200000], [1.0, 1450765260000], [2.0, 1450765320000], [1.0, 1450765380000], [1.0, 1450765440000], [1.0, 1450765500000], [1.0, 1450765560000], [1.0, 1450765620000], [1.0, 1450765680000], [1.0, 1450765740000], [1.0, 1450765800000], [1.0, 1450765860000], [1.0, 1450765920000], [1.0, 1450765980000], [1.0, 1450766040000], [1.0, 1450766100000], [3.0, 1450766160000], [1.0, 1450766220000], [1.0, 1450766280000], [18.0, 1450766340000], [1.0, 1450766400000]]},
	{"target": "upper_50", "datapoints": [[130.0, 1450754160000], [24.0, 1450754220000], [4.0, 1450754280000], [1.0, 1450754340000], [4.0, 1450754400000], [36.0, 1450754460000], [30.0, 1450754520000], [2.0, 1450754580000], [6.0, 1450754640000], [186.0, 1450754700000], [9.0, 1450754760000], [114.0, 1450754820000], [288.0, 1450754880000], [112.0, 1450754940000], [2.0, 1450755000000], [5.0, 1450755060000], [9.0, 1450755120000], [6.0, 1450755180000], [149.0, 1450755240000], [49.0, 1450755300000], [2.0, 1450755360000], [238.0, 1450755420000], [8.0, 1450755480000], [7.0, 1450755540000], [267.0, 1450755600000], [152.0, 1450755660000], [2.0, 1450755720000], [18.0, 1450755780000], [15.0, 1450755840000], [7.0, 1450755900000], [3.0, 1450755960000], [7.0, 1450756020000], [9.0, 1450756080000], [219.0, 1450756140000], [5.0, 1450756200000], [211.0, 1450756260000], [6.0, 1450756320000], [5.0, 1450756380000], [6.0, 1450756440000], [49.0, 1450756500000], [133.0, 1450756560000], [13.0, 1450756620000], [8.0, 1450756680000], [4.0, 1450756740000], [19.0, 1450756800000], [137.0, 1450756860000], [98.0, 1450756920000], [13.0, 1450756980000], [282.0, 1450757040000], [9.0, 1450757100000], [2.0, 1450757160000], [83.0, 1450757220000], [70.0, 1450757280000], [9.0, 1450757340000], [76.0, 1450757400000], [28.0, 1450757460000], [11.0, 1450757520000], [33.0, 1450757580000], [4.0, 1450757640000], [8.0, 1450757700000], [6.0, 1450757760000], [56.0, 1450757820000], [259.0, 1450757880000], [370.0, 1450757940000], [2.0, 1450758000000], [306.0, 1450758060000], [45.0, 1450758120000], [3.0, 1450758180000], [5.0, 1450758240000], [1.0, 1450758300000], [13.0, 1450758360000], [1.0, 1450758420000], [55.0, 1450758480000], [6.0, 1450758540000], [2.0, 1450758600000], [90.0, 1450758660000], [3.0, 1450758720000], [14.0, 1450758780000], [15.0, 1450758840000], [3.0, 1450758900000], [7.0, 1450758960000], [6.0, 1450759020000], [7.0, 1450759080000], [2.0, 1450759140000], [43.0, 1450759200000], [2.0, 1450759260000], [61.0, 1450759320000], [20.0, 1450759380000], [12.0, 1450759440000], [84.0, 1450759500000], [49.0, 1450759560000], [47.0, 1450759620000], [112.0, 1450759680000], [40.0, 1450759740000], [214.0, 1450759800000], [6.0, 1450759860000], [2.0, 1450759920000], [6.0, 1450759980000], [11.0, 1450760040000], [106.0, 1450760100000], [450.0, 1450760160000], [5.0, 1450760220000], [7.0, 1450760280000], [32.0, 1450760340000], [293.0, 1450760400000], [8.0, 1450760460000], [58.0, 1450760520000], [13.0, 1450760580000], [86.0, 1450760640000], [11.0, 1450760700000], [77.0, 1450760760000], [21.0, 1450760820000], [32.0, 1450760880000], [53.0, 1450760940000], [11.0, 1450761000000], [14.0, 1450761060000], [10.0, 1450761120000], [5.0, 1450761180000], [21.0, 1450761240000], [9.0, 1450761300000], [245.0, 1450761360000], [27.0, 1450761420000], [62.0, 1450761480000], [8.0, 1450761540000], [21.0, 1450761600000], [53.0, 1450761660000], [13.0, 1450761720000], [3.0, 1450761780000], [14.0, 1450761840000], [9.0, 1450761900000], [5.0, 1450761960000], [156.0, 1450762020000], [9.0, 1450762080000], [6.0, 1450762140000], [8.0, 1450762200000], [24.0, 1450762260000], [3.0, 1450762320000], [356.0, 1450762380000], [42.0, 1450762440000], [79.0, 1450762500000], [8.0, 1450762560000], [211.0, 1450762620000], [6.0, 1450762680000], [3.0, 1450762740000], [3.0, 1450762800000], [20.0, 1450762860000], [3.0, 1450762920000], [2.0, 1450762980000], [4.0, 1450763040000], [7.0, 1450763100000], [7.0, 1450763160000], [34.0, 1450763220000], [8.0, 1450763280000], [14.0, 1450763340000], [7.0, 1450763400000], [4.0, 1450763460000], [14.0, 1450763520000], [74.0, 1450763580000], [251.0, 1450763640000], [5.0, 1450763700000], [91.0, 1450763760000], [30.0, 1450763820000], [28.0, 1450763880000], [6.0, 1450763940000], [79.0, 1450764000000], [17.0, 1450764060000], [174.0, 1450764120000], [189.0, 1450764180000], [120.0, 1450764240000], [184.0, 1450764300000], [188.0, 1450764360000], [250.0, 1450764420000], [3.0, 1450764480000], [87.0, 1450764540000], [17.0, 1450764600000], [244.0, 1450764660000], [65.0, 1450764720000], [8.0, 1450764780000], [56.0, 1450764840000], [25.0, 1450764900000], [5.0, 1450764960000], [57.0, 1450765020000], [16.0, 1450765080000], [38.0, 1450765140000], [13.0, 1450765200000], [28.0, 1450765260000], [91.0, 1450765320000], [95.0, 1450765380000], [8.0, 1450765440000], [61.0, 1450765500000], [11.0, 1450765560000], [19.0, 1450765620000], [5.0, 1450765680000], [102.0, 1450765740000], [82.0, 1450765800000], [133.0, 1450765860000], [178.0, 1450765920000], [46.0, 1450765980000], [68.0, 1450766040000], [8.0, 1450766100000], [200.0, 1450766160000], [128.0, 1450766220000], [222.0, 1450766280000], [334.0, 1450766340000], [153.0, 1450766400000]]},
	{"target": "upper_75", "datapoints": [[622.0, 1450754160000], [365.0, 1450754220000], [42.0, 1450754280000], [240.0, 1450754340000], [401.0, 1450754400000], [364.0, 1450754460000], [325.0, 1450754520000], [6.0, 1450754580000], [267.0, 1450754640000], [302.0, 1450754700000], [123.0, 1450754760000], [290.0, 1450754820000], [326.0, 1450754880000], [322.0, 1450754940000], [539.0, 1450755000000], [149.0, 1450755060000], [18.0, 1450755120000], [10.0, 1450755180000], [643.0, 1450755240000], [256.0, 1450755300000], [13.0, 1450755360000], [455.0, 1450755420000], [341.0, 1450755480000], [394.0, 1450755540000], [662.0, 1450755600000], [244.0, 1450755660000], [213.0, 1450755720000], [274.0, 1450755780000], [466.0, 1450755840000], [247.0, 1450755900000], [11.0, 1450755960000], [178.0, 1450756020000], [291.0, 1450756080000], [1039.0, 1450756140000], [84.0, 1450756200000], [384.0, 1450756260000], [339.0, 1450756320000], [266.0, 1450756380000], [22.0, 1450756440000], [384.0, 1450756500000], [701.0, 1450756560000], [549.0, 1450756620000], [13.0, 1450756680000], [279.0, 1450756740000], [266.0, 1450756800000], [267.0, 1450756860000], [1373.0, 1450756920000], [51.0, 1450756980000], [388.0, 1450757040000], [58.0, 1450757100000], [175.0, 1450757160000], [425.0, 1450757220000], [338.0, 1450757280000], [373.0, 1450757340000], [509.0, 1450757400000], [406.0, 1450757460000], [168.0, 1450757520000], [342.0, 1450757580000], [299.0, 1450757640000], [696.0, 1450757700000], [483.0, 1450757760000], [775.0, 1450757820000], [1178.0, 1450757880000], [625.0, 1450757940000], [230.0, 1450758000000], [553.0, 1450758060000], [185.0, 1450758120000], [584.0, 1450758180000], [214.0, 1450758240000], [183.0, 1450758300000], [282.0, 1450758360000], [262.0, 1450758420000], [345.0, 1450758480000], [204.0, 1450758540000], [59.0, 1450758600000], [299.0, 1450758660000], [82.0, 1450758720000], [376.0, 1450758780000], [474.0, 1450758840000], [526.0, 1450758900000], [220.0, 1450758960000], [293.0, 1450759020000], [77.0, 1450759080000], [109.0, 1450759140000], [633.0, 1450759200000], [69.0, 1450759260000], [392.0, 1450759320000], [376.0, 1450759380000], [309.0, 1450759440000], [578.0, 1450759500000], [519.0, 1450759560000], [310.0, 1450759620000], [497.0, 1450759680000], [636.0, 1450759740000], [674.0, 1450759800000], [516.0, 1450759860000], [143.0, 1450759920000], [325.0, 1450759980000], [516.0, 1450760040000], [279.0, 1450760100000], [977.0, 1450760160000], [322.0, 1450760220000], [1277.0, 1450760280000], [568.0, 1450760340000], [907.0, 1450760400000], [465.0, 1450760460000], [528.0, 1450760520000], [156.0, 1450760580000], [729.0, 1450760640000], [316.0, 1450760700000], [466.0, 1450760760000], [356.0, 1450760820000], [549.0, 1450760880000], [448.0, 1450760940000], [386.0, 1450761000000], [400.0, 1450761060000], [391.0, 1450761120000], [588.0, 1450761180000], [574.0, 1450761240000], [507.0, 1450761300000], [545.0, 1450761360000], [417.0, 1450761420000], [542.0, 1450761480000], [346.0, 1450761540000], [561.0, 1450761600000], [765.0, 1450761660000], [446.0, 1450761720000], [356.0, 1450761780000], [523.0, 1450761840000], [508.0, 1450761900000], [595.0, 1450761960000], [457.0, 1450762020000], [163.0, 1450762080000], [298.0, 1450762140000], [301.0, 1450762200000], [445.0, 1450762260000], [170.0, 1450762320000], [595.0, 1450762380000], [508.0, 1450762440000], [268.0, 1450762500000], [488.0, 1450762560000], [670.0, 1450762620000], [366.0, 1450762680000], [501.0, 1450762740000], [701.0, 1450762800000], [484.0, 1450762860000], [232.0, 1450762920000], [317.0, 1450762980000], [153.0, 1450763040000], [444.0, 1450763100000], [330.0, 1450763160000], [399.0, 1450763220000], [612.0, 1450763280000], [359.0, 1450763340000], [320.0, 1450763400000], [424.0, 1450763460000], [490.0, 1450763520000], [426.0, 1450763580000], [717.0, 1450763640000], [339.0, 1450763700000], [420.0, 1450763760000], [436.0, 1450763820000], [398.0, 1450763880000], [419.0, 1450763940000], [595.0, 1450764000000], [518.0, 1450764060000], [780.0, 1450764120000], [466.0, 1450764180000], [474.0, 1450764240000], [505.0, 1450764300000], [593.0, 1450764360000], [654.0, 1450764420000], [402.0, 1450764480000], [456.0, 1450764540000], [525.0, 1450764600000], [578.0, 1450764660000], [413.0, 1450764720000], [790.0, 1450764780000], [567.0, 1450764840000], [512.0, 1450764900000], [441.0, 1450764960000], [501.0, 1450765020000], [550.0, 1450765080000], [692.0, 1450765140000], [499.0, 1450765200000], [507.0, 1450765260000], [519.0, 1450765320000], [581.0, 1450765380000], [414.0, 1450765440000], [371.0, 1450765500000], [376.0, 1450765560000], [617.0, 1450765620000], [327.0, 1450765680000], [755.0, 1450765740000], [615.0, 1450765800000], [526.0, 1450765860000], [569.0, 1450765920000], [473.0, 1450765980000], [508.0, 1450766040000], [558.0, 1450766100000], [577.0, 1450766160000], [473.0, 1450766220000], [594.0, 1450766280000], [695.0, 1450766340000], [607.0, 1450766400000]]},
	{"target": "upper_90", "datapoints": [[861.0, 1450754160000], [767.0, 1450754220000], [809.0, 1450754280000], [744.0, 1450754340000], [624.0, 1450754400000], [2445.0, 1450754460000], [3134.0, 1450754520000], [586.0, 1450754580000], [505.0, 1450754640000], [626.0, 1450754700000], [1441.0, 1450754760000], [1246.0, 1450754820000], [666.0, 1450754880000], [813.0, 1450754940000], [1654.0, 1450755000000], [785.0, 1450755060000], [254.0, 1450755120000], [534.0, 1450755180000], [1042.0, 1450755240000], [1574.0, 1450755300000], [1001.0, 1450755360000], [526.0, 1450755420000], [2447.0, 1450755480000], [1596.0, 1450755540000], [794.0, 1450755600000], [731.0, 1450755660000], [425.0, 1450755720000], [835.0, 1450755780000], [510.0, 1450755840000], [404.0, 1450755900000], [112.0, 1450755960000], [418.0, 1450756020000], [1032.0, 1450756080000], [1661.0, 1450756140000], [435.0, 1450756200000], [730.0, 1450756260000], [591.0, 1450756320000], [389.0, 1450756380000], [208.0, 1450756440000], [512.0, 1450756500000], [968.0, 1450756560000], [1274.0, 1450756620000], [536.0, 1450756680000], [893.0, 1450756740000], [708.0, 1450756800000], [332.0, 1450756860000], [1555.0, 1450756920000], [331.0, 1450756980000], [814.0, 1450757040000], [261.0, 1450757100000], [358.0, 1450757160000], [821.0, 1450757220000], [713.0, 1450757280000], [945.0, 1450757340000], [671.0, 1450757400000], [663.0, 1450757460000], [1046.0, 1450757520000], [957.0, 1450757580000], [1017.0, 1450757640000], [1096.0, 1450757700000], [1233.0, 1450757760000], [2616.0, 1450757820000], [1919.0, 1450757880000], [1850.0, 1450757940000], [883.0, 1450758000000], [1206.0, 1450758060000], [479.0, 1450758120000], [1282.0, 1450758180000], [501.0, 1450758240000], [3727.0, 1450758300000], [1019.0, 1450758360000], [1075.0, 1450758420000], [798.0, 1450758480000], [571.0, 1450758540000], [457.0, 1450758600000], [1682.0, 1450758660000], [381.0, 1450758720000], [641.0, 1450758780000], [618.0, 1450758840000], [753.0, 1450758900000], [805.0, 1450758960000], [783.0, 1450759020000], [521.0, 1450759080000], [532.0, 1450759140000], [1380.0, 1450759200000], [696.0, 1450759260000], [613.0, 1450759320000], [597.0, 1450759380000], [1241.0, 1450759440000], [1000.0, 1450759500000], [1034.0, 1450759560000], [590.0, 1450759620000], [797.0, 1450759680000], [959.0, 1450759740000], [1105.0, 1450759800000], [921.0, 1450759860000], [740.0, 1450759920000], [736.0, 1450759980000], [961.0, 1450760040000], [521.0, 1450760100000], [1583.0, 1450760160000], [640.0, 1450760220000], [1977.0, 1450760280000], [1628.0, 1450760340000], [1821.0, 1450760400000], [1130.0, 1450760460000], [799.0, 1450760520000], [435.0, 1450760580000], [1280.0, 1450760640000], [1171.0, 1450760700000], [1078.0, 1450760760000], [564.0, 1450760820000], [1707.0, 1450760880000], [786.0, 1450760940000], [725.0, 1450761000000], [2347.0, 1450761060000], [770.0, 1450761120000], [896.0, 1450761180000], [1019.0, 1450761240000], [1241.0, 1450761300000], [988.0, 1450761360000], [693.0, 1450761420000], [757.0, 1450761480000], [1522.0, 1450761540000], [883.0, 1450761600000], [1307.0, 1450761660000], [691.0, 1450761720000], [600.0, 1450761780000], [698.0, 1450761840000], [883.0, 1450761900000], [796.0, 1450761960000], [749.0, 1450762020000], [512.0, 1450762080000], [946.0, 1450762140000], [1069.0, 1450762200000], [1202.0, 1450762260000], [696.0, 1450762320000], [1044.0, 1450762380000], [1297.0, 1450762440000], [661.0, 1450762500000], [829.0, 1450762560000], [1268.0, 1450762620000], [646.0, 1450762680000], [1111.0, 1450762740000], [1341.0, 1450762800000], [658.0, 1450762860000], [806.0, 1450762920000], [918.0, 1450762980000], [442.0, 1450763040000], [796.0, 1450763100000], [847.0, 1450763160000], [988.0, 1450763220000], [756.0, 1450763280000], [716.0, 1450763340000], [761.0, 1450763400000], [749.0, 1450763460000], [731.0, 1450763520000], [900.0, 1450763580000], [1157.0, 1450763640000], [811.0, 1450763700000], [638.0, 1450763760000], [833.0, 1450763820000], [787.0, 1450763880000], [883.0, 1450763940000], [1654.0, 1450764000000], [1011.0, 1450764060000], [1751.0, 1450764120000], [1000.0, 1450764180000], [1073.0, 1450764240000], [1106.0, 1450764300000], [1127.0, 1450764360000], [1441.0, 1450764420000], [825.0, 1450764480000], [881.0, 1450764540000], [903.0, 1450764600000], [1065.0, 1450764660000], [1215.0, 1450764720000], [1613.0, 1450764780000], [1012.0, 1450764840000], [1426.0, 1450764900000], [1380.0, 1450764960000], [1181.0, 1450765020000], [1178.0, 1450765080000], [1336.0, 1450765140000], [1004.0, 1450765200000], [1236.0, 1450765260000], [954.0, 1450765320000], [1183.0, 1450765380000], [952.0, 1450765440000], [1163.0, 1450765500000], [818.0, 1450765560000], [1183.0, 1450765620000], [847.0, 1450765680000], [1227.0, 1450765740000], [1109.0, 1450765800000], [1061.0, 1450765860000], [824.0, 1450765920000], [917.0, 1450765980000], [1006.0, 1450766040000], [964.0, 1450766100000], [906.0, 1450766160000], [1036.0, 1450766220000], [939.0, 1450766280000], [1203.0, 1450766340000], [1344.0, 1450766400000]]},
	{"target": "upper_95", "datapoints": [[861.0, 1450754160000], [767.0, 1450754220000], [809.0, 1450754280000], [907.0, 1450754340000], [624.0, 1450754400000], [2445.0, 1450754460000], [3134.0, 1450754520000], [611.0, 1450754580000], [505.0, 1450754640000], [646.0, 1450754700000], [1441.0, 1450754760000], [1246.0, 1450754820000], [666.0, 1450754880000], [813.0, 1450754940000], [1654.0, 1450755000000], [785.0, 1450755060000], [309.0, 1450755120000], [1570.0, 1450755180000], [1042.0, 1450755240000], [1574.0, 1450755300000], [1001.0, 1450755360000], [729.0, 1450755420000], [2447.0, 1450755480000], [1596.0, 1450755540000], [883.0, 1450755600000], [731.0, 1450755660000], [1173.0, 1450755720000], [1255.0, 1450755780000], [716.0, 1450755840000], [635.0, 1450755900000], [931.0, 1450755960000], [558.0, 1450756020000], [1614.0, 1450756080000], [1881.0, 1450756140000], [435.0, 1450756200000], [1798.0, 1450756260000], [1493.0, 1450756320000], [2108.0, 1450756380000], [297.0, 1450756440000], [702.0, 1450756500000], [1216.0, 1450756560000], [1666.0, 1450756620000], [536.0, 1450756680000], [893.0, 1450756740000], [916.0, 1450756800000], [473.0, 1450756860000], [1555.0, 1450756920000], [331.0, 1450756980000], [1644.0, 1450757040000], [556.0, 1450757100000], [358.0, 1450757160000], [821.0, 1450757220000], [1325.0, 1450757280000], [1052.0, 1450757340000], [974.0, 1450757400000], [816.0, 1450757460000], [1062.0, 1450757520000], [1438.0, 1450757580000], [3759.0, 1450757640000], [1479.0, 1450757700000], [2117.0, 1450757760000], [2878.0, 1450757820000], [3627.0, 1450757880000], [2101.0, 1450757940000], [931.0, 1450758000000], [1593.0, 1450758060000], [487.0, 1450758120000], [2282.0, 1450758180000], [983.0, 1450758240000], [4287.0, 1450758300000], [1422.0, 1450758360000], [1604.0, 1450758420000], [1099.0, 1450758480000], [1128.0, 1450758540000], [1547.0, 1450758600000], [1932.0, 1450758660000], [595.0, 1450758720000], [708.0, 1450758780000], [1481.0, 1450758840000], [1107.0, 1450758900000], [875.0, 1450758960000], [1128.0, 1450759020000], [618.0, 1450759080000], [1809.0, 1450759140000], [2170.0, 1450759200000], [831.0, 1450759260000], [1898.0, 1450759320000], [1556.0, 1450759380000], [1388.0, 1450759440000], [1864.0, 1450759500000], [1220.0, 1450759560000], [1351.0, 1450759620000], [1612.0, 1450759680000], [1089.0, 1450759740000], [1364.0, 1450759800000], [1397.0, 1450759860000], [1194.0, 1450759920000], [892.0, 1450759980000], [1275.0, 1450760040000], [1110.0, 1450760100000], [2732.0, 1450760160000], [1751.0, 1450760220000], [2395.0, 1450760280000], [1750.0, 1450760340000], [1821.0, 1450760400000], [1353.0, 1450760460000], [1088.0, 1450760520000], [938.0, 1450760580000], [1699.0, 1450760640000], [1497.0, 1450760700000], [1880.0, 1450760760000], [599.0, 1450760820000], [2319.0, 1450760880000], [1114.0, 1450760940000], [840.0, 1450761000000], [2462.0, 1450761060000], [1316.0, 1450761120000], [1018.0, 1450761180000], [1195.0, 1450761240000], [1300.0, 1450761300000], [1389.0, 1450761360000], [908.0, 1450761420000], [2060.0, 1450761480000], [1535.0, 1450761540000], [1535.0, 1450761600000], [2505.0, 1450761660000], [920.0, 1450761720000], [996.0, 1450761780000], [1378.0, 1450761840000], [1171.0, 1450761900000], [1105.0, 1450761960000], [848.0, 1450762020000], [798.0, 1450762080000], [1338.0, 1450762140000], [1307.0, 1450762200000], [1317.0, 1450762260000], [940.0, 1450762320000], [1418.0, 1450762380000], [1699.0, 1450762440000], [859.0, 1450762500000], [1038.0, 1450762560000], [1760.0, 1450762620000], [676.0, 1450762680000], [1501.0, 1450762740000], [1521.0, 1450762800000], [714.0, 1450762860000], [964.0, 1450762920000], [1286.0, 1450762980000], [609.0, 1450763040000], [1363.0, 1450763100000], [1610.0, 1450763160000], [1097.0, 1450763220000], [1571.0, 1450763280000], [949.0, 1450763340000], [1239.0, 1450763400000], [998.0, 1450763460000], [808.0, 1450763520000], [1158.0, 1450763580000], [1683.0, 1450763640000], [1195.0, 1450763700000], [733.0, 1450763760000], [1498.0, 1450763820000], [1015.0, 1450763880000], [956.0, 1450763940000], [2610.0, 1450764000000], [1335.0, 1450764060000], [2282.0, 1450764120000], [1840.0, 1450764180000], [1540.0, 1450764240000], [1371.0, 1450764300000], [1553.0, 1450764360000], [1722.0, 1450764420000], [1031.0, 1450764480000], [1850.0, 1450764540000], [1590.0, 1450764600000], [1264.0, 1450764660000], [1828.0, 1450764720000], [2048.0, 1450764780000], [1460.0, 1450764840000], [1498.0, 1450764900000], [1671.0, 1450764960000], [1516.0, 1450765020000], [2505.0, 1450765080000], [1489.0, 1450765140000], [1141.0, 1450765200000], [1756.0, 1450765260000], [1161.0, 1450765320000], [1687.0, 1450765380000], [1227.0, 1450765440000], [1979.0, 1450765500000], [1457.0, 1450765560000], [1400.0, 1450765620000], [1267.0, 1450765680000], [1560.0, 1450765740000], [1843.0, 1450765800000], [1565.0, 1450765860000], [1266.0, 1450765920000], [1063.0, 1450765980000], [1464.0, 1450766040000], [1333.0, 1450766100000], [1004.0, 1450766160000], [1358.0, 1450766220000], [1234.0, 1450766280000], [1744.0, 1450766340000], [1640.0, 1450766400000]]}
	]

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
	
	#Handler for the GET requests
	def do_GET(self):
		if self.path=="/":
			self.path="/index.html"

		try:
			#Check the file extension required and
			#set the right mime type

			sendReply = False
			if self.path.endswith(".html"):
				mimetype='text/html'
				sendReply = True
			if self.path.endswith(".jpg"):
				mimetype='image/jpg'
				sendReply = True
			if self.path.endswith(".gif"):
				mimetype='image/gif'
				sendReply = True
			if self.path.endswith(".js"):
				mimetype='application/javascript'
				sendReply = True
			if self.path.endswith(".css"):
				mimetype='text/css'
				sendReply = True

			if (self.path == "/search"):
				data = []
				for row in data_series:
					data.append (row["target"])
				self.request.sendall(json.dumps(data))
			elif sendReply == True:
				#Open the static file requested and send it
				f = open(curdir + sep + self.path) 
				self.send_response(200)
				self.send_header('Content-type',mimetype)
				self.end_headers()
				self.wfile.write(f.read())
				f.close()
			return


		except IOError:
			self.send_error(404,'File Not Found: %s' % self.path)

	def do_POST(self):
		try:
			if (self.path == "/query"):
				data = []
				print("\n----- Request Start ----->\n")
				print "POST /query"
				request_headers = self.headers
				content_length = request_headers.getheaders('content-length')
				length = int(content_length[0]) if content_length else 0
				#~ print (self.headers)
				print(json.dumps(json.loads(self.rfile.read(length)), indent=4))
				print("<----- Request End -----\n")
				print ("Response:")
				self.send_response(200)  # OK
				self.send_header("Access-Control-Allow-Origin", "*")
				self.end_headers()

				#~ print (self.headers)
				self.request.sendall(json.dumps(data_series))
				#~ print(json.dumps(data_series, indent=2))

		except IOError:
			self.send_error(404,'File Not Found: %s' % self.path)


try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print 'Started httpserver on port ' , PORT_NUMBER
	
	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()
