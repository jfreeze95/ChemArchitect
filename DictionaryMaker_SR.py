#!/usr/bin/python

#########################
#Author: Jessica Freeze
#Last Edited 02/9/23
#The purpose of this script is to make dictionaries with spherical radii names
########################

import numpy as np
import csv

#Set the array of elements you wish to include
#a=["H","B","C","N","O","F","Si","S","Cl","Br","I"]
a=["H","C","N","O","F"]

name=input("What would you like the dictionary to be named? (please include extension .csv)")
#Get number of elements
lena=len(a)
#Get granularity of dictionary (start,end,step)
rang=np.arange(0.5,8.5,0.5)#[1,1.5,2,2.5,3,3.5,4,4.5,5]
#Make an array of the correct length to hold the dictionary.
dicty=[None]*((len(a)**2)*len(rang))

#Set count for indexing to 0
count=0

#For each element
for i in range(0,lena):
	#For each element that hasn't had a duplicate flipped dictionary entry
	for j in range(i,lena):
		#For each granularity value
		for k in range(0,len(rang)):
			#Make the dictionary name
			dictent=a[i]+"-"+a[j]+"-"+str(round(rang[k],2))
			#Add the dictionary name to the dictionary
			dicty[count]=str(dictent)
			#Update the index
			count=count+1

			
with open(name, 'w') as f:
    csv.writer(f).writerows([dicty])


		