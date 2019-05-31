import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import h5py


def loadPersonalData(filename):
    # dataFile = 'D://Python Projects/EEG_minimumEnergy_SSVEP/'+filename+'.mat'
    SubData = h5py.File(filename+'.mat', 'r')
    dataset = SubData['y']
    ssvep = np.transpose(np.array(dataset))
    eeg_signal = ssvep[1:9]

########## get the heads and ends of triggle signals #################
    trig = 9
    head = list()
    end = list()
    for index in range(0, len(ssvep[trig])-1):
        if ssvep[trig][index] == 0 and ssvep[trig][index+1] == 1:
            head.append(index+1)
        elif ssvep[trig][index] == 1 and ssvep[trig][index+1] == 0:
            end.append(index-1)

######### triggle the eeg signals into 24 trial 8 chs * 1882 samples ######
    test_x_signal = list()
    for i in range(len(head)):
        ch_x_signals = list()
        for x in range(len(eeg_signal)):
            tmp = eeg_signal[x][head[i]:end[i]]
            tmp = np.transpose(np.array([tmp]))
            ch_x_signals.append(tmp)
        test_x_signal.append(ch_x_signals)
    test_x_signal = np.array(test_x_signal)
    print(test_x_signal.shape)
    return test_x_signal


def load_all_data():
    test1_data = loadPersonalData('mohamed_TEST1')
    test2_data = loadPersonalData('mohamed_TEST2')
    test3_data = loadPersonalData('Mohamed_Test1_SSVEP')
    test4_data = loadPersonalData('Mohamed_feedback1_SSVEP')
    data = np.vstack((test1_data, test2_data, test3_data, test4_data))
    return data




















