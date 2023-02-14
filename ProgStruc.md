<h1>Program Structure</h1>

<h2>Description: This section details the structure of all files currently in the ChemArchItect package.</h2>
  
<h3>Making Many Gaussian Input Files From a List of SMILES.</h3>

  <h4>Order of Operations</h4>
    #SmileToMol.py (SmileTo Mol_tester.txt for testing example)
    #Use open babel to convert .mol files to .gjf
    #FileCreator.py
    
  <h4>Related Utilities</h4>
  
    <h5>Select a random subset of smiles from the list you have
        RandInputSelect.py
        
    Make train and test set files from a single dataset
        #Separate_Train_Test.py
        
    Change the Route Card details for already made Gaussian input files
        #BasisChanger_FileCreator.py
        
    Create files with shifted atomic cartesian coordinates from existing atomic coordinates
        #ShiftedInputCreator.py</h5>

<h3>Utilities to Speed Up Gaussian Job Submission and Fixing</h3>

    <h4>Make new input files for files that underwent a TIMEOUT failure.
        #TimeOutRestarter.py
        
    Make new input files for files that failed due to a bad angle.
        #AngleRestarter.py</h4>

<h3>Making Input for Machine Learning</h3>

  <h4>Making Encoding Dictionaries For Machine Learning Input</h4>
    <h5>Encoding Dictionaries detail what each feature column refers to.
  
    Spherical Radii Dictionary
    #DictionaryMaker_SR.py
  
    #Diherdral Arcs Dictionary
    #DictionaryMaker_DA.py
    
    #Angular Arcs Dictionary
    #DictionaryMaker_AA.py</h5>
    
  <h4>Extracting Encoded Interactions for Machine Learning Input</h4>
 
    <h5>ExtractInteractions.py</h5>
    
  <h4>Extraction of Energies and Computed Properties</h4>
  
    <h5>ExtractEnergies.py
    ExtractBondOrder.py
    ExtractProperties.py</h5>

<h3>Analysis Tools for Already Trained Models</h3>

    <h4>Predict the energies for a new dataset on a trained model
        Predictor.py</h4>
