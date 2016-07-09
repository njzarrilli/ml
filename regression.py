import numpy as np
from numpy.linalg import inv

X_train = np.array([
    [90,85,95],
    [75,80,85],
[95.9671959974, 81.991583949, 91.5570468897],
[93.2434116756, 73.8935186774, 91.7967803287],
[75.5813101869, 77.2624380774, 80.103030044],
[76.6728103576, 73.9023238097, 82.5870451219],
[83.8867225959, 73.2591995827, 69.9015021091],
[95.7798228498, 97.2498095167, 85.4399406649],
[77.1410995, 91.912324582, 72.4659061079],
[66.5787294455, 70.6495587983, 75.8091779161],
[75.0147688469, 96.6756294525, 89.7813484213],
[70.7245112457, 99.5851085662, 80.2335823424],
[78.6624717322, 92.3580535404, 80.220963373],
[91.4118544052, 89.4074002133, 91.0039386499],
[85.6480601656, 100, 80.6916735262],
[83.3946158666, 100, 69.83780783],
[68.0845779814, 78.2208611696, 79.4035889595],
[95.5486218542, 93.6926445833, 86.1015266803],
[73.9041098302, 75.7958530381, 79.9029477072],
[91.7855188544, 89.7836771728, 65.1242826704],
[68.4676776685, 71.3171604125, 97.4324384198],
[100, 69.2840584144, 88.665197265],
[94.3730795425, 83.0206410834, 86.8139108547],
[89.9321867528, 100, 80.8974181088],
[64.314806019, 97.7214514869, 100],
[79.6837161883, 95.1442448664, 87.6418995414],
[94.8373605616, 100, 78.7810803413],
[75.8258822052, 86.0707729058, 100],
[92.4163219696, 92.9253893501, 83.587995822],
[78.2355033614, 82.9620797117, 98.3472012346],
[91.7168632331, 91.5826079371, 79.4515765909],
[83.1518247152, 86.6301913608, 83.0776562326],
[92.1643879482, 84.2020685955, 83.8765219035],
[84.1020826094, 99.4777888903, 67.0782650721],
[79.8899327728, 88.42049012, 73.9653709586],
[71.6418857543, 74.7137733442, 68.9511500925],
[72.4264065576, 83.6737873776, 83.0647420619],
[99.9832057646, 85.2442176286, 89.8092898481],
[74.3379595083, 74.5319307496, 87.7251968331],
[98.2306029857, 93.4078188015, 79.7541236148],
[84.0400178418, 82.102077878, 78.6361558314],
[83.1480731371, 71.8818530453, 81.5545202898],
[59.9060619001, 83.7404716713, 100],
[90.7219427277, 68.1399988124, 89.6189569086],
[85.6967122278, 88.5165281616, 78.226163762],
[63.332237609, 69.8001573373, 79.9942946679],
[91.6791542221, 89.9587876907, 74.7116884319],
[91.3722410536, 82.7658261771, 90.6178510154],
[79.3264957173, 73.9472582162, 89.0813661455],
[79.4025771705, 83.2309834465, 88.1769488411],
[81.9349329308, 88.1957550538, 88.5580058932],
[79.925247077, 86.4071750469, 91.9475247565],
[62.6603592786, 89.6411725231, 90.4802026083],
[84.9107531335, 70.6399318428, 77.5974282993],
[85.076932115, 73.1998759543, 95.3587229381],
[78.4679542921, 71.6502568582, 94.1688175342],
[67.2705886002, 83.7446576395, 87.1910440394],
[82.4394765148, 70.0404534677, 80.2419754172],
[87.9151769088, 92.2816402371, 92.0267286918],
[76.2205987622, 83.1927776999, 86.2555651536],
[91.9310969854, 79.1402084551, 89.6447259102],
[88.7137338341, 79.2584441306, 100],
[91.0705502303, 67.1020701667, 69.809777485],
[84.1108851044, 100, 85.0651951333],
[84.6248432177, 81.4422835315, 89.0266768766],
[100, 93.2957668991, 79.9437157378],
[71.4669887478, 75.038877912, 60.4576902569],
[90.906509258, 84.0264932418, 100],
[80.3831382282, 96.9752801036, 89.3491429717],
[89.9797242557, 80.1641167686, 69.8489062305],
[74.6266354852, 78.0247727643, 95.9248020464],
[79.0634828385, 71.640729626, 85.1487996184],
[81.2435026586, 99.5454328609, 91.4135090373],
[67.9902605074, 91.4749445932, 100],
[68.5627503713, 62.883492544, 67.6894777608],
[85.3116821972, 82.6760266356, 95.8200950706],
[94.8684587224, 82.4112609571, 90.8211117287],
[100, 80.7124778421, 85.4413292895],
[99.0933739692, 90.6245174603, 96.5722251099],
[71.2444064279, 80.7482823065, 96.5011435779],
[87.2639034955, 69.7096510267, 82.6037257644],
[96.1924612208, 99.4070246762, 86.4122261334],
[82.5162511182, 79.0674962299, 78.8925043126],
[86.3889239538, 73.9694930525, 80.1740525],
[81.19284575, 79.5369409606, 76.5388096349],
[100, 86.911286676, 92.4122730747],
[97.1913568709, 65.858078876, 81.8917113722],
[73.9683276763, 94.7627322646, 86.6137957292],
[99.9773174621, 89.2061720646, 84.1328587369],
[76.0263068559, 96.7671994913, 84.2419731416],
[80.6281202161, 86.3300279432, 88.8645759276],
[80.4426940885, 76.5668768515, 79.8275452532],
[83.556642154, 81.5923681933, 98.7204602068],
[95.3579296452, 91.1481956542, 80.1241314842],
[96.5036157363, 86.8585884483, 100],
[97.706937339, 85.8916765801, 85.7752753317],
[90.6759402896, 83.7104525563, 83.6793732735],
[88.1869347665, 81.1030806237, 97.8877635785],
[89.9922317499, 83.021963826, 91.2266844315],
[88.5472544476, 87.2839222574, 75.0782387921],
[90.8987792192, 83.9376688677, 79.5218307426],
[79.1038581542, 66.1273102206, 77.0978442959],
])
y_train = np.array([
    90,
    80,
89.8386089454,
86.3112368939,
77.6489261027,
77.7207264297,
75.6824747625,
92.8231910105,
80.5064433966,
71.01248872,
87.1572489069,
83.5144007181,
83.7471628819,
90.6077310894,
88.7799112306,
84.4108078989,
75.2363427035,
91.7809310393,
76.5343035251,
82.2311595659,
79.0724255003,
85.9830852265,
88.0692104936,
90.2765349539,
87.3454191686,
87.489953532,
91.2061469676,
87.298885037,
89.6432357139,
86.5149281026,
87.583682587,
84.2865574362,
86.7476594824,
83.5527121906,
80.7585979505,
71.768936397,
79.7216453324,
91.6789044138,
78.8650290303,
90.4641818006,
81.5927505171,
78.8614821574,
81.2155111905,
82.8269661495,
84.1464680504,
71.0422298714,
85.4498767816,
88.2519727487,
80.7850400263,
83.6035031527,
86.2295646259,
86.0933156268,
80.9272448034,
77.7160377585,
84.5451770025,
81.4290095615,
79.4020967597,
77.5739684666,
90.7411819459,
81.8896472052,
86.9053437836,
89.3240593216,
75.9941326273,
89.7253600793,
85.0312678752,
91.0798275457,
68.9878523056,
91.6443341666,
88.9025204345,
79.9975824183,
82.8587367653,
78.6176706943,
90.7341481856,
86.4884017002,
66.3785735587,
87.9359346345,
89.3669438027,
88.7179357105,
95.4300388465,
82.8312774374,
79.8590934289,
94.0039040102,
80.1587505536,
80.1774898354,
79.0895321151,
93.1078532502,
81.6470490397,
85.1149518901,
91.1054494212,
85.6784931629,
85.2742413623,
78.9457053977,
87.9564901847,
88.8767522612,
94.4540680615,
89.7912964169,
86.0219220398,
89.0592596562,
88.0802933358,
83.6364718324,
84.7860929432,
74.1096708902,
])

new_friend = np.array([50, 50, 90])
#new_friend = np.array([65, 55, 70])

# x is a N x w array, y is corresponding values. Returns the weight vector ure
# sposed 2 dot w/ the new d8a
def train(X, y):
    ones_vector = np.ones((len(y), 1))
    X = np.append(X, ones_vector, axis=1)

    transpose_normal = np.dot(X.T, X)
    inverse = inv(transpose_normal)
    hi = np.dot(inverse, X.T)
    return np.dot(hi, y)

# x is a vector, w is the weight vector
def predict(w, x):
    ones_vector = np.ones(1)
    x = np.append(x, ones_vector)

    return np.dot(w.T, x)

def main():
    w = train(X_train, y_train)
    score = predict(w, new_friend)
    print("This friend will probably get a " + str(score))

main()

# Addons: logistic reguression
# Non-linear data modelling
# k-fold cross-validation to see %error

