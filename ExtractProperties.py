##########
#Current script for extracting properties from gaussian log files, formatting them, and putting them into rows for ML.
#May 20, 2020
#Latest Author: Jessica Freeze
##########

import ahocorasick
from math import sqrt
import os
import re

#Atom number that you want the mulliken charge from
atmnum=5
#Atom numbers for bond distance determination
atm1=1
atm2=2

#Checker for if an SCF Done line has been found yet
scfcheck=0

#outer loop for multiple files
for i in os.listdir('.'):
	#if the file is an output file
	if i.endswith('.log'):

		#Open the log file for reading
		with open(i,'r') as f:
			#Print the filename for progress reporting
			print(i)
			#Read the file into memory
			listStrings = f.readlines()

		#List of substrings that will be used to find sections in the file
		listSubstrings = ["NAtoms=","Charge =","SCF Done:","Mulliken charges:","Thermal correction to Energy=","Thermal correction to Enthalpy=","Thermal correction to Gibbs Free Energy=","CV","Zero-point correction=","Coordinates (Angstroms)","occ. eigenvalues --","virt. eigenvalues --","Dipole moment (field-independent basis, Debye):","Maximum Force"]

		#Make an iteration automaton
		auto = ahocorasick.Automaton()
		#Run over each section substring
		for substr in listSubstrings:
			#Add all occurrences of substring
			auto.add_word(substr, substr)
		#Make the automaton
		auto.make_automaton()

		#Make a set of seen instances
		seen = set()
		#length of file
		ct = len(listStrings)

		#Request an output filename and open that file
		propname=input("What filename would you like for the output file?")
		w = open(propname,"a+")

		#Extracting id's from filenames with restarted files handled, Hardcode needs to be adjusted based on user filenames
		id0=re.search('(?<=chg_pos_0_mult_1_dgdzvp_)[\d]+(?=_\dr\.log)',i)
		id1=re.search('(?<=chg_pos_0_mult_1_dgdzvp_)[\d]+(?=\.log)',i)

		#Check the fileID and write it as the first column entry
		if id0:
			w.write(id0.group(0)+",")
		elif id1:
			w.write(id1.group(0)+",")
		else:
			w.write(i+",")

		#Read the file backwards string by string
		for astr in reversed(listStrings):
			#Run over found cases
			for end_ind, found in auto.iter(astr):
				#If SCF not yet found update the checker
				if found not in seen and found=="SCF Done":
					scfcheck=1
				#If not found yet and not keyword add to the seen 
				elif found not in seen:
					scfcheck=0
					seen.add(found)
					if found == "Mulliken charges:":
						#mulliken charge collector on user specified atom number
						mulliken = listStrings[ct+atmnum].split()[2]
						w.write(mulliken+",")
					elif found == "NAtoms=":
						#Number of atoms finder
						numatoms=listStrings[ct-1].split()[1]
						w.write(numatoms+",")
					elif found == "SCF Done:":
						#SCF energy finder
						scfE = listStrings[ct-1].split()[4]
						w.write(scfE+",")
					elif found == "Thermal correction to Energy=":
						#Thermal correction to Energy finder
						themcorE = listStrings[ct-1].split()[4]
						w.write(themcorE+",")
					elif found == "Thermal correction to Enthalpy=":
						#Thermal correction to Enthalpy finder
						themcorH = listStrings[ct-1].split()[4]
						w.write(themcorH+",")
					elif found == "Thermal correction to Gibbs Free Energy=":
						#Thermal correction to Gibbs Free Energy finder
						themcorG = listStrings[ct-1].split()[6]
						w.write(themcorG+",")
					elif found == "Zero-point correction=":
						#Zero-point correction finder
						zeroptcor = listStrings[ct-1].split()[2]
						w.write(zeroptcor+",")
					elif found == "CV":
						#Extract all Specific heat at constant volume, internal energy, and entropy values
						totalE = listStrings[ct+1].split()[1]
						w.write(totalE+",")
						totalCV = listStrings[ct+1].split()[2]
						w.write(totalCV+",")
						totalS = listStrings[ct+1].split()[3]
						w.write(totalS+",")
						ElecE = listStrings[ct+2].split()[1]
						w.write(ElecE+",")
						ElecCV = listStrings[ct+2].split()[2]
						w.write(ElecCV+",")
						ElecS = listStrings[ct+2].split()[3]
						w.write(ElecS+",")
						TransE = listStrings[ct+3].split()[1]
						w.write(TransE+",")
						TransCV = listStrings[ct+3].split()[2]
						w.write(TransCV+",")
						TransS = listStrings[ct+3].split()[3]
						w.write(TransS+",")
						RotE = listStrings[ct+4].split()[1]
						w.write(RotE+",")
						RotCV = listStrings[ct+4].split()[2]
						w.write(RotCV+",")
						RotS = listStrings[ct+4].split()[3]
						w.write(RotS+",")
						VibE = listStrings[ct+5].split()[1]
						w.write(VibE+",")
						VibCV = listStrings[ct+5].split()[2]
						w.write(VibCV+",")
						VibS = listStrings[ct+5].split()[3]
						w.write(VibS+",")
					elif found == "Coordinates (Angstroms)":
						#Specific bond length calculation numbers
						x1 = listStrings[ct+atm1+1].split()[3]
						w.write(x1+",")
						y1 = listStrings[ct+atm1+1].split()[4]
						w.write(y1+",")
						z1 = listStrings[ct+atm1+1].split()[5]
						w.write(z1+",")
						x2 = listStrings[ct+atm2+1].split()[3]
						w.write(x2+",")
						y2 = listStrings[ct+atm2+1].split()[4]
						w.write(y2+",")
						z2 = listStrings[ct+atm2+1].split()[5]
						w.write(z2+",")
						#calculate bond distance
						bnddist=sqrt((float(x1)-float(x2))**2+(float(y1)-float(y2))**2+(float(y1)-float(y2))**2)
						w.write(str(bnddist)+",")
					elif found == "occ. eigenvalues --":
						#Find HOMO and LUMO energies
						HOMO = listStrings[ct-1].split()[-1]
						LUMO = listStrings[ct].split()[4]
						w.write(HOMO+",")
						w.write(LUMO+",")

					elif found == "Dipole moment (field-independent basis, Debye):":
						#Find dipoles
						dipoleX = listStrings[ct].split()[1]
						w.write(dipoleX+",")
						dipoleY = listStrings[ct].split()[3]
						w.write(dipoleY+",")
						dipoleZ = listStrings[ct].split()[5]
						w.write(dipoleZ+",")
						dipoleTot = listStrings[ct].split()[7]
						w.write(dipoleTot+",")
					elif found == "Maximum Force":
						#Check if all forces are converged or not
						countyes=0
						print(listStrings[ct-1])
						maxfrc = listStrings[ct-1].split()[4]
						rmsfrc = listStrings[ct].split()[4]
						maxdisp = listStrings[ct+1].split()[4]
						rmsdisp = listStrings[ct+2].split()[4]
						if maxfrc=="YES" and rmsfrc=="YES" and maxdisp=="YES" and rmsdisp=="YES":
							w.write("YES,")
						else:
							w.write("NO,")

					

			#Update the line number
			ct=ct-1

		#Calculate the HOMO-LUMO gap
		HLGap = float(HOMO)-float(LUMO)
		w.write(str(HLGap)+"\n")
		#Close File
		w.close()

