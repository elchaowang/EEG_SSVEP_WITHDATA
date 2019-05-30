import numpy as np
import pandas as pd
import scipy.io as scio
import matplotlib.pyplot as plt
import h5py


def loadPersonalData(filename):
    dataFile = 'D://Python Projects/EEG_minimumEnergy_SSVEP/'+filename+'.mat'
    SubData = h5py.File(dataFile, 'r')
    # SubData = scio.loadmat(dataFile)
    dataset = SubData['y']
    dataset = np.transpose(np.array(dataset))
    return dataset

ssvep = loadPersonalData('Mohamed_TEST1')

trig = 9
# for i in range(0, 11):
#     plt.plot(ssvep[i])
# plt.show()
print(ssvep[trig])
l = list()
count = 0
for index in range(0, len(ssvep[trig]-1)):
    if ssvep[trig][index] == 1: # and ssvep[trig][index-1] == 0:
        l.append(index)
        if ssvep[trig][index+1] == 0:
            print(len(l))
            l = list()
            count += 1
            print(count)





























