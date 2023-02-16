#!/usr/bin/python

#########################
#Author: Jessica Freeze
#Last Edited 02/09/2023
#The purpose of this script is to generate all possible permutations of ligands on a given molecular skeleton using 
# Hammett parameters as identifiers to be used in structure generation.
########################

import itertools

def main():
	
	#Example input, Hammett sigma_meta (mterms) and sigma_para (pterms)
	#pterms = [-0.27,0,-0.83,0,0.23,0.23,0.18,-0.17,-0.15,-0.61,0.03,-0.72,0.13,-0.7,0.06,-0.37]
	#mterms = [0.12,0.15,-0.16,0,0.37,0.39,0.35,-0.07,-0.07,-0.24,0.18,-0.23,0.1,-0.21,0.03,0.12]

	#Number of unique substitution points
	#numsub=5
	
	#Number of supplied Hammett Parameters you'd like to use.
	#end=5
	

	#User input for Hammett Parameters, # substitutions, and how many HP's to use. 
	mterms = input("Enter the meta Hammet Parameters in the required format: ")
	if not (mterms.startswith('[') and mterms.endswith(']') and (',' in mterms)):
		raise Exception('meta Hammett Parameters must follow the correct format. Correct format: "[param_value,param_value,...,param_value]"')
	mterms = mterms.split(',')
	pterms = input("Enter the para Hammet Parameters in the required format: ")
	if not (pterms.startswith('[') and pterms.endswith(']') and (',' in pterms)):
		raise Exception('para Hammett Parameters must follow the correct format. Correct format: "[param_value,param_value,...,param_value]"')
	pterms = pterms.split(',')
	numsub = int(input("How many unique substitution points do you want? "))
	end = int(input("How many of your supplied Hammett Parameters would you like to use? "))
	
	count=0

	##Generate every combination of Hammett Parameter at each substitution spot.
	#counts is an array of length numsub with the value end in each position.
	counts = [end]*numsub
	#Creates subarrays of ranges that can be iterated over to make all permutations.
	ranges=[range(x) for x in counts]
	#For loop generates every iteration of the desired indexes.
	for i in itertools.product(*ranges):
		m = [] #Initializing term selector
		stri = '' #Initializing string length maker

		#Based off the current i permutation select corresponding m and p terms and add them to the current term selector
		for j in range(0,len(i)):
			#Add sigma_m and sigma_p terms to term selector
			m.extend([mterms[i[j]],pterms[i[j]]])
			#Add string formatting terms
			stri=stri+'%s,%s,'

		#After all values have been added to the string add end of line terminators
		stri=stri+'%d\r\n'

		#Add the Molecule ID
		m.extend([count])

		#limit the number of molecules per file to make quicker/easier on memory openable files.
		if (count%999999)==0:
			#determine which number file this is
			n=int(count/999999)
			#write the filename
			name="inpparams_"+str(n)+".csv"
			#if this isn't the first file, close the file
			if n > 0:
				f.close()
			#open the new file
			f=open(name,'w+')
		f.write(stri % tuple(m))
		count=count+1
	
	f.close()
	print(n)
	output=[n,mterms,pterms,numsub,end]
	return output

if __name__ == "__main__":
    main()