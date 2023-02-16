#!/usr/bin/python

#########################
#Author: Jessica Freeze
#Last Edited 3/06/19
#The purpose of this script is to split data into train and test sets.
#If you desire random splits every run of training, use an sklearn or other package. 
#This will make permanent files you can refer back to and analyze.
########################

import random

def seper():

	#Collect user input for full dataset and percentage to be used for training
	TotalFile=input("What is the name of the file you would like split into a train and test set?")
	split=input("What integer percentage of data would you like to be used for training?")

	#Make train and test filenames
	TrainName=str(TotalFile)+"_train.csv"
	TestName=str(TotalFile)+"_test.csv"

	#Open the full dataset file
	f = open(TotalFile,"r")

	#Open new files to store train and test sets
	g=open(TrainName,"w+")
	h=open(TestName,"w+")

	#Make the integer for a random ratio split
	percent=int(100/split)
	
	#For each datapoint in the dataset, determine if it will be added to train or test.
	for line in f:
		if random.randint(0,percent) == 1:
			#Write to train
			g.write(line)

		else:
			#Write to test
			h.write(line)

	#Close files
	f.close()
	g.close()
	h.close()

if __name__ == "__main__":
    seper()