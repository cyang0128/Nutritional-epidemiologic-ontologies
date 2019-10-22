def nut(doi, *nut_items):

    from py2neo import Graph, Node, Relationship

    graph = Graph("http://localhost:7474", auth=("neo4j", ""))

    query = """
    MATCH (n:`Article`{DOI:'%s'})
    MERGE (n)-[:`STROBE-nut`{DOI:'10.1371/journal.pmed.1002036'}]->(:`STROBE-nut article`{name:'Harmonized Article', DOI:'%s'})
    """ %(doi,doi)
    graph.run(query)

    for nut_item in nut_items:
        if nut_item == 'nut-1':
            query = """
            MATCH (n:`STROBE-nut article`{name:'Harmonized Article', DOI:'%s'})
            MERGE (n)-[:section]->(:`STROBE-nut section`{name:'Title/Abstract', DOI:'%s'})
            """ %(doi,doi)
            graph.run(query)
            
            query = """
            MATCH (n:`STROBE-nut section`{name:'Title/Abstract', DOI:'%s'})
            MERGE (n)-[:reports]->(:`STROBE-nut item`{name:'Dietary assessment method', item:'nut-1', DOI:'%s'})
            """ %(doi, doi)
            graph.run(query)

        if nut_item == 'nut-5':
            query = """
            MATCH (n:`STROBE-nut article`{name:'Harmonized Article', DOI:'%s'})
            MERGE (n)-[:section]->(:`STROBE-nut section`{name:'Methods', DOI:'%s'})
            """ %(doi,doi)
            graph.run(query)

            query = """
            MATCH (n:`STROBE-nut section`{name:'Methods', DOI:'%s'})
            MERGE (n)-[:`sub-section`]->(:`STROBE-nut sub-section`{name:'Settings', DOI:'%s'})
            """ %(doi,doi)
            graph.run(query)
            
            query = """
            MATCH (n:`STROBE-nut sub-section`{name:'Settings', DOI:'%s'})
            MERGE (n)-[:reports]->(:`STROBE-nut item`{name:'Settings affecting dietary intake of participants', item:'nut-5', DOI:'%s'})
            """ %(doi, doi)
            graph.run(query)
            
        if nut_item == 'nut-6':
            query = """
            MATCH (n:`STROBE-nut article`{name:'Harmonized Article', DOI:'%s'})
            MERGE (n)-[:section]->(:`STROBE-nut section`{name:'Methods', DOI:'%s'})
            """ %(doi,doi)
            graph.run(query)

            query = """
            MATCH (n:`STROBE-nut section`{name:'Methods', DOI:'%s'})
            MERGE (n)-[:`sub-section`]->(:`STROBE-nut sub-section`{name:'Participants', DOI:'%s'})
            """ %(doi,doi)
            graph.run(query)
            
            query = """
            MATCH (:`STROBE-nut section`{name:'Methods', DOI:'%s'})-[]->(n:`STROBE-nut sub-section`{name:'Participants', DOI:'%s'})
            MERGE (n)-[:reports]->(:`STROBE-nut item`{name:'Dietary, physiological or nutritional characteristics', item:'nut-6', DOI:'%s'})
            """ %(doi, doi, doi)
            graph.run(query)
            
        if nut_item == 'nut-7.1':
            query = """
            MATCH (n:`STROBE-nut article`{name:'Harmonized Article', DOI:'%s'})
            MERGE (n)-[:section]->(:`STROBE-nut section`{name:'Methods', DOI:'%s'})
            """ %(doi,doi)
            graph.run(query)

            query = """
            MATCH (n:`STROBE-nut section`{name:'Methods', DOI:'%s'})
            MERGE (n)-[:`sub-section`]->(:`STROBE-nut sub-section`{name:'Variables', DOI:'%s'})
            """ %(doi,doi)
            graph.run(query)
            
            query = """
            MATCH (n:`STROBE-nut sub-section`{name:'Variables', DOI:'%s'})
            MERGE (n)-[:reports]->(:`STROBE-nut item`{name:'Food components', item:'nut-7.1', DOI:'%s'})
            """ %(doi, doi)
            graph.run(query)
            
        if nut_item == 'nut-7.2':
            query = """
            MATCH (n:`STROBE-nut article`{name:'Harmonized Article', DOI:'%s'})
            MERGE (n)-[:section]->(:`STROBE-nut section`{name:'Methods', DOI:'%s'})
            """ %(doi,doi)
            graph.run(query)

            query = """
            MATCH (n:`STROBE-nut section`{name:'Methods', DOI:'%s'})
            MERGE (n)-[:`sub-section`]->(:`STROBE-nut sub-section`{name:'Variables', DOI:'%s'})
            """ %(doi,doi)
            graph.run(query)
            
            query = """
            MATCH (n:`STROBE-nut sub-section`{name:'Variables', DOI:'%s'})
            MERGE (n)-[:reports]->(:`STROBE-nut item`{name:'Methods to obtain dietary patterns', item:'nut-7.2', DOI:'%s'})
            """ %(doi, doi)
            graph.run(query)
            
        if nut_item == 'nut-8.1':
            query = """
            MATCH (n:`STROBE-nut article`{name:'Harmonized Article', DOI:'%s'})
            MERGE (n)-[:section]->(:`STROBE-nut section`{name:'Methods', DOI:'%s'})
            """ %(doi,doi)
            graph.run(query)

            query = """
            MATCH (n:`STROBE-nut section`{name:'Methods', DOI:'%s'})
            MERGE (n)-[:`sub-section`]->(:`STROBE-nut sub-section`{name:'Data sources - measurements', DOI:'%s'})
            """ %(doi,doi)
            graph.run(query)
            
            query = """
            MATCH (n:`STROBE-nut sub-section`{name:'Data sources - measurements', DOI:'%s'})
            MERGE (n)-[:reports]->(:`STROBE-nut item`{name:'Dietary assessment method', item:'nut-8.1', DOI:'%s'})
            """ %(doi, doi)
            graph.run(query)
        
        if nut_item == 'nut-8.2':
            query = """
            MATCH (n:`STROBE-nut article`{name:'Harmonized Article', DOI:'%s'})
            MERGE (n)-[:section]->(:`STROBE-nut section`{name:'Methods', DOI:'%s'})
            """ %(doi,doi)
            graph.run(query)

            query = """
            MATCH (n:`STROBE-nut section`{name:'Methods', DOI:'%s'})
            MERGE (n)-[:`sub-section`]->(:`STROBE-nut sub-section`{name:'Data sources - measurements', DOI:'%s'})
            """ %(doi,doi)
            graph.run(query)
            
            query = """
            MATCH (n:`STROBE-nut sub-section`{name:'Data sources - measurements', DOI:'%s'})
            MERGE (n)-[:reports]->(:`STROBE-nut item`{name:'Food composition data', item:'nut-8.2', DOI:'%s'})
            """ %(doi, doi)
            graph.run(query)
            
        if nut_item == 'nut-8.3':
            query = """
            MATCH (n:`STROBE-nut article`{name:'Harmonized Article', DOI:'%s'})
            MERGE (n)-[:section]->(:`STROBE-nut section`{name:'Methods', DOI:'%s'})
            """ %(doi,doi)
            graph.run(query)

            query = """
            MATCH (n:`STROBE-nut section`{name:'Methods', DOI:'%s'})
            MERGE (n)-[:`sub-section`]->(:`STROBE-nut sub-section`{name:'Data sources - measurements', DOI:'%s'})
            """ %(doi,doi)
            graph.run(query)
            
            query = """
            MATCH (n:`STROBE-nut sub-section`{name:'Data sources - measurements', DOI:'%s'})
            MERGE (n)-[:reports]->(:`STROBE-nut item`{name:'Dietary guidelines and evaluation approach', item:'nut-8.3', DOI:'%s'})
            """ %(doi, doi)
            graph.run(query)

            
        if nut_item == 'nut-8.4':
            query = """
            MATCH (n:`STROBE-nut article`{name:'Harmonized Article', DOI:'%s'})
            MERGE (n)-[:section]->(:`STROBE-nut section`{name:'Methods', DOI:'%s'})
            """ %(doi,doi)
            graph.run(query)

            query = """
            MATCH (n:`STROBE-nut section`{name:'Methods', DOI:'%s'})
            MERGE (n)-[:`sub-section`]->(:`STROBE-nut sub-section`{name:'Data sources - measurements', DOI:'%s'})
            """ %(doi,doi)
            graph.run(query)
            
            query = """
            MATCH (n:`STROBE-nut sub-section`{name:'Data sources - measurements', DOI:'%s'})
            MERGE (n)-[:reports]->(:`STROBE-nut item`{name:'Nutritional biomarkers', item:'nut-8.4', DOI:'%s'})
            """ %(doi, doi)
            graph.run(query)
            
            
        if nut_item == 'nut-8.5':
            query = """
            MATCH (n:`STROBE-nut article`{name:'Harmonized Article', DOI:'%s'})
            MERGE (n)-[:section]->(:`STROBE-nut section`{name:'Methods', DOI:'%s'})
            """ %(doi,doi)
            graph.run(query)

            query = """
            MATCH (n:`STROBE-nut section`{name:'Methods', DOI:'%s'})
            MERGE (n)-[:`sub-section`]->(:`STROBE-nut sub-section`{name:'Data sources - measurements', DOI:'%s'})
            """ %(doi,doi)
            graph.run(query)
            
            query = """
            MATCH (n:`STROBE-nut sub-section`{name:'Data sources - measurements', DOI:'%s'})
            MERGE (n)-[:reports]->(:`STROBE-nut item`{name:'Nondietary data', item:'nut-8.5', DOI:'%s'})
            """ %(doi, doi)
            graph.run(query)
            
            
        if nut_item == 'nut-8.6':
            query = """
            MATCH (n:`STROBE-nut article`{name:'Harmonized Article', DOI:'%s'})
            MERGE (n)-[:section]->(:`STROBE-nut section`{name:'Methods', DOI:'%s'})
            """ %(doi,doi)
            graph.run(query)

            query = """
            MATCH (n:`STROBE-nut section`{name:'Methods', DOI:'%s'})
            MERGE (n)-[:`sub-section`]->(:`STROBE-nut sub-section`{name:'Data sources - measurements', DOI:'%s'})
            """ %(doi,doi)
            graph.run(query)
            
            query = """
            MATCH (n:`STROBE-nut sub-section`{name:'Data sources - measurements', DOI:'%s'})
            MERGE (n)-[:reports]->(:`STROBE-nut item`{name:'Validity of the dietary assessment method', item:'nut-8.6', DOI:'%s'})
            """ %(doi, doi)
            graph.run(query)
            
        if nut_item == 'nut-9':
            query = """
            MATCH (n:`STROBE-nut article`{name:'Harmonized Article', DOI:'%s'})
            MERGE (n)-[:section]->(:`STROBE-nut section`{name:'Methods', DOI:'%s'})
            """ %(doi,doi)
            graph.run(query)

            query = """
            MATCH (n:`STROBE-nut section`{name:'Methods', DOI:'%s'})
            MERGE (n)-[:`sub-section`]->(:`STROBE-nut sub-section`{name:'Bias', DOI:'%s'})
            """ %(doi,doi)
            graph.run(query)
            
            query = """
            MATCH (n:`STROBE-nut sub-section`{name:'Bias', DOI:'%s'})
            MERGE (n)-[:reports]->(:`STROBE-nut item`{name:'Bias in dietary assessment', item:'nut-9', DOI:'%s'})
            """ %(doi, doi)
            graph.run(query)
            
        if nut_item == 'nut-11':
            query = """
            MATCH (n:`STROBE-nut article`{name:'Harmonized Article', DOI:'%s'})
            MERGE (n)-[:section]->(:`STROBE-nut section`{name:'Methods', DOI:'%s'})
            """ %(doi,doi)
            graph.run(query)

            query = """
            MATCH (n:`STROBE-nut section`{name:'Methods', DOI:'%s'})
            MERGE (n)-[:`sub-section`]->(:`STROBE-nut sub-section`{name:'Quantitative variables', DOI:'%s'})
            """ %(doi,doi)
            graph.run(query)
            
            query = """
            MATCH (n:`STROBE-nut sub-section`{name:'Quantitative variables', DOI:'%s'})
            MERGE (n)-[:reports]->(:`STROBE-nut item`{name:'Categorization of dietary data', item:'nut-11', DOI:'%s'})
            """ %(doi, doi)
            graph.run(query)
            
        if nut_item == 'nut-12.1':
            query = """
            MATCH (n:`STROBE-nut article`{name:'Harmonized Article', DOI:'%s'})
            MERGE (n)-[:section]->(:`STROBE-nut section`{name:'Methods', DOI:'%s'})
            """ %(doi,doi)
            graph.run(query)

            query = """
            MATCH (n:`STROBE-nut section`{name:'Methods', DOI:'%s'})
            MERGE (n)-[:`sub-section`]->(:`STROBE-nut sub-section`{name:'Statistical methods', DOI:'%s'})
            """ %(doi,doi)
            graph.run(query)
            
            query = """
            MATCH (n:`STROBE-nut sub-section`{name:'Statistical methods', DOI:'%s'})
            MERGE (n)-[:reports]->(:`STROBE-nut item`{name:'method to combine dietary data', item:'nut-12.1', DOI:'%s'})
            """ %(doi, doi)
            graph.run(query)
            
        if nut_item == 'nut-12.2':
            query = """
            MATCH (n:`STROBE-nut article`{name:'Harmonized Article', DOI:'%s'})
            MERGE (n)-[:section]->(:`STROBE-nut section`{name:'Methods', DOI:'%s'})
            """ %(doi,doi)
            graph.run(query)

            query = """
            MATCH (n:`STROBE-nut section`{name:'Methods', DOI:'%s'})
            MERGE (n)-[:`sub-section`]->(:`STROBE-nut sub-section`{name:'Statistical methods', DOI:'%s'})
            """ %(doi,doi)
            graph.run(query)
            
            query = """
            MATCH (n:`STROBE-nut sub-section`{name:'Statistical methods', DOI:'%s'})
            MERGE (n)-[:reports]->(:`STROBE-nut item`{name:'Energy adjustments, intake modeling, weighting factors', item:'nut-12.2', DOI:'%s'})
            """ %(doi, doi)
            graph.run(query)
            
        if nut_item == 'nut-12.3':
            query = """
            MATCH (n:`STROBE-nut article`{name:'Harmonized Article', DOI:'%s'})
            MERGE (n)-[:section]->(:`STROBE-nut section`{name:'Methods', DOI:'%s'})
            """ %(doi,doi)
            graph.run(query)

            query = """
            MATCH (n:`STROBE-nut section`{name:'Methods', DOI:'%s'})
            MERGE (n)-[:`sub-section`]->(:`STROBE-nut sub-section`{name:'Statistical methods', DOI:'%s'})
            """ %(doi,doi)
            graph.run(query)
            
            query = """
            MATCH (n:`STROBE-nut sub-section`{name:'Statistical methods', DOI:'%s'})
            MERGE (n)-[:reports]->(:`STROBE-nut item`{name:'Adjustments for measurement error', item:'nut-12.3', DOI:'%s'})
            """ %(doi, doi)
            graph.run(query)
            
        if nut_item == 'nut-13':
            query = """
            MATCH (n:`STROBE-nut article`{name:'Harmonized Article', DOI:'%s'})
            MERGE (n)-[:section]->(:`STROBE-nut section`{name:'Results', DOI:'%s'})
            """ %(doi,doi)
            graph.run(query)

            query = """
            MATCH (n:`STROBE-nut section`{name:'Results', DOI:'%s'})
            MERGE (n)-[:`sub-section`]->(:`STROBE-nut sub-section`{name:'Participants', DOI:'%s'})
            """ %(doi,doi)
            graph.run(query)
            
            query = """
            MATCH (:`STROBE-nut section`{name:'Results', DOI:'%s'})-[]->(n:`STROBE-nut sub-section`{name:'Participants', DOI:'%s'})
            MERGE (n)-[:reports]->(:`STROBE-nut item`{name:'Number of individuals excluded', item:'nut-13', DOI:'%s'})
            """ %(doi, doi, doi)
            graph.run(query)
            
        if nut_item == 'nut-14':
            query = """
            MATCH (n:`STROBE-nut article`{name:'Harmonized Article', DOI:'%s'})
            MERGE (n)-[:section]->(:`STROBE-nut section`{name:'Results', DOI:'%s'})
            """ %(doi,doi)
            graph.run(query)

            query = """
            MATCH (n:`STROBE-nut section`{name:'Results', DOI:'%s'})
            MERGE (n)-[:`sub-section`]->(:`STROBE-nut sub-section`{name:'Descriptive data', DOI:'%s'})
            """ %(doi,doi)
            graph.run(query)
            
            query = """
            MATCH (n:`STROBE-nut sub-section`{name:'Descriptive data', DOI:'%s'})
            MERGE (n)-[:reports]->(:`STROBE-nut item`{name:'Distribution of participant characteristics', item:'nut-14', DOI:'%s'})
            """ %(doi, doi)
            graph.run(query)
            
        if nut_item == 'nut-16':
            query = """
            MATCH (n:`STROBE-nut article`{name:'Harmonized Article', DOI:'%s'})
            MERGE (n)-[:section]->(:`STROBE-nut section`{name:'Results', DOI:'%s'})
            """ %(doi,doi)
            graph.run(query)

            query = """
            MATCH (n:`STROBE-nut section`{name:'Results', DOI:'%s'})
            MERGE (n)-[:`sub-section`]->(:`STROBE-nut sub-section`{name:'Main results', DOI:'%s'})
            """ %(doi,doi)
            graph.run(query)
            
            query = """
            MATCH (n:`STROBE-nut sub-section`{name:'Main results', DOI:'%s'})
            MERGE (n)-[:reports]->(:`STROBE-nut item`{name:'Dietary supplement intake', item:'nut-16', DOI:'%s'})
            """ %(doi, doi)
            graph.run(query)
            
        if nut_item == 'nut-17':
            query = """
            MATCH (n:`STROBE-nut article`{name:'Harmonized Article', DOI:'%s'})
            MERGE (n)-[:section]->(:`STROBE-nut section`{name:'Results', DOI:'%s'})
            """ %(doi,doi)
            graph.run(query)

            query = """
            MATCH (n:`STROBE-nut section`{name:'Results', DOI:'%s'})
            MERGE (n)-[:`sub-section`]->(:`STROBE-nut sub-section`{name:'Other analyses', DOI:'%s'})
            """ %(doi,doi)
            graph.run(query)
            
            query = """
            MATCH (n:`STROBE-nut sub-section`{name:'Other analyses', DOI:'%s'})
            MERGE (n)-[:reports]->(:`STROBE-nut item`{name:'Sensitivity analysis and data imputation', item:'nut-17', DOI:'%s'})
            """ %(doi, doi)
            graph.run(query)
            
        if nut_item == 'nut-19':
            query = """
            MATCH (n:`STROBE-nut article`{name:'Harmonized Article', DOI:'%s'})
            MERGE (n)-[:section]->(:`STROBE-nut section`{name:'Discussion', DOI:'%s'})
            """ %(doi,doi)
            graph.run(query)

            query = """
            MATCH (n:`STROBE-nut section`{name:'Discussion', DOI:'%s'})
            MERGE (n)-[:`sub-section`]->(:`STROBE-nut sub-section`{name:'Limitation', DOI:'%s'})
            """ %(doi,doi)
            graph.run(query)
            
            query = """
            MATCH (n:`STROBE-nut sub-section`{name:'Limitation', DOI:'%s'})
            MERGE (n)-[:reports]->(:`STROBE-nut item`{name:'Data sources and assessment methods', item:'nut-19', DOI:'%s'})
            """ %(doi, doi)
            graph.run(query)
            
        if nut_item == 'nut-20':
            query = """
            MATCH (n:`STROBE-nut article`{name:'Harmonized Article', DOI:'%s'})
            MERGE (n)-[:section]->(:`STROBE-nut section`{name:'Discussion', DOI:'%s'})
            """ %(doi,doi)
            graph.run(query)

            query = """
            MATCH (n:`STROBE-nut section`{name:'Discussion', DOI:'%s'})
            MERGE (n)-[:`sub-section`]->(:`STROBE-nut sub-section`{name:'Interpretation', DOI:'%s'})
            """ %(doi,doi)
            graph.run(query)
            
            query = """
            MATCH (n:`STROBE-nut sub-section`{name:'Interpretation', DOI:'%s'})
            MERGE (n)-[:reports]->(:`STROBE-nut item`{name:'Nutritional relevance of the findings', item:'nut-20', DOI:'%s'})
            """ %(doi, doi)
            graph.run(query)

        if nut_item == 'nut-22.1':
            query = """
            MATCH (n:`STROBE-nut article`{name:'Harmonized Article', DOI:'%s'})
            MERGE (n)-[:section]->(:`STROBE-nut section`{name:'Other information', DOI:'%s'})
            """ %(doi,doi)
            graph.run(query)

            query = """
            MATCH (n:`STROBE-nut section`{name:'Other information', DOI:'%s'})
            MERGE (n)-[:`sub-section`]->(:`STROBE-nut sub-section`{name:'Ethics', DOI:'%s'})
            """ %(doi,doi)
            graph.run(query)
            
            query = """
            MATCH (n:`STROBE-nut sub-section`{name:'Ethics', DOI:'%s'})
            MERGE (n)-[:reports]->(:`STROBE-nut item`{name:'Consent and study approval from ethics committee', item:'nut-22.1', DOI:'%s'})
            """ %(doi, doi)
            graph.run(query)

        if nut_item == 'nut-22.2':
            query = """
            MATCH (n:`STROBE-nut article`{name:'Harmonized Article', DOI:'%s'})
            MERGE (n)-[:section]->(:`STROBE-nut section`{name:'Other information', DOI:'%s'})
            """ %(doi,doi)
            graph.run(query)

            query = """
            MATCH (n:`STROBE-nut section`{name:'Other information', DOI:'%s'})
            MERGE (n)-[:`sub-section`]->(:`STROBE-nut sub-section`{name:'Supplementary material', DOI:'%s'})
            """ %(doi,doi)
            graph.run(query)
            
            query = """
            MATCH (n:`STROBE-nut sub-section`{name:'Supplementary material', DOI:'%s'})
            MERGE (n)-[:reports]->(:`STROBE-nut item`{name:'Accessible data', item:'nut-22.2', DOI:'%s'})
            """ %(doi, doi)
            graph.run(query)


