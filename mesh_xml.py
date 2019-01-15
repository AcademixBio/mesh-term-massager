import xml.etree.cElementTree as ET
import csv
import sys

#Python script to perform xml parsing of the MESH headings

# if(!(len(sys.argv) > 1)):
#     print("please select an option from: [option1, option2, option3]")
#     exit()
# else:

#Csv file for the output
csv_diseases = open("mesh_records.csv","w", newline ='')
csv_diseases_writer = csv.writer(csv_diseases, delimiter =",")
csv_diseases_writer.writerow(["DescriptorUI", "UIstring", "TreeNumbers", "TreeString"])

#iterate through the entire xml tree tag by tag
for event, elem in ET.iterparse("desc2019.xml"):
    treenumbers = []
    id = ""
    match = False
    idString = ""
    termStrings = []

    #If the tag is DescriptorRecord it means the parsing reached a new heading.
    if(elem.tag =="DescriptorRecord"):
        id = elem.find("DescriptorUI").text
        idString = elem.find("DescriptorName").find("String").text
        #Find the treenumbers inside the treenumberlist, if they start with C it means they represent a disease and match is set true.
        if(elem.find("TreeNumberList") != None):
            for number in elem.find("TreeNumberList"):
                if(number.text[0] == 'C'):
                    treenumbers.append(number.text)
                    match = True
    #if(match) = if the descriptorrecord was of a disease
    if(match):
        conceptlist = elem.find("ConceptList")
        for item in conceptlist.iter():
            #iterate through the concept list and find the terms that match those described by the mesh website
            if(item.tag == "Term" and item.get("RecordPreferredTermYN") == 'N' and item.get("IsPermutedTermYN") == 'N'):
                termStrings.append(item.find("String").text)

        csv_diseases_writer.writerow([id, idString, treenumbers, termStrings])
