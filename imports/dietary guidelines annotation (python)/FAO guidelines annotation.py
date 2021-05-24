def get(url, country):
    import re
    import operator
    from py2neo import Graph, Node, Relationship
    from stanfordcorenlp import StanfordCoreNLP
    import urllib.request, urllib.error, urllib.parse
    import json
    import os
    from pprint import pprint
    try:
        from urllib import request
    except:
        from urllib2 import urlopen as request
        from urllib2 import Request
    from bs4 import BeautifulSoup

    #open a graph database
    graph = Graph("http://localhost:7474", auth=("neo4j", ""))

    #load the NLP model
    stanford_model = StanfordCoreNLP(r'/Users/chenyang/opt/anaconda3/lib/python3.8/site-packages/stanfordcorenlp/stanford-corenlp-4.2.0', lang='en')

    REST_URL = "http://data.bioontology.org"
    API_KEY = "555dccd0-37ca-4de0-b722-bc491b888622"

    #use the ontology checking API
    def get_json(url):
        opener = urllib.request.build_opener()
        opener.addheaders = [('Authorization', 'apikey token=' + API_KEY)]
        return json.loads(opener.open(url).read())

    def print_annotations(annotations, get_class=True):
        for result in annotations:
            class_details = result["annotatedClass"]
            if get_class:
                try:
                    class_details = get_json(result["annotatedClass"]["links"]["self"])
                except urllib.error.HTTPError:
                    print(f"Error retrieving {result['annotatedClass']['@id']}")
                    continue
            if class_details["@id"] not in id_set:
                id_set.append(class_details["@id"])
                label_set.append(class_details["prefLabel"])

            if result["hierarchy"]:
                print("\n\tHierarchy annotations")
                for annotation in result["hierarchy"]:
                    try:
                        class_details = get_json(annotation["annotatedClass"]["links"]["self"])
                    except urllib.error.HTTPError:
                        print(f"Error retrieving {annotation['annotatedClass']['@id']}")
                        continue
                    pref_label = class_details["prefLabel"] or "no label"
                    print("\t\tClass details")
                    print("\t\t\tid: " + class_details["@id"])
                    print("\t\t\tprefLabel: " + class_details["prefLabel"])
                    print("\t\t\tontology: " + class_details["links"]["ontology"])
                    print("\t\t\tdistance from originally annotated class: " + str(annotation["distance"]))
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    }
    m = request.urlopen(request.Request(url, headers=HEADERS)).read()
    s = BeautifulSoup(m, "html.parser")
    metadata = s.findAll("p", attrs={"class":"bodytext"})

    n=len(metadata)

    #find official name
    official_name = ""
    for nn in range(1,n):
        if len(metadata[nn].get_text().split()) < 3:
            nx=nn
            break
        else:
            official_name += metadata[nn].get_text()

    print(country + "--" + official_name)
    print("processing...")
    ##create ontology
    official_name_onto = Node("dietary guidelines", name=official_name, area = country)
    graph.create(official_name_onto)
    ##nlp
    nation_set=[]
    res = stanford_model.ner(official_name)
    ##"n_t" = a temporary used number
    for n_t in range(0,len(res)):
        id_set=[]
        label_set=[]
        if res[n_t][1]=="NATIONALITY":
            if res[n_t][0] not in nation_set:
                nation_set.append(res[n_t][0])
                text_to_annotate = res[n_t][0]
                annotations = get_json(REST_URL + "/annotator?text=" + urllib.parse.quote(text_to_annotate)+"&ontologies=NCIT,MESH")
                print_annotations(annotations)
                Nation_onto=Node("nation", name=res[n_t][0])
                relation = Relationship(official_name_onto, "nation/language", Nation_onto)
                graph.create(relation)
                for nn in range(0,len(id_set)):
                    identifier=Node("identifier", url=id_set[nn])
                    relation = Relationship(Nation_onto, "identifier", identifier)
                    graph.create(relation)

    #find all publication years
    publication_year = []

    for nn in range(nx+1,n):
        if len(metadata[nn].get_text().split()) < 4:
            nx=nn
            break
        else:
            publication_year.append(metadata[nn].get_text())

    publication_year_para_onto = Node("description", content = publication_year)
    relation = Relationship(official_name_onto, "publication year", publication_year_para_onto)
    graph.create(relation)

    res = stanford_model.ner(str(publication_year))

    date_set=[]
    for n_t in range(0,len(res)):
        if res[n_t][1]=="DATE":
            if res[n_t][0] not in nation_set:
                date_set.append(res[n_t][0])

    date_set = re.findall('\d+', str(date_set))
    date_set = sorted(date_set, reverse=False)

    for date in date_set:
        publication_year_onto=Node("value", name = date, value = date, unit= "year")
        relation = Relationship(publication_year_para_onto, "has value", publication_year_onto)
        graph.create(relation)


    #calculation publication frequency
    if len(date_set) > 1:
        frequency=(int(date_set[len(date_set)-1]) - int(date_set[0]))/(len(date_set)-1)
        frequency_onto=Node("publication frequency", name="each " + str(int(frequency))+" years", value=int(frequency), unit="year")
        relation = Relationship(official_name_onto, "publication frequency", frequency_onto)
        graph.create(relation)

    #find stakeholders
    stakeholders = []
    for nn in range(nx+1,n):
        if len(metadata[nn].get_text().split()) < 3:
            nx=nn
            break
        else:
            stakeholders.append(str(metadata[nn].get_text()))

    stakeholders_para_onto = Node("description", content = stakeholders)
    relation = Relationship(official_name_onto, "stakeholders", stakeholders_para_onto)
    graph.create(relation)

    res = stanford_model.ner(str(stakeholders))
    organization = ""
    organization_set = []
    for n_t in range(0,len(res)):
        if res[n_t][1]=="ORGANIZATION":
            organization += " " + res[n_t][0]
        else:
            if organization != "":
                organization_set.append(str(organization))
                organization = ""

    organization_set_clean=[]
    for organization in organization_set:
        if organization not in organization_set_clean:
            organization_set_clean.append(organization)

    for organization in organization_set_clean:
        stakeholder_onto = Node("stakeholder", name = organization)
        relation = Relationship(stakeholders_para_onto, "has value", stakeholder_onto)
        graph.create(relation)


    #find audiance
    audience = []
    for nn in range(nx+1,n):
        nx=nn
        if len(metadata[nn].get_text().split()) < 3:
            break
        else:
            audience.append(metadata[nn].get_text())

    audience_onto = Node("audience", content = audience)
    relation = Relationship(official_name_onto, "audience", audience_onto)
    graph.create(relation)


    res = stanford_model.ner(str(audience))
    age=""
    age_set=[]

    ##nlp for getting age
    for n_t in range(0,len(res)):
        if res[n_t][1]=="DURATION":
            age += " " + res[n_t][0]
        else:
            if age != "":
                age_set.append(age)
                age = ""

    age_set_clean=[]
    for age in age_set:
        if age not in age_set_clean:
            age_set_clean.append(age)

    for age in age_set_clean:
        age_onto = Node("age", name = "over"+age)
        relation = Relationship(audience_onto, "age", age_onto)
        graph.create(relation)

    #find food guide
    food_guide=[]
    for nn in range(nx+1,n):
        nx=nn
        if len(metadata[nn].get_text().split()) < 3:
            break
        else:
            food_guide.append(metadata[nn].get_text())

    food_guide_onto = Node("food guide", name="food guide", content = food_guide)
    relation = Relationship(official_name_onto, "food guide", food_guide_onto)
    graph.create(relation)
    ##add identifiers
    id_set = []
    annotations = get_json(REST_URL + "/annotator?text=" + urllib.parse.quote(str(food_guide))+"&ontologies=FOODON")
    print_annotations(annotations)

    for nn in range(0,len(id_set)):
        identifier=Node("identifier", url=id_set[nn])
        relation = Relationship(food_guide_onto, "identifier", identifier)
        graph.create(relation)

    #find food guidelines(messages)
    guidelines = s.findAll('ul')
    n_max = len(guidelines)-6

    for n in range(2, n_max):
        for li in guidelines[n].findAll('li'):
            guideline = Node("message", content=li.get_text())
            relation = Relationship(official_name_onto, "message", guideline)
            graph.create(relation)
            id_set = []
            label_set = []
            annotations = get_json(REST_URL + "/annotator?text=" + urllib.parse.quote(str(li.get_text()))+"&ontologies=FOODON")
            print_annotations(annotations)
            if len(id_set) != 0:
                for nn in range(0,len(id_set)):
                    food_onto = Node("food", name=label_set[nn], url=id_set[nn])
                    relation = Relationship(guideline, "has value", food_onto)
                    graph.create(relation)
                    identifier=Node("identifier", url=id_set[nn])
                    relation = Relationship(food_onto, "identifier", identifier)
                    graph.create(relation)
    print("done")
    print("")
