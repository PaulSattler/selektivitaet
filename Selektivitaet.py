from numpy import Infinity
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math 
from scipy.ndimage.filters import gaussian_filter1d

Sigma = 0.1

xBLinks = [1.21947691963578, 1.21947691963578, 1.23646087388146, 1.25368136782475, 1.27114169581205, 1.28884519807095, 1.30679526134918, 1.34344885445183, 1.38113052435202, 1.45969424722853, 1.52153615284769, 1.58599807378709, 1.66083045298657, 1.70938328098213, 1.75935550558264, 1.82826498199741, 1.88171260215731, 1.91820960712388, 2.01257921203653, 2.09140681640906, 2.15254714246898, 2.28024218806856, 2.39242260547135, 2.4861277086087, 2.58350300209366, 2.71060285431669, 2.78984479855805, 2.84395560131942, 2.87140330707114, 2.92709598864166, 2.92709598864166, 2.95534610245004, 2.98386886496325, 3.0126669075801, 3.0126669075801, 3.04174288709569, 3.07109948594647, 3.07109948594647, 3.13066540109361, 3.19138663480452, 3.28468384408218, 3.44627948799817, 3.721530378009, 4.21647531752444, 4.96435800357145, 5.7336853370728, 6.81583031914152, 8.66569449121857, 10.9123074515298, 13.6100095255165, 17.1384542244347, 21.3753622946617, 27.176785602254, 34.2224665705242, 44.3546013334198, 59.1670892775528, 80.4571227579622, 92.9255756108875]
yBLinks = [7842.54286194908, 6459.19644146858, 4986.63156741771, 3976.33048235961, 3170.71832782904, 2611.43520673379, 2016.081312307, 1556.45594704118, 1090.50187914774, 629.27082256526, 426.855399114582, 329.541085680853, 227.183064020714, 189.819309612168, 158.600600167779, 123.881349353979, 105.858274210462, 86.4838074168415, 67.5516407172121, 53.96242374101, 44.0860754378541, 32.191351045567, 25.7154868108758, 21.0089690727482, 16.0454313638902, 12.2545693109364, 10.0117049911117, 8.17933574700165, 6.83411798883221, 5.33806150295284, 4.26421525398298, 3.48376707971093, 2.78294521605071, 2.07824558737779, 1.66016943235236, 1.18532032773817, 0.0103668724729712, 0.00809746084928882, 0.00676570867925005, 0.00540466574581504, 0.00461835935368752, 0.00394644999763561, 0.00322416007743662, 0.00275508802055803, 0.00246242635940713, 0.00230197135617203, 0.00222570830971272, 0.00210417634403025, 0.00205744241336074, 0.00205744241336074, 0.00192337670705823, 0.00188065835128258, 0.00179804690193559, 0.00175811213149965, 0.00171906431561871, 0.00160704777986721, 0.00157135511573286, 0.00153645518862163]
yBLinksSmoothes = gaussian_filter1d(yBLinks, sigma=Sigma)
xBRechts = [1.3997532585089423, 1.4091209822168922, 1.4185513985793756, 1.437601990335818, 1.4569084241059047, 1.4863553070770257, 1.5163973674130156, 1.547046634777456, 1.578315381976248, 1.610216129871983, 1.653755688085088, 1.687181227675713, 1.7328018893469421, 1.7915663039269196, 1.8156263403097326, 1.8771995759116966, 1.9151413403429332, 1.993340994305867, 2.0609410571340545, 2.1308336371519387, 2.1739018270985024, 2.262667270696546, 2.339400980631425, 2.402657386582404, 2.500763449181725, 2.5855717016413036, 2.6911465791218863, 2.838649094350309, 2.915404956620718, 3.0344476893773193, 3.179488195965585, 3.3093140586662573, 3.490698510602477, 3.6332318108178856, 3.8323702875776404, 4.06947716034836, 4.321253719213173, 4.438098578962676, 4.619316416945395, 4.84011046640312, 4.9709849915679944, 5.173961815266002, 5.208588092766172, 5.208588092766172, 5.243446103536958, 5.243446103536958, 5.173961815266002, 5.173961815266002, 5.173961815266002, 5.173961815266002, 5.139565730492189, 5.173961815266002, 5.105398308141874, 5.173961815266002, 5.173961815266002, 5.173961815266002, 5.278537398432588, 5.34942609597951, 5.5678555459599375, 5.7952039759884535, 6.194933832930554, 6.491039231140076, 7.031949911201107, 7.7202416139829, 8.197889181614697]
yBRechts = [ 7791.431799014061,  6985.53753639846,  6070.6409478687365,  4956.482552153788,  4110.423187359445,  3408.7840724548446,  2783.1622598456984,  2344.365934986005,  1914.0991787203761,  1612.3202644410414,  1316.4074976286672,  1126.2923727948776,  891.3378255662401,  750.8085550634931,  642.3770379008349,  567.0203493346136,  477.62331740501196,  383.92875013105487,  318.39305802597204,  276.6930856070002,  240.454562977556,  208.96220348219887,  176.0170000186914,  150.59668450719312,  130.87302084042344,  113.73256748610434,  97.30734862018495,  80.69722385990693,  71.2307030975187,  60.00039461449987,  52.96180079179647,  43.2416022969277,  36.99666474263516,  31.653618954267895,  25.844159028122686,  22.459346792121234,  17.774128473986693,  15.935689977741218,  13.423252130612646,  10.296772105186584,  8.276871544310236,  6.154060016913094,  4.575696806337789,  3.5651229599547225,  2.56934358789622,  2.0333557982684334,  1.4204083253657538,  1.0895735757839349,  0.7040229081609339,  0.49179784514426095,  0.3329956891757991,  0.25148265923450297,  0.09561476871188007,  0.05539081619429363,  0.010938305337723784,  0.004290568282334249,  0.003670925864562201,  0.0031901443165805636,  0.002815911276540027,  0.0026046499504365065,  0.002335242156679725,  0.002263518671483123,  0.0021939980663236223,  0.0021266126830214106,  0.0021266126830214106]
yBRechtsSmoother = gaussian_filter1d(yBRechts, sigma=Sigma)

