#!/usr/bin/python3
# coding: UTF-8

import numpy as np
import pandas as pd
import pylab as plt
import argparse

# Scaling data to the [0,1] range
# y = (x - min) / (max / min)
def scaling(series):
    minimum = np.amin(series)
    maximum = np.amax(series)
    new = np.zeros(len(series))
    for i in range(len(series)):
        new[i] = (series[i] - minimum)/(maximum - minimum)
    return new

# Binarization
def binarization(matrix, threshold):
    matrix[matrix < threshold] = 0.0
    matrix[matrix >= threshold] = 1.0
    return matrix

# Recurrence (Distance) Plot 
def rplot(series, err=0.03, bin=0):
    dim = len(series)
    rp = np.zeros((dim,dim))
    for x in range(dim):
        for y in range(dim):
            rp[x,y] = abs(series[x] - series[y])
    if (bin == 1):
        rp = binarization(rp, err)
    return rp

#### Main 
if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('timeSeries', help='Time Series file. Can be a spreadsheet but you \
                        need to use --column to set which data column will be loaded')
    parser.add_argument('-b', action='store_true',
                        help='create Recurrence Plot, otherwise Distance Plot')
    parser.add_argument('--epsilon', type=float, default=0.05,
                        help='threshold distance')
    parser.add_argument('--column',type=int, default=0,
                        help='column of the spreadsheet to be used')
    parser.add_argument('--output', default='recurrencePlot.png', help='Output picture name (you must include extension, e.g., .png, .pdf)')
    args = parser.parse_args()

    dataframe = pd.read_csv(args.timeSeries, usecols=[args.column], engine='python')
    plt.plot(dataframe)
    plt.figure()
    dataset = dataframe.values
    dataset = dataset.astype('float32')
    new_dataset = scaling(dataset)
    rp = []
    if args.b:
        rp = rplot(new_dataset, err=args.epsilon, bin=1)
    else:
        rp = rplot(new_dataset)
    
    plt.imshow(rp,cmap='gray' ,origin='lower')
    plt.xticks([])
    plt.yticks([])
    plt.savefig(args.output, bbox_inches='tight')

