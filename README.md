# mesh-term-massager
Turn MeSH-terms xml file into tabular format

Introduction
--
Mesh-term-massager is used to convert MeSH term lists downloaded from [NCBI](https://www.nlm.nih.gov/databases/download/mesh.html) in XML format into CSV tabular format which could be readily used in down-stream applications.

Requirements
--
- Python3
- MeSH XML file downloaded from NCBI

*Note: code was tested on the 2019 xml version, and is currently set only to extract diease terms.*


Usage
--
1. Edit the script to include the path to the .xml file downloaded from NCBI
2. Invoke the command `python mesh_xml.py` 

Output
--

The out is a CSV file with the following structure

DescriptorUI |	UIstring |	TreeNumbers | TreeStrings
-------------|-----------|--------------|------------
D000007 |	Abdominal Injuries |	['C26.017'] |	['Injuries, Abdominal']
D000008 |	Abdominal Neoplasms |	['C04.588.033'] |	[]
D000013 |	Congenital Abnormalities |	['C16.131'] |	['Deformities', 'Congenital Defects', 'Defects, Congenital', 'Abnormalities, Congenital', 'Birth Defects']
D000014 |	Abnormalities, Drug-Induced |	['C16.131.042']	| ['Drug-Induced Abnormalities'] 




