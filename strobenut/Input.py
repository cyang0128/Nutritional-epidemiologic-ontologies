
def DOI(doi):
    from lxml import etree
    from py2neo import Graph, Node, Relationship
    import re
    
    print("Online: the paper (doi:", doi, ") referring STROBE-nut reporting guidelines has been converted.")
    
    graph = Graph("http://localhost:7474", auth=("neo4j", "")) #please fill in your password!
    
    #retrieve article content from "Springer Natural API Portal"
    url="http://api.springernature.com/openaccess/jats/doi/{value}?api_key=???".format(value=doi)
    xml = etree.parse(url).getroot()

    #retrieve an article title
    title = xml.xpath('//article-meta/title-group/article-title//text()')
    title_node = Node("Article", Subject="Nutritional epidemiology", name=title)
    graph.create(title_node)


    #retrieve an article abstract
    abstract = xml.xpath('//abstract//text()')
    ab_node = Node("Abstract", name="Abstract", value=abstract)
    title_ab = Relationship(title_node, "hasAbstract", ab_node)
    graph.create(title_ab)

    #retrieve an article doi
    doi = xml.xpath('.//article-id[@pub-id-type="doi"]//text()')
    title_node['DOI'] = re.sub('^[^\s]{2}|[^\s]{2}$','',str(doi))
    graph.push(title_node)

    #retrieve a set of keywords
    #develop a set for keywords
    keywords_node = Node("Keywords set", name="Keywords set")
    title_keywords = Relationship(title_node, "has", keywords_node)
    graph.create(title_keywords)
    #retrieve keywords
    keyword_group = xml.xpath('//article-meta/kwd-group/*//text()')
    for keyword in keyword_group:
        if keyword != "Keywords":
            keyword_node = Node("Keyword", name=keyword)
            keywordsInGroup = Relationship(keywords_node, "keyword", keyword_node)
            graph.create(keywordsInGroup)

    #retrieve introduction, methods, results, discussion as well as their sub-sections
    main_parts = xml.xpath('//body/sec/title/text()')
    n=0
    for main_part in main_parts:
        n = n+1
        path='//body/sec[{value}]//text()'.format(value=n)
        text = xml.xpath(path)
        
        main_part_node = Node("Section", name=main_part, content=text)
        title_mainpart = Relationship(title_node, "section", main_part_node)
        graph.create(title_mainpart)
        
        sub_path='//body/sec[{value}]/sec/title/text()'.format(value=n)
        sub_parts = xml.xpath(sub_path)
        for sub_part in sub_parts:
            sub_part_node = Node("Sub-section", name=sub_part)
            relation = Relationship(main_part_node, "sub-section", sub_part_node)
            graph.create(relation)

def File(path):
    from lxml import etree
    from py2neo import Graph, Node, Relationship
    import re

    graph = Graph("http://localhost:7474", auth=("neo4j", "")) #your password!!!


    #retrieve article content from a local path
    xml = etree.parse(path).getroot()


    #retrieve an article title
    title = xml.xpath('//article-meta/title-group/article-title//text()')
    title_node = Node("Article", Subject="Nutritional epidemiology", name=title)
    graph.create(title_node)


    #retrieve an article abstract
    abstract = xml.xpath('//abstract//text()')
    ab_node = Node("Abstract", name="Abstract", value=abstract)
    title_ab = Relationship(title_node, "hasAbstract", ab_node)
    graph.create(title_ab)

    #retrieve an article doi
    doi = xml.xpath('.//article-id[@pub-id-type="doi"]//text()')
    title_node['DOI'] = re.sub('^[^\s]{2}|[^\s]{2}$','',str(doi))
    graph.push(title_node)
    print("Local file: the paper (doi:", re.sub('^[^\s]{2}|[^\s]{2}$','',str(doi)), ") referring STROBE-nut reporting guidelines has been converted.")

    #retrieve a set of keywords
    #develop a set for keywords
    keywords_node = Node("Keywords set", name="Keywords set")
    title_keywords = Relationship(title_node, "has", keywords_node)
    graph.create(title_keywords)
    #retrieve keywords
    keyword_group = xml.xpath('//article-meta/kwd-group/*//text()')
    for keyword in keyword_group:
        if keyword != "Keywords":
            keyword_node = Node("Keyword", name=keyword)
            keywordsInGroup = Relationship(keywords_node, "keyword", keyword_node)
            graph.create(keywordsInGroup)

    #retrieve introduction, methods, results, discussion as well as their sub-sections
    main_parts = xml.xpath('//body/sec/title/text()')
    n=0
    for main_part in main_parts:
        n = n+1
        path='//body/sec[{value}]//text()'.format(value=n)
        text = xml.xpath(path)
        
        main_part_node = Node("Section", name=main_part, content=text)
        title_mainpart = Relationship(title_node, "section", main_part_node)
        graph.create(title_mainpart)
        
        sub_path='//body/sec[{value}]/sec/title/text()'.format(value=n)
        sub_parts = xml.xpath(sub_path)
        for sub_part in sub_parts:
            sub_part_node = Node("Sub-section", name=sub_part)
            relation = Relationship(main_part_node, "sub-section", sub_part_node)
            graph.create(relation)
