import numpy as np 
import matplotlib.pyplot as plt  
import pickle


def plot1():

    # creating the dataset 
    data = {'RF':82.5, 'SVM':77.7, 'XG':68,'ANN':58,'LSTM':63} 
    methods = list(data.keys()) 
    values = list(data.values()) 
    
    fig = plt.figure(figsize = (10, 5)) 
    
    # creating the bar plot 
    plt.bar(methods, values, color ='maroon', width = 0.4) 
    
    plt.xlabel("Methods") 
    plt.ylabel("Accuracy") 
    plt.title("Stock trend prediction accuracy with continuous data") 
    plt.show() 

def plot2():

    # creating the dataset 
    data = {'RF':97.2, 'SVM':95, 'XG':72.1,'ANN':65,'LSTM':76} 
    methods = list(data.keys()) 
    values = list(data.values()) 
    
    fig = plt.figure(figsize = (10, 5)) 
    
    # creating the bar plot 
    plt.bar(methods, values, color ='maroon', width = 0.4) 
    
    plt.xlabel("Methods") 
    plt.ylabel("Accuracy") 
    plt.title("Stock trend prediction accuracy with binary data") 
    plt.show()   


#plot2()
    