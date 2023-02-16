#!/usr/bin/python

#########################
#Author: Jessica Freeze
#Last Edited 2/9/23
#The purpose of this script is to convert a list of smiles strings given in the first column of a file
#into mol files with names as given in the second column.
########################
from rdkit import Chem
from rdkit.Chem import AllChem


def main():
	#Collecting user input
	count=input("Enter the number of smiles you wish to convert: ")
	inputfile = input("Enter the name of your .txt file with extension: ")

	#Opening user's list of smiles file
	f = open(inputfile,'r')

	print("Preparing to convert all selected SMILES strings to mol formatted files")
	
	#trigger for alerting user of size allocation and keep track of going over user's desired number of files
	num = 0
	#Trigger for if the file did not correctly convert to 3D
	chk = 0
	#Run over each SMILES string in the file
	for line in f:
		#Check if we have surpassed the user's desired amount
		if num<=int(count):
			#Remove newline characters
			line = line.strip()
			#split the line into SMILES and ID
			line = line.split()
			#While the file correctly converted to 3D
			while chk == 0:
				#Convert the SMILES to mol format
				filename = convert(line,num,count)
				#print filename to show progress
				print(filename)
				#check if 3D operation was successful
				chk = check2D(filename,chk)
			#update so we no longer inform about space allocation
			num += 1
			#reset 3D checker for next molecule
			chk = 0
	
	#Close file	
	f.close()

#######################################	
#check for 2D bug
def check2D(filename,chk):
	#open last converted file
	file=open(filename,'r')
	#read unneeded lines and trash
	for i in range(0,4):
		file.readline()
	#set constants for number of atoms and number of atoms using a 2D format
	numatoms = 0
	num2D = 0
	#read in the first line of atom specification
	l = file.readline()
	l=l.split()
	#while loop over all lines of file with atom coordinates (all such lines will have length=16 per the format)
	while len(l)==16:
		#for each atom add 1
		numatoms += 1
		#check for 2D coordinates
		if l[2] == "0.0000":
			#if 2D add 1
			num2D += 1
		#read next line
		l=file.readline()
		l=l.split()

	#If more than half of the atoms are not in the same plane then the molecule is not 2D
	if (num2D/float(numatoms))<=0.5:
		chk=1
	else:
		print("2D bug found, please resubmit this file.")
	return chk

#####################################
#Convert the smiles to a mol format and adjust it to the correct mol format
#####################################
def convert(line,num,count):
	#Takes in the smiles string and returns a mol object
	mol = Chem.MolFromSmiles(line[0])

	#Gets the index of the last atom
	for atom in mol.GetAtoms():
		max =atom.GetIdx()

	#Adds hydrogens only to atoms in the onlyOnAtoms keyword give user ability to specify atoms they don't want to have hydrogens added
	#Default value is set to put on all atoms that need hydrogens to fill the valence.
	mol_h=Chem.AddHs(mol,onlyOnAtoms=range(0,(max+1)))
	
	#Gives the molecule 3D coordinates
	Chem.AllChem.EmbedMolecule(mol_h)
	#Takes the name you gave to that smiles string from the second column of the file and makes the mol filename
	filename = line[1]+".mol" 

	#Create the typical mol format block for a text file
	block = Chem.MolToMolBlock(mol_h)

	#Open the new file
	file=open(filename,'w+')
	#Write the molblock to the file
	file.write(block)
	
	if num == 0:
		#file.seek(0,2) gets us the number of characters in the file.
		sz=file.seek(0,2)
		#Informs the user that they are about to take up an amount of space on their computer based on the number of characters in their files and the number of bytes per character.
		input("Your files will take approximately " +str(sz*int(count))+" bytes. Press Enter if you wish to continue.")
	
	#close the input file you just created
	file.close()

	#return the filename of the new mol file you just created.
	return filename

#####################################
if __name__ == "__main__":
    main()	