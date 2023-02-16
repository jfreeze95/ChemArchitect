#!/usr/bin/python

#########################
#Author: Jessica Freeze
#Last Edited 2/10/23
#The purpose of this script is to randomly select a desired amount of structures from the total permutation library
########################

from random import randint

#Initiate the count variable
count = 0

Fullfile=input("What is the name of the .txt file (with extension) that has all of your SMILES structures?")
Newfile=input("What name would you like for the random selection of SMILES structures?")
ratio = int(input("What ratio (Integer X for 1 out of every X) of files would you like selected?"))

#Open the file with all SMILES structures
f = open(Fullfile,'r')

#Open a new file for the random subset of structuresto be saved to.
g = open(Newfile,'w+')

#For each line in your all SMILES file, read the line
for line in f:
	#If you randomly select the value 1 out of the pool of 0 to ratio, accept that line.
	if randint(0,ratio) ==1:
		#write that smiles string to the new file with an additional index for referencing back to the original full file.
		g.write(str(line.strip()) + ' ' + str(count)+'\n') 
	#Add a count value to get new indices
	count +=1

#Close the files.
f.close()
g.close()