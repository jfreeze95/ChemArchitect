#!/usr/bin/python

#########################
#Author: Jessica Freeze
#Last Edited 02/9/23
#The purpose of this script is to convert gjf files outputted from ibabel to gjf files ready for submission
# ---Includes taking mol geometry instead of gjf geom
#This file should be run after generating .gjf or .com files from .mol files using oBabel.
#This should be run in the same directory as the .gjf and .mol files
########################

import os
import FileCreatorConfig

def main():

	#Collect User input for job specifications?
	charge = int(input("What is the desired charge? "))
	#Hard code option
	#charge=0
	multiplicity = int(input("What is the desired multiplicity? "))
	#Hard code option
	#multiplicity=1
	filedescript = input("Type any additional file descriptor to be included in the file name now and press enter or simply press enter for no descriptor: ")
	fileextension=input("What is your file extension you would like for input? (Ex: .gjf)")
	IDnumber=input("What index of the filename should be used as the file identifier?")

	#To grab every file in a directory
	allfile=[fle for fle in os.listdir('.') if os.path.isfile(fle)]
	
	#iterate over every file in the directory
	for file in allfile:

		#checkes for files with desired ending
		if file.endswith(fileextension):
			
			#Creates string with user specifications
			if charge >= 0:
				chgmultfile = "chg_pos_%d_mult_%d_%s_%s" % (abs(charge),multiplicity,filedescript,file)
			else:
				chgmultfile = "chg_neg_%d_mult_%d_%s_%s" % (abs(charge),multiplicity,filedescript,file)
			
			#renames file with user specifications
			os.rename(file,chgmultfile)

			#opens file with desired ending and reads the entire file into data
			print("Warning: Next step requires input file to be read into memory. If you experience problems with this step, contact developers.")
			print(chgmultfile)
			f = open(chgmultfile,'r+')
			data = f.readlines()
			#close file to save memory space and avoid future opening problems
			f.close()
			#Makes variable with filename and no extension for use in input file. Note quotes used to avoid problems with weird characters
			fileid=(file.split("_")[int(IDnumber)])
			#Sets variable ext to index of extension so that extension can be removed
			ext = fileid.find(fileextension)
			filename = "%s" % (fileid[:ext])

			#gets chkpoint filename base
			ext = chgmultfile.find(fileextension)
			chgmultfilename = "%s" % (chgmultfile[:ext])
			
			#Sets first 4 lines of input file to the desired values (route card, blank line,title, blank line)
			data[0] = "%%mem=40gb\n%%nprocshared=12\n%%chk=%s.chk\n#p opt=maxstep=20 freq wb97xd dgdzvp int=ultrafine scrf=(smd,solvent=tetrahydrofuran) scf=(xqc,maxconventionalcycles=120,verytight) \n" % chgmultfilename
			data[1] = "\n"
			data[2] = "optimization freq test for %s charge= %d mult= %d mixed basis very tight conv\n" % (file,charge,multiplicity)
			data[3]="\n"
			data[4] = "%d %d\n" % (charge, multiplicity) # adjust to change metal oxidation
			
			#name filename with mol extension for opening mol file with same name as input file
			filename = "%s.mol" % filename


			with open(filename,'r') as f:
				#read through the first 4 lines of mol file then grab number of atoms so that number of atom specification lines can be skipped
				for i in range(0,4):
					line = f.readline()
				tst = line[0]+line[1]+line[2]
				atmcoord=[None]*int(tst)
				#skipping atom specification lines
				for i in range(0,(int(tst))):
					line = f.readline()
					line = line.split()
					
					data[i+5] = "%s    %.5f    %.5f    %.5f \n" % (line[3],float(line[0]),float(line[1]),float(line[2]))
				
				#Read rest fo file in variable lines
				lines = f.readlines()

			#remove unneeded 3 lines at bottom
			lines = lines[0:(len(lines)-3)]

			#open gaussian input file in overwrite mode
			gfile=open(chgmultfile,'w') 
			#write all route card and title data to file
			gfile.writelines(data)


			#Write pseudopotentials if desired. Additional atoms types and basis sets can easily be added by copying the below lines
			#and adding the new elements and basese.
			#Add blank line to separate atom coords from pseudo
			# gfile.write('\n')
			# gfile.write("-H 0\n6-31g\n****\n-C 0\n6-31g\n****\n-N 0\n6-31g(d)\n****\n-O 0\n6-31g(d)\n****\nRu 0\nlanl2dz\n****\n")
			# if any("Cl" in s for s in data):
			# 	gfile.write("Cl 0\n6-31g(d)\n****\n")
			# if any("S" in s for s in data):
			# 	gfile.write("S 0\n6-31g(d)\n****\n")
			# if any("P" in s for s in data):
			# 	gfile.write("P 0\n6-31g(d)\n****\n")
			# if any("Br" in s for s in data):
			# 	gfile.write("Br 0\n6-31g(d)\n****\n")
			# if any("I" in s for s in data):
			# 	gfile.write("I 0\n6-31g(d,p)\n****\n")
			# gfile.write("\nRu 0\nlanl2dz\n\n\n\n\n")

			# gfile.write("-C 0\ndgtzvp\n****\n")
			# if any("N" in s for s in data):
			# 	gfile.write("N 0\ndgtzvp\n****\n")
			# if any("H" in s for s in data):
			# 	gfile.write("H 0\ndgtzvp\n****\n")
			# if any("Si" in s for s in data):
			# 	gfile.write("Si 0\ndgtzvp\n****\n")
			# if any("O" in s for s in data):
			# 	gfile.write("O 0\ndgtzvp\n****\n")
			# if any("Cl" in s for s in data):
			# 	gfile.write("Cl 0\ndgtzvp\n****\n")
			# if any("F" in s for s in data):
			# 	gfile.write("F 0\ndgtzvp\n****\n")
			# if any("S " in s for s in data):
			# 	gfile.write("S 0\ndgtzvp\n****\n")
			# if any("Br" in s for s in data):
			# 	gfile.write("Br 0\ndgdzvp\n****\n")
			# if any("B " in s for s in data):
			# 	gfile.write("B 0\ndgdzvp\n****\n")
			# if any("I" in s for s in data):
			# 	gfile.write("I 0\ndgdzvp\n****\n")


			#Add necessary ending blank lines
			gfile.write('\n\n')
			#Close file
			gfile.close()

if __name__ == "__main__":
    main()	