xCLinks = [1.216798880819914, 1.2249421986899547, 1.2331400149877776, 1.241392694439246, 1.2580641139273772, 1.2664835956856921, 1.2920816316431605, 1.3181970524661821, 1.3358999245131364, 1.3720220893897528, 1.3904478106797686, 1.4185513985793756, 1.466658653656609, 1.5265457214054325, 1.578315381976248, 1.6209923575557048, 1.6648233003747952, 1.709839413216098, 1.7443985112810867, 1.8156263403097326, 1.8771995759116966, 1.9408609412451616, 2.020110786046887, 2.088618691340944, 2.1594499014360036, 2.277809969387231, 2.3708182229543056, 2.4676242188035977, 2.5855717016413036, 2.6911465791218863, 2.876771044031103, 2.9942362647095613, 3.137354745940506, 3.2873140032021433, 3.4215426432000053, 3.537577229510304, 3.6820246963303376, 3.8068929960933415, 3.9623372490564717, 4.15172901345846, 4.2925263697347384, 4.467800157454199, 4.619316416945395, 4.807933798723468, 5.0042528647980085, 5.173961815266002, 5.173961815266002, 5.173961815266002, 5.139565730492189, 5.243446103536958, 5.278537398432588, 5.457548145110798, 5.6426296733346355, 5.873031304065833, 6.153750407753944, 6.491039231140076, 6.801297872824575, 7.222090841248008, 7.928993658466498, 9.815569357306765, 13.251689486899927, 16.29565727125395, 20.718412993602424, 25.308145489502813, 33.490813253283655, 39.30508708278413, 49.972763502282895, 63.113341747404704, 81.8646036399463, 92.92557561088759]
yCLinks = [ 7791.431799014061,  6877.425748172152,  5703.4661107291995,  4584.626703746667,  3516.7972631739385,  2871.351546578195,  2272.3622265258687,  1884.4755908467585,  1491.3573207548623,  1217.645155235776,  978.7817418394326,  774.5992164629391,  594.183252103674,  421.5937437152821,  338.8904041936162,  281.04264681931517,  233.06935916096438,  190.29361512947807,  157.81096368326172,  126.85345090159143,  101.9688216209104,  84.56299489971535,  62.87469160742344,  54.63998661059827,  43.92135183131328,  32.656618354753434,  26.663075691291965,  21.43262473118951,  17.228222587164602,  13.634263029863522,  10.623043052700034,  8.406982346860543,  6.653211497854259,  5.781839685672733,  4.870268685445908,  4.16690613184791,  3.455625517425704,  2.910807919467243,  2.5295790989921194,  2.0977861766584525,  1.8808050251097335,  1.6091798005642435,  1.355474800064132,  1.2152734362236717,  1.0236721324807425,  0.9035860498066898,  0.7611257112306554,  0.5838479316101794,  0.005421551955655846,  0.004358015176927552,  0.003503110629147019,  0.0030443078602621467,  0.0027723307786889874,  0.00252465200605712,  0.002371951706843497,  0.002299100742481522,  0.0022284872870001696,  0.0021939980663236223,  0.0021266126830214106,  0.00209370012635298,  0.001997987275547531,  0.001997987275547531,  0.0018480899954426006,  0.001819487999795257,  0.0017636051354655612,  0.0017094386300929214,  0.0016569357682679612,  0.0016312921742066284,  0.001556718159272642,  0.001556718159272642]
yCLinksSmoother = gaussian_filter1d(yCLinks, sigma=Sigma)
xCRechts = [1.3904478106797686, 1.3997532585089423, 1.4091209822168922, 1.4280449271613862, 1.437601990335818, 1.4569084241059047, 1.4863553070770257, 1.5163973674130156, 1.536761992350864, 1.5678228674164978, 1.5995115416889343, 1.6209923575557048, 1.687181227675713, 1.709839413216098, 1.7560727425721405, 1.8156263403097326, 1.9024096337226968, 2.020110786046887, 2.0886186913409444, 2.2178405068631966, 2.323848829818807, 2.402657386582404, 2.500763449181725, 2.6378310104982745, 2.7455397565257216, 2.915404956620718, 3.0344476893773193, 3.179488195965585, 3.2873140032021433, 3.4674926257936134, 3.609078376016901, 3.7815850756073166, 3.9623372490564717, 4.15172901345846, 4.408594454191958, 4.588607570466181, 4.84011046640312, 5.071458028085533, 5.421266801073329, 5.6426296733346355, 6.0318355686654535, 6.4050222811784145, 6.801297872824575, 7.174078958344891, 7.516985527492598, 8.035476949363211, 8.363584073172055, 8.763346598363364, 9.243668136812905, 9.462003974042654, 9.881259178863893, 9.947388623686793, 10.01396063391491, 10.01396063391491, 10.01396063391491, 10.216361774566748, 10.28473386359231, 10.70468335363349, 11.067710687806914, 11.51963093396138, 12.070246161971614, 12.731819813191308, 13.340375235636134, 14.071565025375998, 14.942165861879625, 15.8666303457568]
yCRechts = [ 7791.431799014061,  7206.886317123965,  6461.45357971259,  5528.292642747683,  4879.773467243177,  4175.03823627806,  3516.7972631739385,  2826.913026462964,  2418.65120488538,  1944.1884436039652,  1637.6656237898594,  1423.1803841714618,  1143.9974687053439,  948.7199182419429,  837.4264142755603,  662.7318600407964,  508.37150813280994,  366.3775665978015,  289.9479668295769,  222.41466581691185,  178.78395284770698,  152.9640349460331,  124.89020135233484,  103.5717515619127,  88.61395428947452,  70.1282999326421,  58.15757184658521,  50.54066852277232,  43.92135183131328,  37.57824507955098,  33.1699740109297,  28.825699013322964,  24.662701327415657,  20.77435358006506,  18.337332328475416,  16.44063974405675,  14.512002672795822,  12.611364150864643,  10.959652456780637,  9.673985211141726,  8.539138465790296,  7.537419599728118,  6.55024295910789,  5.69235694731525,  5.183804362994748,  4.36652024841358,  3.854287576534359,  3.2213953724606212,  2.5295790989921194,  2.1642581424888085,  1.4427368665510427,  1.1597175886478703,  0.8896016852317483,  0.004711490723729019,  0.00415878986706251,  0.003614112719174883,  0.003291229530300221,  0.0029508064779216266,  0.0027294247551400267,  0.00252465200605712,  0.002335242156679725,  0.0021939980663236223,  0.00209370012635298,  0.0020293952449131373,  0.0019670653921438023,  0.0019366220717844695]
yCRechtsSmoother = gaussian_filter1d(yCRechts, sigma=Sigma)

