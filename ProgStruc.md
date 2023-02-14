#This section details the structure of all files currently in the ChemArchItect package.
  
#Making Many Gaussian Input Files From a List of SMILES.

  #Order of Operations
    #SmileToMol.py (SmileTo Mol_tester.txt for testing example)
    #Use open babel to convert .mol files to .gjf
    #FileCreator.py
    
  #Related Utilities
  
    #Select a random subset of smiles from the list you have
        #RandInputSelect.py
        
    #Make train and test set files from a single dataset
        #Separate_Train_Test.py
        
    #Change the Route Card details for already made Gaussian input files
        #BasisChanger_FileCreator.py
        
    #Create files with shifted atomic cartesian coordinates from existing atomic coordinates
        #ShiftedInputCreator.py

#Utilities to Speed Up Gaussian Job Submission and Fixing

    #Make new input files for files that underwent a TIMEOUT failure.
        #TimeOutRestarter.py
        
    #Make new input files for files that failed due to a bad angle.
        #AngleRestarter.py

#Making Input for Machine Learning

  #Making Encoding Dictionaries For Machine Learning Input
  ##Encoding Dictionaries detail what each feature column refers to.
  
    #Spherical Radii Dictionary
    #DictionaryMaker_SR.py
  
    #Diherdral Arcs Dictionary
    #DictionaryMaker_DA.py
    
    #Angular Arcs Dictionary
    #DictionaryMaker_AA.py
    
  #Extracting Encoded Interactions for Machine Learning Input
 
    #ExtractInteractions.py
    
  #Extraction of Energies and Computed Properties
  
    #ExtractEnergies.py
    #ExtractBondOrder.py
    #ExtractProperties.py

#Analysis Tools for Already Trained Models

    #Predict the energies for a new dataset on a trained model
        #Predictor.py
