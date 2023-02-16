#!/usr/bin/python

#########################
#Author: Jessica Freeze
#Last Edited 2/25/19
#The purpose of this script is generate rerun scripts for timeout failures when the archive has filenames from multiple folders
#This specifically only works when the Gaussian restart command can be used and you have the original input file.
#If the restart command may not be used, 1) collect the names of logs using this file, 2)extract timed out .log files from
#the cluster, 3) Use openBabel to turn the log files into input files, 4) Use BasisChanger_FileCreator.py to regenerate the route card.
########################

####Summary####
#Grab file names from archive file
#copy gjf file with that name to name + "r"
#Open new gjf file and add restart to opt params in route card, save, close
#add new gjf filename to batch script
#gen new .sh files with mksh.sh script
#run new files from batch script

import numpy as np
from shutil import copyfile
import os


#Prepare array for filenames
files= np.array([])

#Name of mailbox archive file (Toggle these two lines to hardcode or accept user input)
#open archive file from takeout.google.com
arcfile = "TIMEOUT.mbox"
#arcfile =input("What is the name of the mailbox archive file you want to use? (.mbox)")

#Collect User desired file identifier
extension=input("What extension of files are you trying to update? (.gjf or .com)")
fileid=input("What is the identicle string in every file's name that we should use to find the filenames? (ex: Name=[Ru])")
extrafront=input("How many extra characters are at the front of the identicle string just provided that are not part of the filename? (ex: Name=[Ru] has six for ' Name=')")

#Find the index of the period in the mailbox archive filename.
extarc = arcfile.find('.')
#Make filenames
arcfile1=arcfile[:extarc] + "timeoutother.txt" # files located elesewhere that need to be restarted
arcfile2=arcfile[:extarc] + "timeoutrestart.txt" #files located here that will need to be restarted

#Open the mailbox archive file
f=open(arcfile,'r') #should be name of archive

#Read in the mailbox archive file.
lines=f.readlines()

#Close the mailbox archive file
f.close()

#Move over every line of the mailbox archive file, getting the line number
for i in range(0,len(lines)):

	#Finds index of line with filename
	lineind= lines[i].find(fileid) 

	#If the filename is found in the subject line continue
	if (lineind==1):
		#Find the index in the line where the failed message appears
		curlineind=lines[i].find('Failed')

		#Take everything in the line that comes before the status message
		curfile=lines[i][:(curlineind-1)]

		#Chop off extra characters from filenames
		curfile=curfile[extrafront:] 
		#makes fileoutput filename. If filename has a different extension, change .log accordingly
		filechk = curfile+".log"
		#check if file exists in this folder
		exists = os.path.isfile(filechk)
		if exists:
			#Make input filenames, if .gjf is not the extension, change the code here to match your specifications
			filename = curfile+extension
			newflnm = curfile+"r"+extension
			#save filename to restart list
			h=open(arcfile2,"a+")
			writenewflnm = newflnm +"\n"
			h.write(writenewflnm)
			h.close()

			#Specify restart route card details HERE
			newline="# ub3lyp/gen pseudo=read empiricaldispersion=gd3bj int=ultrafine geom=connectivity scf=(xqc,maxconventionalcycles=120,tight) scrf=(smd,solvent=CH3CN) opt=(restart,gdiis,maxstep=20) freq\n"
			
			#Take the old input file and copy to the new input file
			copyfile(filename,newflnm)
			#Open the new input file and extract the file into memory
			g=open(newflnm,"r")
			data=g.readlines()
			#change the saved file to have the new route card
			data[3]=newline
			#close the file
			g.close()
			#reopen the file
			g=open(newflnm,"w+")
			#rewrite the file with the new route card.
			for j in range(0,len(data)):
				g.write(str(data[j]))

			#close the file
			g.close()
		
		#If we can't find this file in the folder we are currently in then add it to a new list that can be addressed after running this script
		else:
			g=open(arcfile1,"a+")
			filewrite = filechk+"\n"
			g.write(filewrite)
			g.close()