xDLinks = [1.216798880819914, 1.216798880819914, 1.216798880819914, 1.2331400149877776, 1.241392694439246, 1.249700604211116, 1.2664835956856921, 1.2749594240739555, 1.3007287726015913, 1.3007287726015913, 1.3270189685467995, 1.3538405392239246, 1.381204224724303, 1.3997532585089423, 1.4280449271613862, 1.4569084241059047, 1.476474135748048, 1.5063164788671373, 1.536761992350864, 1.578315381976248, 1.6209923575557048, 1.6427616523976354, 1.698472537404788, 1.7443985112810867, 1.8035562014589586, 1.8277772574871034, 1.8771995759116966, 1.9279582527729962, 1.9669259463515782, 2.006681250938153, 2.074733721151259, 2.1308336371519387, 2.203096480368107, 2.277809969387231, 2.339400980631425, 2.418736956624873, 2.484138573570252, 2.5855717016413036, 2.655484459021718, 2.7455397565257216, 2.857646499970226, 2.974330821246507, 3.075199137787647, 3.179488195965585, 3.2873140032021433, 3.376201573480398, 3.514059698723522, 3.6332318108178856, 3.7815850756073166, 3.9098297610030595, 4.042423601317552, 4.179514089200869, 4.350173323913119, 4.49770051110792, 4.650230779637884, 4.807933798723468, 5.020970199371848, 5.243446103536961, 5.421266801073329, 5.6426296733346355, 5.912336041704547, 6.194933832930554, 6.447887320933533, 6.711169485370911, 6.985202070009619, 7.222090841248008, 7.567292281993901, 7.876282342112565, 8.25275282302787, 8.53262797280697, 8.821994513052218, 9.06053748658911, 9.30553056051313, 9.557148142791045, 9.750316236435049, 9.881259178863893, 9.947388623686793, 10.01396063391491, 10.01396063391491, 10.148444217726434, 10.422853826221214, 10.63351947395003, 10.994133431409965, 11.4430493478742, 11.990004129840067, 12.479583752093825, 13.163593313935761, 13.792786642744453, 14.452054149292913, 15.142833318890208, 16.29565727125395, 17.074556968251674, 18.252291219288956, 19.252704531745998, 20.857069122753355, 22.595128475275093, 24.641840616452395, 27.05379955412325, 29.90061948684712, 33.490813253283655, 37.01498790911489, 41.4594101698137, 44.6157152078551, 49.64054856309743, 55.231302471900975, 61.45171358985225, 67.46664616470524, 72.60288216799647, 81.3203742955267, 92.30781380852248]
yDLinks = [ 7670.847574787127,  7095.34882079986,  6461.45357971259,  5793.123482963711,  4513.672652077846,  3802.042216466355,  3252.9525676236394,  2740.088602697902,  2344.365934986005,  1944.1884436039652,  1637.6656237898594,  1337.101166134064,  1074.804266889086,  919.5813987881412,  762.6111187662119,  642.3770379008349,  558.2448494381689,  477.62331740501196,  408.64511971504686,  333.6455611991864,  281.04264681931517,  240.454562977556,  199.40956127038953,  160.2917211803598,  128.84756234994742,  117.33637964954302,  101.9688216209104,  87.2425189475095,  75.81635703170545,  66.92240648868233,  56.371348635652815,  48.23021756322917,  40.626190116011095,  33.69139951766013,  28.825699013322964,  24.662701327415657,  21.100922356962922,  17.228222587164602,  15.207194861309109,  12.809612329797774,  10.790035212686305,  9.23174198272821,  7.655906362272258,  6.653211497854259,  5.69235694731525,  4.946828357044838,  4.232409081611487,  3.678090017423196,  3.146901503173653,  2.734751481118656,  2.3397995986971236,  2.0333557982684334,  1.7396992427446516,  1.511850649281158,  1.3344967717066798,  1.1417692000388435,  1.0078292536438205,  0.8622788942659004,  0.7730904586113213,  0.6718387196402013,  0.6023481582738595,  0.5234585564013541,  0.476693006716678,  0.4207725669602526,  0.3714121050899945,  0.3329956891757991,  0.29393225607875734,  0.26767248181872866,  0.23261538861964193,  0.20214972661743763,  0.18408976185372627,  0.16249435287464206,  0.1390269734824724,  0.11710783283421697,  0.09561476871188007,  0.07566868256790334,  0.06275222481089869,  0.004937192966296092,  0.004358015176927552,  0.0037286321014880605,  0.003291229530300221,  0.0029508064779216266,  0.002687182767380339,  0.00252465200605712,  0.002371951706843497,  0.0022284872870001696,  0.0021266126830214106,  0.0020612969414169216,  0.0020293952449131373,  0.001997987275547531,  0.0019670653921438023,  0.0019366220717844695,  0.0019670653921438023,  0.0019366220717844695,  0.0019066499079805834,  0.0018771416088698453,  0.0018480899954426006,  0.001791328663410735,  0.0017636051354655612,  0.0017636051354655612,  0.0017636051354655612,  0.0016829824746146152,  0.0016829824746146152,  0.0016569357682679612,  0.0016569357682679612,  0.0016312921742066284,  0.0015811894643984132,  0.0015811894643984132,  0.0015811894643984132,  0.001532625584708927]
yDLinksSmoother = gaussian_filter1d(yDLinks, sigma=Sigma)
xDRechts = [1.3904478106797686, 1.3904478106797686, 1.4091209822168922, 1.4185513985793756, 1.4280449271613862, 1.4569084241059047, 1.466658653656609, 1.4963026072628987, 1.5063164788671373, 1.536761992350864, 1.578315381976248, 1.5888781167528832, 1.6318407041810634, 1.653755688085088, 1.709839413216098, 1.7443985112810867, 1.7678251026137959, 1.8277772574871034, 1.8771995759116966, 1.9279582527729962, 1.9669259463515782, 2.0609410571340545, 2.102596585453927, 2.1739018270985024, 2.2476252394569296, 2.3084000684622503, 2.402657386582404, 2.484138573570252, 2.5683830275432404, 2.655484459021718, 2.7639140362153594, 2.857646499970226, 2.9545577075812477, 3.054755459612905, 3.179488195965585, 3.3537568551617833, 3.490698510602477, 3.6332318108178856, 3.7564454001547083, 3.9623372490564717, 4.15172901345846, 4.379286470485479, 4.681352033942557, 4.937938280501276, 5.173961815266002, 5.494072298803923, 5.873031304065833, 6.194933832930554, 6.534479931652934, 7.174078958344891, 7.668918064542428, 8.25275282302787, 9.000303757270597, 9.685496913097486, 10.562828686053052, 11.2163457236632, 11.990004129840067, 12.56310225213601, 13.340375235636134, 13.978018385336062, 14.16573771795226, 14.646139597247698, 15.042164972824052, 15.244175378874406, 15.44889870585247, 15.656371387227678, 15.656371387227678, 15.656371387227678, 15.8666303457568, 15.8666303457568, 15.8666303457568, 16.18732504365744, 16.62502341717256, 16.961046677699773, 17.536245715054427, 18.497412368220594, 19.511260841097233, 20.443859932020843, 21.42103538689524, 22.14748577452858]
yDRechts = [ 7791.431799014061,  7206.886317123965,  6770.987153840034,  6070.6409478687365,  5275.568462114485,  4513.672652077846,  3861.809576810935,  3252.9525676236394,  2783.1622598456984,  2381.2189091610503,  2037.324081011541,  1743.0944274383799,  1491.3573207548623,  1275.9760017348483,  1074.804266889086,  905.3494819278258,  774.5992164629391,  652.4750793520917,  541.0991902266693,  477.62331740501196,  408.64511971504686,  344.2176950945537,  285.4605822835499,  248.07377968888827,  212.24704846888224,  184.44903012628822,  155.36859967095526,  135.0199577714682,  117.33637964954302,  98.83700111693264,  85.89230864749513,  78.218728803466,  66.92240648868233,  60.00039461449987,  49.75847502317705,  41.9135008778308,  36.4240852435065,  32.656618354753434,  28.379577601625503,  24.28100861885812,  21.769541401891164,  18.337332328475416,  15.68906100593529,  14.06628812199511,  12.809612329797774,  10.790035212686305,  9.376863161893505,  8.406982346860543,  7.420766599541283,  6.55024295910789,  5.69235694731525,  5.103577128286112,  4.4351610930650605,  3.976417312604924,  3.5651229599547225,  3.2466164939186384,  2.910807919467243,  2.4518868440192323,  2.0653197538966754,  1.7396992427446516,  1.4884524674843767,  1.2935096906981252,  1.0727107721602547,  0.8758337499084592,  0.749346136462442,  0.6214345964629693,  0.5153572413200121,  0.4015370797872902,  0.3329956891757991,  0.0029508064779216266,  0.002687182767380339,  0.002447111079406293,  0.0021939980663236223,  0.0020293952449131373,  0.0019366220717844695,  0.0019066499079805834,  0.0018771416088698453,  0.0018771416088698453,  0.0018480899954426006,  0.0018480899954426006]
yDRechtsSmoother = gaussian_filter1d(yDRechts, sigma=Sigma)

