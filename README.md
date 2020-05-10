# mesh-term-massager :massage:
Turn MeSH-terms xml file into tabular format 

Introduction
--
Mesh-term-massager is used to convert MeSH term lists downloaded from [NCBI](https://www.nlm.nih.gov/databases/download/mesh.html) in XML format into a Pandas DataFrame or json format which could be readily used in down-stream applications.

Requirements
--
- Python > 3.5
- MeSH XML file downloaded from NCBI

*Note: code was tested on the 2019, 2020 xml version*


Usage
--
Please see the [attached Jupyter notebook](https://github.com/AcademixBio/mesh-term-massager/blob/master/mesh-term-massager.ipynb) for an example on how to run the parser.

Basix steps:
1. Initiate a new instance of the class `MeshTermMassager` with and include the path to the .xml file downloaded from NCBI
2. Invoke the `parse_terms` function to parse the data
3. Use either the `get_processed_df` or `save_json` to view/export the processed data

Output
--

The out is a DataFrame or json file with the following structure

Unique_ID |	MeSH_heading |	tree_num | term_concepts | entry_terms
-------------|-----------|--------------|------------|------------------
D000001 |	Calcimycin	| [D03.633.100.221.173] |	[Calcimycin, A-23187]	| [A-23187, A23187, Antibiotic A23187]
D000002 |	Temefos	| [D02.705.400.625.800, D02.705.539.345.800, D02... |	[Temefos, Abate, Difos]	| [Temephos, Abate, Difos]
D000003 |	Abattoirs | 	[J01.576.423.200.700.100, J03.540.020] |	[Abattoirs]	| [Slaughter Houses, Slaughter House, Slaughterh...
D000004 |	Abbreviations as Topic |        [L01.559.598.400.556.131]	| [Abbreviations as Topic, Acronyms as Topic] |	[Acronyms as Topic]


