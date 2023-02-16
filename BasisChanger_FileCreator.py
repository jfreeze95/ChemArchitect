#!/usr/bin/python

#########################
#Last Edited 02/10/23
#Last Edited By: Jessica Freeze
#The purpose of this script is to change the route card specifications for an already existing input file.
#This script is best used by hardcoding the data lines.
#.gjf's can also be changed to .com
########################

import os
fileextension=input("What is your file extension you would like for input? (Ex: .gjf)")

#To grab every file in the current directory
for file in os.listdir('.'):
	if file.endswith(fileextension):
		f = open(file,'r')
		data = f.readlines()
		#close file to save memory space and avoid future opening problems
		f.close()
		#gets chkpoint filename base
		ext = file.find(fileextension)
		chgmultfilename = "%s" % (file[:ext])

		#New route card specifications "Data Lines"
		data[0] = "%%mem=40gb\n%%nprocshared=12\n%%chk=%s.chk\n#p opt=maxstep=20 freq wb97xd dgdzvp int=ultrafine scrf=(smd,solvent=tetrahydrofuran) scf=(xqc,maxconventionalcycles=120,verytight) density=current output=wfn fchk=all gfinput pop=full iop(6/80=1) \n" % chgmultfilename
		data[1] = "\n"
		data[2] = "optimization freq test for %s \n" % (file)
		data[3]="\n"
		data[4] ="0 1\n"
		
		#open gaussian input file in overwrite mode
		gfile=open(file,'w') 
		#write all route card and title data to file
		gfile.writelines(data)

		#Example inclusion of post atomic coordinates specifications
		end1 = "%s.wfn" % (file[:ext])
		end2 = "%s.fchk" % (file[:ext])
		end3 ="%s\n\n%s\n\n" %(end1,end2)
		gfile.write(end3)
		
		#Area for pseudopotential specifications
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


		#Add necessary blank lines
		gfile.write('\n\n\n\n')

		#Close file
		gfile.close()