xThermik = [1.2920816316431605, 1.309433783778841, 1.3270189685467995, 1.3358999245131367, 1.3629009961572993, 1.3720220893897528, 1.3997532585089423, 1.4185513985793756, 1.437601990335818, 1.466658653656609, 1.4963026072628987, 1.5265457214054325, 1.5574001062552405, 1.5888781167528832, 1.6209923575557048, 1.653755688085088, 1.687181227675713, 1.7443985112810867, 1.8035562014589586, 1.84000949359281, 1.889762566470871, 1.9538499798079314, 2.020110786046887, 2.0609410571340545, 2.203096480368107, 2.2930540092369136, 2.3550572128248084, 2.434924137754213, 2.5174995852889053, 2.6202949206901915, 2.727287627579447, 2.8197779819651543, 2.934916043995861, 3.054755459612905, 3.2221874817838, 3.331461347537326, 3.4674926257936134, 3.6332318108178856, 3.7815850756073166, 3.9623372490564717, 4.124128650679696, 4.321253719213173, 4.527800970208863, 4.744220765069356, 4.9709849915679944, 5.208588092766172, 5.494072298803923, 5.756677922964344, 6.072203089666425, 6.4050222811784145, 6.801297872824575, 7.174078958344891, 7.823921446378377, 8.197889181614697, 8.647217837003884, 9.243668136812905, 9.947388623686793, 10.63351947395003]
yThermik = [ 7913.911583671649,  6877.425748172152,  5884.190251561756,  4804.2515717649785,  3984.177660407532,  3304.088346035296,  2826.913026462964,  2308.0833164806218,  1944.1884436039652,  1587.3671629690402,  1316.4074976286672,  1108.8612900966552,  948.7199182419429,  786.775764711789,  652.4750793520917,  549.6051637122799,  470.23137216469524,  377.9868704243201,  328.48189010486294,  268.19486953430237,  233.06935916096438,  190.29361512947807,  165.37084026873225,  137.14244511126893,  98.83700111693264,  83.2542542983308,  69.04295812873887,  60.00039461449987,  51.33515795126266,  43.2416022969277,  36.99666474263516,  31.653618954267895,  27.082214028534633,  22.81240333289688,  19.517843771966874,  16.44063974405675,  14.06628812199511,  12.224024881831562,  10.13741393991298,  9.08886677391338,  7.537419599728118,  6.757798681899384,  5.69235694731525,  4.946828357044838,  4.232409081611487,  3.7359088734314323,  3.146901503173653,  2.8657587521387184,  2.3765807909584202,  2.1307629652388678,  1.8230388996609053,  1.6344757924348745,  1.3344967717066798,  1.2537814668447314,  1.1597175886478703,  1.0236721324807425,  0.932217729095956,  0.8622788942659004]
yThermikSmoother = gaussian_filter1d(yThermik, sigma=Sigma)

plt.plot(xBLinks, yBLinksSmoothes)
plt.plot(xBRechts, yBRechtsSmoother)
plt.plot(xCLinks, yCLinksSmoother)
plt.plot(xCRechts, yCRechtsSmoother)
plt.plot(xDLinks, yDLinksSmoother)
plt.plot(xDRechts, yDRechtsSmoother)
plt.plot(xThermik, yThermikSmoother)



plt.xlabel('I in Ampere')
plt.ylabel('T in s')
plt.title("Selektivität",fontsize=16)


plt.semilogx(2) #loglog
plt.semilogy(2) #loglog


plt.grid(True, 'both', 'both') #grid für loglog mit (Visible, which, axis)
plt.legend(['Minimum B','Maximum B','Minimum C', 'Maximum C', 'Minimum D', 'Maximum D', "Thermik"], loc='upper right')
plt.show()