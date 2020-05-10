"""
Mesh Term Massager 
By Academix.bio
"""
import pandas as pd
import xml.etree.cElementTree as ET
from tqdm import tqdm

class MeshTermMassager:
        """
        Parser for the NCBI mesh term XML file
        Parameters:
                MESH_XML_PATH(str): the path of the XML file
        """
        def __init__(self, MESH_XML_PATH: str, take_permutated=False ):
                self.MESH_XML_PATH=MESH_XML_PATH
                self.processed_df=pd.DataFrame()
                self.df_cols = ["Unique_ID", "MeSH_heading", "tree_num", "term_concepts", "entry_terms"]
                self.take_permutated=take_permutated # Should the parser take all permutations of a term
                
        def parse_terms(self):
                """
                Parse XML file 
                """
                print("Parsing XML...")
                rows=[]
                for event, elem in tqdm(ET.iterparse(self.MESH_XML_PATH)): 
                        id = ""
                        idString = ""
                        treenumbers = []
                        conceptStrings = []  
                        termStrings = []
                        match = False
                        if(elem.tag == "DescriptorRecord"): #Broad Categorical Number (ex: "1")
                                id = elem.find("DescriptorUI").text #Descriptor UniqueID (ex: "D001932")
                                idString = elem.find("DescriptorName").find("String").text #(ex: "Brain Neoplasms")
                                if(elem.find("TreeNumberList") != None): #varify the tree in there
                                        for number in elem.find("TreeNumberList"): #List of Pathways to this Descriptor
                                                if(number.text[0] ): 
                                                        treenumbers.append(number.text) #(ex: 'C04.588.614.250.195')
                                                        match = True 
                                if(match): 
                                        for concept in elem.find("ConceptList"): #Related Concepts
                                                if(concept.tag == "Concept"):
                                                        conceptStrings.append(concept.find("ConceptName").find("String").text) 
                                                        for term in concept.find("TermList"):
                                                                if(term.tag == "Term"):
                                                                        if(self.take_permutated):
                                                                                termStrings.append(term.find("String").text)
                                                                        elif(term.attrib["IsPermutedTermYN"] == "N" and term.attrib["RecordPreferredTermYN"] == "N"):
                                                                                termStrings.append(term.find("String").text)
                                                        
                                        rows.append({"Unique_ID": id, "MeSH_heading": idString, "tree_num": treenumbers, "term_concepts": conceptStrings, "entry_terms": termStrings})
                print("Parsing complete! {} records detected".format(len(rows)))                        
                self.processed_df = pd.DataFrame(rows, columns = self.df_cols)

        def get_processed_df(self) -> pd.DataFrame:
                """
                Return the processed dataframe
                """
                return self.processed_df

        def save_json(self):
                """
                Export the processed data to json
                """
                self.processed_df.to_json('mesh_data.json',orient='records')
                print("Data saved to json")
                pass



