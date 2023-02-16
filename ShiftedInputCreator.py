#!/usr/bin/python

#########################
#Author: Jessica Freeze
#Last Edited 02/9/23
#The purpose of this script is to generate files with randomly shifted cartesian coordinates from provided cartesian coordinates. 
#This is particularly useful for making non-ground state species.
########################

import os
import numpy as np
import random

#Collect User values. Can be hardcoded by commenting and adding desired values to these variables.
extension=input("What extension of files are you trying to update? (.gjf or .com)")
IDnumber=input("What index of the filename should be used as the file identifier?")
fname=input("What additional identifier would you like to include in your filenames?")
charge = int(input("What is the desired charge? "))
multiplicity = int(input("What is the desired multiplicity? "))
shift=int(input("What percentage of atoms in the molecules would you like to shift? (Ex: 30% = 30)"))
sz=float(input("What is the greatest positive change in angstroms you would like an atom to move?"))

#Makes a list of all files in the current directory
allfile=[fle for fle in os.listdir('.') if os.path.isfile(fle)]

#Runs over the names of all files in the directory
for file in allfile:
	#Grab the input files with user given extension
	if file.endswith(extension):
		#open the currently selected input file
		f = open(file,'r+')
		#Extract the fileID from the filename
		fileid=(file.split("_")[int(IDnumber)])[:-4]
		#Make the new filename
		chgmultfilename=str(fname)+str(fileid)+str(extension)
		###Read in all lines and then remove the route card, comment, and charge/multiplicity
		data = f.readlines()
		atmcrd=data[5:]
		#cleans out blank spaces
		atmcrd = [x for x in atmcrd if ((x != '\n'))]
		count=0
		#Go over each atm
		for i in atmcrd:
			#Split the line on whitespace
			atmcenter=i.split()
			#Make random number for cartesian coordinate shift choice.
			rnd=random.random()
			#Make random number for negative or positive shifting choice.
			rnd1=random.random()
			#Make random number for atom shift choice.
			chance=int(100/shift)
			rndyesno=random.randint(0,chance)
			#Amount the atom is shifted by in angstroms
			rnd2=random.randint(0,int(sz*100))/100.0
			
			#Choose if the atom will be shifted
			if rndyesno==0:
				#Choose which cartesian coordinate will be changed. Currently only
				#one of the cartesian coordinates may be shifted at a time per atom.
				#X coordinate
				if rnd<0.33:
					#Choose if the shift will occur in a positive or negative way?
					if rnd1<0.5:
						atmcenter[1]=float(atmcenter[1])+rnd2
					else:
						atmcenter[1]=float(atmcenter[1])-rnd2
				#Y coordinate
				elif rnd>0.33 and rnd<0.66:
					if rnd1<0.5:
						atmcenter[2]=float(atmcenter[2])+rnd2
					else:
						atmcenter[2]=float(atmcenter[2])-rnd2
				#Z coordinate
				else:
					if rnd1<0.5:
						atmcenter[3]=float(atmcenter[3])+rnd2
					else:
						atmcenter[3]=float(atmcenter[3])-rnd2
			
			#Write the new cartesian coordinates generated from shifting
			data[count+5]="%s    %.5f    %.5f    %.5f \n" % (str(atmcenter[0]),float(atmcenter[1]),float(atmcenter[2]),float(atmcenter[3]))
			count=count+1
		#Update any route card information manually HERE.
		data[0] = "%%mem=40gb\n%%nprocshared=12\n#p freq wb97xd dgdzvp int=ultrafine scrf=(smd,solvent=tetrahydrofuran) scf=(xqc,maxconventionalcycles=120,verytight) \n"
		data[1] = "\n"
		data[2] = "optimization freq test for %s charge= %d mult= %d mixed basis very tight conv\n" % (file,charge,multiplicity)
		data[3]="\n"
		data[4] = "%d %d\n" % (charge, multiplicity)
		
		#Open new file
		gfile=open(chgmultfilename,'w') 
		#write all route card and title data to file
		gfile.writelines(data)
		#Add necessary blank lines.
		gfile.write('\n\n')
		#Close file
		gfile.close()


		
