This repository includes:
1) one ontology for nutritional epidemiologic research. It was developed according to three well-developed standards agreed by nutrition science community.
2) Python code to manage a graph database of nutritional epidemiologic research.

# Ontology for Nutritional Epidemiology (ONE)
Nutritional epidemiology is a special research area. The general ontologies for food science, nutrition science or medical science failed to cover the specific characteristics of Nutritional Epidemiological studies. As a result, we developed the ontology for nutritional epidemiology (ONE), which includes the key elements of Nutritional Epidemiological research.

### Homepage
http://www.strobe-nut.org/content/strobe-nut-ontology
### BioPortal
https://bioportal.bioontology.org/ontologies/ONE
### Publication
Yang, C.; Ambayo, H.; De Baets, B.; Kolsteren, P.; Thanintorn, N.; Hawwash, D.; Bouwman, J.; Bronselaer, A.; Pattyn, F.; Lachat, C. An Ontology to Standardize Research Output of Nutritional Epidemiology: From Paper-Based Standards to Linked Content. Nutrients 2019, 11, 1300. https://doi.org/10.3390/nu11061300


# A Python module
It has been tested in Python v3.7.4 and neo4j v3.5.6.

A Python module was developed to process the content and STROBE-nut annotations of nutritional epidemiologic papers in XML format:
1) “Input.py”: extract and store metadata of papers through the “Springer Nature API Portal” or in local XML files respectively; 
2) “Annotate.py”: annotate the reporting completeness of papers reported according to STROBE-nut reporting guidelines;
3) “Figure.py”: visualize the statistics of reporting completeness of paper(s); visualize the reporting frequency of STROBE-nut items.

### code
Please download the code under the folder "strobenut".


