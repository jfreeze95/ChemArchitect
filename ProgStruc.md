<h1>Program Structure</h1>

<h2>Description: This section details the structure of all files currently in the ChemArchItect package.</h2>
  
<h3>Making Many Gaussian Input Files From a List of SMILES.</h3>

<h4>Order of Operations</h4>

1. SmileToMol.py (SmileTo Mol_tester.txt for testing example)
    
2. Use open babel to convert .mol files to .gjf
    
3. FileCreator.py
    
<h4>Related Utilities</h4>
<h5>Select a random subset of smiles from the list you have</h5>
RandInputSelect.py
        
<h5>Make train and test set files from a single dataset</h5>
Separate_Train_Test.py
        
<h5>Change the Route Card details for already made Gaussian input files</h5>
BasisChanger_FileCreator.py
        
<h5>Create files with shifted atomic cartesian coordinates from existing atomic coordinates</h5>
ShiftedInputCreator.py

<h3>Utilities to Speed Up Gaussian Job Submission and Fixing</h3>
<h4>Make new input files for files that underwent a TIMEOUT failure.</h4>
TimeOutRestarter.py
        
<h4>Make new input files for files that failed due to a bad angle.</h4>
AngleRestarter.py</h4>

<h3>Making Input for Machine Learning</h3>

<h4>Making Encoding Dictionaries For Machine Learning Input</h4>
<h5>Encoding Dictionaries detail what each feature column refers to.<\h5>
  
<h5>Spherical Radii Dictionary</h5>
DictionaryMaker_SR.py
  
<h5>Diherdral Arcs Dictionary</h5>
DictionaryMaker_DA.py
    
<h5>Angular Arcs Dictionary</h5>
DictionaryMaker_AA.py
    
<h4>Extracting Encoded Interactions for Machine Learning Input</h4>
ExtractInteractions.py
    
<h4>Extraction of Energies and Computed Properties</h4>
ExtractEnergies.py
ExtractBondOrder.py
ExtractProperties.py

<h3>Analysis Tools for Already Trained Models</h3>

<h4>Predict the energies for a new dataset on a trained model</h4>
Predictor.py
