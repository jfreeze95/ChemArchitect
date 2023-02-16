#!/usr/bin/python

#########################
#Author: Jessica Freeze
#Last Edited 02/10/23
#The purpose of this script is to predict output based on a the coefficients of a trained linear model and new input features.
########################

import numpy as np

#Request User input?
coefname=input("What is the name of the trained coefficients file?")
predsetinname=input("What is the name of the input features file?")
predsetoutname=input("What is the name of the ground truth output file you'd like to compare predictions to?")
outfile=input("What is the name of the file to save predictions in?")

#Remove ID's If ID's not in first column, comment out or change.
predsetin=predsetin[:,1:]

#If you have multiple output values, select one column.
outval=37

#Select the output value
predsetoutval=predsetout[:,outval]

#Make an array to hold the predicted output
outpred=np.zeros(int(predsetoutval.size))

#Set the index counter
count=0

#For each datapoint in the input
for i in predsetin:
	#Multiply the coefficients with the input features
	multset=np.multiply(coefs,i)
	#Sum the multiplied terms across all coefficients.
	outpred[count]=np.sum(multset)

	#Update the index.
	count=count+1

#Append the actual and predicted output values
printset=np.append(np.reshape(outpred,(outpred.size,1)),np.reshape(predsetoutval,(predsetoutval.size,1)),1)
#Save the predicted and actual output values to a file.
np.savetxt(outfile,printset,delimiter=",")

