#!/usr/bin/python

#########################
#Author: Jessica Freeze
#Last Edited 3/06/19
#The purpose of this script is to create input files for angle problems, also warns about Atoms Too Close Errors so they can be handled manually
#This version handles archives with files from multiple folders
########################

#open log file
#read log file lines
#close log file
#prep filenames
#duplicate .gjf
#open new gjf
#read lines from end, find standard orientation
#Read lines 5 after that on and write to duplicated file at lines of center number
# read while not = -----

from shutil import copyfile
import os


#Collect User desired file identifier
extension=input("What extension of files are you trying to update? (.gjf or .com)")
fileid=input("What is the identicle string in every file's name that we should use to find the filenames? (ex: Name=[Ru])")
extrafront=input("How many extra characters are at the front of the identicle string just provided that are not part of the filename? (ex: Name=[Ru] has six for ' Name=')")

#Get angle failed files and put in formbx.txt
#open archive file from takeout.google.com
arcfile = "FAILED.mbox"
extarc = arcfile.find('.')
arcfile1=arcfile[:extarc] + "angleother.txt" #file with files in other directory
arcfile2=arcfile[:extarc] + "anglerestart.txt" #file with files in this directory, to be used for restart
f=open(arcfile,'r') #should be name of archive
#read in file
lines=f.readlines()
f.close()
#open file to save to
g=open("formbx.txt","w+")
#for every line check that if it contains a filename
for i in range(0,len(lines)):
	lineind= lines[i].find(fileid) 
	if (lineind==1):
		curlineind=lines[i].find('Failed')
		#set curfile to the filename plus Name=
		curfile=lines[i][:(curlineind-1)]
		#Chop off extra characters from filenames
		curfile=curfile[extrafront:] 
		#Add log extension
		filename = curfile+".log"
		#add new line to each file name
		wrline=filename+"\n"
		#write to formbx.txt
		g.write(wrline)
g.close()

#element list
elements=['H','He','Li','Be','B','C','N','O','F','Ne','Na','Mg','Al','Si','P','S','Cl','Ar','K','Ca','Sc','Ti','V','Cr','Mn','Fe','Co','Ni','Cu','Zn','Ga','Ge','As','Se','Br','Kr','Rb','Sr','Y','Zr','Nb','Mo','Tc','Ru','Rh','Pd','Ag','Cd','In','Sn','Sb','Te','I','Xe','Cs','Ba','La','Ce','Pr','Nd','Pm','Sm','Eu','Gd','Tb','Dy','Ho','Er','Tm','Yb','Lu','Hf','Ta','W','Re','Os','Ir','Pt','Au','Hg','Tl','Pb','Bi','Po','At','Rn','Fr','Ra','Ac','Th','Pa','U','Np','Pu','Am','Cm','Bk','Cf','Es','Fm','Md','No','Lr','Rf','Db','Sg','Bh','Hs','Mt','Ds','Rg','Cn','Nh','Fl','Mc','Lv','Ts','Os']

#open file with all files that need to be restarted
f = open("formbx.txt",'r')
#read files into anglefiles
anglefiles = f.readlines()

#for every log file
for i in range(0,len(anglefiles)):
	file=anglefiles[i]
	file=file.strip()
	exists = os.path.isfile(file)
	if exists:
		#open log file
		g=open(file,"r")
		#read log file lines
		loglines = g.readlines()
		#close log file
		g.close()
		#clean lines
		for j in range(0,len(loglines)):
			loglines[j]=(loglines[j]).strip()

		#prep filenames
		ext = (file).find('.log')
		filename = "%s" % (file[:ext])
		filenew="%sfrm" % (file[:ext]) #frm comes from Form BX the error that angle problems gives off
		fileorig = "%s%s" % (filename,extension)
		filenew = "%s%s" % (filenew,extension)
		

		#Find atom specifications
		m=len(loglines)-1
		l = loglines[m]
		#print(str(m) + " " + str(len(loglines)))
		while l !="Standard orientation:":
			l=loglines[m-1]
			m=m-1
			#check that m does not equal -1 because if it does Standard orientation not present
			if m==-1:
				l="Standard orientation:"
				
		#if standard orientation not present end this loop and start on next file
		if (m==-1 and loglines[len(loglines)-4]=="Atoms too close."):
			h=open("atomsTooClose.txt","a+")
			fname=file+"\n"
			h.write(fname)
			h.close()
			continue
		elif m==-1:
			#print file to be dealt with manually
			print(file)
			print("did not write to atomsTooClose.txt. Please check file manually")
			continue

				#save filename to restart list
		h=open(arcfile2,"a+")
		writefile = filenew+"\n"
		h.write(writefile)
		h.close()
		#if standard orientation found, print line it was found at and continue this loop
		print("found it at line " + str(m))
		startind=m+5
		#set index to start of atom specifications
		m=m+5
		#while not at the end of atom specification increase line
		while loglines[m] !="---------------------------------------------------------------------":
			m=m+1
		#having found the end of the atom specification set endind (note set for use in range function)
		endind=m
		
		#duplicate .gjf
		copyfile(fileorig,filenew)
		#open new gjf
		g=open(filenew,"r")
		data=g.readlines()
		g.close()
		#line where atom geom starts
		curlineind=8
		#for each line in atom spec
		for j in range(startind,endind):

			#split line to list
			line=loglines[j].split()
			#print(str(line) +" "+ str(line[1]) +" "+ str(elements[int(line[1])-1]))
			#change atom number to atom two lettter code
			line[1] = elements[int(line[1])-1]
			#make line
			newln = line[1]+"    "+line[3]+"    "+line[4]+"    "+line[5]+"\n"
			#replace old atom coordinates with new atom coords
			data[curlineind]=newln
			#update line to be replaced.
			curlineind=curlineind+1

		#open file and write data with new atom coords to file.
		g=open(filenew,"w+")
		g.writelines(data)
		g.close()
	else:
		g=open(arcfile1,"a+")
		filewrite = file+"\n"
		g.write(filewrite)
		g.close()
f.close()

