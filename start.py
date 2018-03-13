# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 14:37:57 2018

@author: Gosia
"""
import utils
import math

trainingStep = 0.0001
epochAmount = 1500000

def learn(inputs, weights, z):
    y = 0
    i = 0
    while i<len(inputs):
        y = y + inputs[i]*weights[i]        
        delta = z - y
        weights[i] = weights[i] + trainingStep*delta*inputs[i]
        i = i+1
        
    return weights
    
def test(inputs, weights, z):
    y = 0
    i = 0
    while i<len(inputs):
        y = y + inputs[i]*weights[i]  
        i = i +1
    return y;
    
def singlePattern(output, inputsAmount):
    print('\n*** Single pattern ***\n----------------------------------------------------')
    print('Desired output: ' + str(output))
    print('The number of neuron\'s inputs: ' + str(inputsAmount))
    print('The number of training epochs: ' + str(epochAmount)+ '\n')
    spRanges = [-2,2,-1,1]
    
    inputs = utils.getRandomFromRange(inputsAmount,spRanges[0],spRanges[1])
    weights = utils.getRandomFromRange(inputsAmount,spRanges[2],spRanges[3])
    
    print('Inputs range: [' + str(spRanges[0])+ ', '+ str(spRanges[1])+']')
    print('Randomly chosen inputs: ' + str(inputs)+ '\n')
    print('Weights range: [' + str(spRanges[2])+ ', '+ str(spRanges[3])+']')
    print('Randomly chosen weights: ' + str(weights)+ '\n')
    
    #training
    k = 0
    while k<epochAmount:
        weights = learn(inputs, weights, output)
        k=k+1
        
    #testing
    y = test(inputs, weights, output)
    print('difference between expected(' + str(output) + ') and the result('+ str(round(y,10)) + ') is: ' + str(round(math.fabs(output-y),10)))

def multiplePattern(patternsAmount, inputsAmount):
    print('\n*** Multiple patterns ***\n----------------------------------------------------')
    print('The number of neuron\'s inputs : ' + str(inputsAmount))
    print('The number of training epochs: ' + str(epochAmount)+ '\n')
    
    patterns = []
    outputs= []
    mpRanges = [-5,5,-1,1]
    i = 0
    
    while i<patternsAmount:
        patterns.append(utils.getRandomFromRange(inputsAmount,mpRanges[0],mpRanges[1]))
        outputs.append(utils.getRandomFromRange(1,mpRanges[0],mpRanges[1])[0])
        i = i+1
    weights = utils.getRandomFromRange(inputsAmount,mpRanges[2],mpRanges[3])
    
    print('Patterns range: [' + str(mpRanges[0])+ ', '+ str(mpRanges[1])+']')
    print('Randomly chosen patterns: ' + str(patterns)+ '\n')
    print('Weights range: [' + str(mpRanges[2])+ ', '+ str(mpRanges[3])+']')
    print('Randomly chosen weights: ' + str(weights)+ '\n')
    
    #training
    k = 0
    while k<epochAmount:
        i = 0
        for pattern in patterns:
            weights = learn(pattern, weights, outputs[i])
            i = i+1
        k = k+1
        
    #testing
    i = 0
    for pattern in patterns:
        y = test(pattern, weights, outputs[i])
        print('For pattern no ' + str(i) + ' - ' + str(pattern) + ' :')
        print('difference between expected(' + str(outputs[i]) + ') and the result('+ str(round(y,10)) + ') is: ' + str(round(math.fabs(outputs[i]-y),10)))
        i = i+1
    
def start():
    #multiplePattern(6,3)
    singlePattern(3,4)
    
start()
        

