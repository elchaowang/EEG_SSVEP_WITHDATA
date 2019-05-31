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
# for i in range(1, 9):
#     plt.plot(ssvep[i]+i*250)
# plt.show()
print(ssvep[trig])
head = list()
end = list()
count = 0
for index in range(0, len(ssvep[trig])-1):
    if ssvep[trig][index] == 0 and ssvep[trig][index+1] == 1:
        head.append(index+1)
    elif ssvep[trig][index] == 1 and ssvep[trig][index+1] == 0:
        end.append(index+1)

chx_signal = ssvep[1:9]

for i in range(len(chx_signal)):
    plt.plot(chx_signal[i]+i*250)
plt.show()


# for i in range(len(head)):
#     chx_signal.append(ssvep[])





    # if ssvep[trig][index] == 1: # and ssvep[trig][index-1] == 0:
    #     l.append(index)
    #     if ssvep[trig][index+1] == 0:
    #         print(len(l))
    #         l = list()
    #         count += 1
    #         print(count)





























