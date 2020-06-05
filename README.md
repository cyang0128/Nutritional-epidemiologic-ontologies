This repository includes:
1) one ontology for nutritional epidemiologic research. It was developed according to three well-developed standards agreed by nutrition science community.
2) Python code to manage a graph database of nutritional epidemiologic papers.

# Ontology for Nutritional Epidemiology (ONE)
Nutritional epidemiology is a specific research area. The generic ontologies for food science, nutrition science or medical science failed to cover the specific characteristics of nutritional epidemiologic studies. As a result, we developed the ontology for nutritional epidemiology (ONE) in order to describe nutritional epidemiologic studies accurately.

### Homepage
http://www.strobe-nut.org/content/strobe-nut-ontology
### BioPortal
https://bioportal.bioontology.org/ontologies/ONE
### Publications
Yang, C.; Ambayo, H.; De Baets, B.; Kolsteren, P.; Thanintorn, N.; Hawwash, D.; Bouwman, J.; Bronselaer, A.; Pattyn, F.; Lachat, C. An Ontology to Standardize Research Output of Nutritional Epidemiology: From Paper-Based Standards to Linked Content. Nutrients 2019, 11, 1300. https://doi.org/10.3390/nu11061300

Yang, C.; Pinart, M.; Kolsteren, P.; Van Camp, J.; De Cock, N.; Nimptsch, K.; et al. Perspective: Essential study quality descriptors for data from nutritional epidemiologic research. Advances in Nutrition. 2017;8(5):639–51. https://doi.org/10.3945/an.117.015651

# A Python module for ONE
It has been tested in Python v3.7.4 and neo4j v3.5.6.

A Python module was developed to process the content and STROBE-nut annotations of nutritional epidemiologic papers in XML format:
1) “Input.py”: extract and store metadata of papers through the “Springer Nature API Portal” or in local XML files respectively; 
2) “Annotate.py”: annotate the reporting completeness of papers according to the STROBE-nut reporting guidelines;
3) “Figure.py”: visualize the statistics of reporting completeness of papers; visualize the reporting frequency of the STROBE-nut items.

<div align=center><img width="500" height="250" src="images/codeExample.png"/></div>

### Code
Please download the code under the folder "strobenut".

### Publications
Yang, C.; Hawwash, D.; De Baets, B.; Bouwman, J.; Lachat, C. Perspective: Towards automated tracking of content and evidence appraisal of nutrition research. Advances in Nutrition. 2020. (In press)

Yang, C., De Baets, B., & Lachat, C. (2019). From DIKW pyramid to graph database: a tool for machine processing of nutritional epidemiologic research data. In 2019 IEEE International Conference on Big Data (Big Data) (pp. 5202–5205). Los Angeles, CA, USA: IEEE. https://doi.org/10.1109/bigdata47090.2019.9006469

## License
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>
