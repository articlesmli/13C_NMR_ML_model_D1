### Using machine learning and 13C NMR spectroscopy data derived by SMILES to predict the influence of nanoformulations on biomolecule functionality. Demonstrative case: Human Dopamine D1 Receptor Antagonists.
- From folder named input run the lists_generatio.ipynb file and you will obtain the smiles.csv and targets.csv files. Provided csv files in the current folders are regarding human dopamine D1 receptor antagonists.
- Creats an empty folder named output. The files in the curent folder output are a part of alredy scraped data regarding the D1 receptor antagonsts.
- Run the files consicunetlly as they are numerated. 2.Web_scraping.ijnb will fill the folder output with text files of the compounds; 2.count.ipynb will generate the csvfile needed for Ml. 
- The last file 7.CID_SID_ML_model_D1.ijynb file is an additional ML model which use the PubChem CID and SID of compound to predict the porbability this compound to be as well a human dopamine D1 receptor antagonist

The raw data used in the porject: 
- PubChem AID 504652 - Antagonist of Human D 1 Dopamine Receptor: qHTS  https://pubchem.ncbi.nlm.nih.gov/bioassay/504652
- PubChem AID 1996 - Aqueous Solubility from MLSMR Stock Solutions https://pubchem.ncbi.nlm.nih.gov/bioassay/1996
 
