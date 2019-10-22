
def DOI(doi):
    from lxml import etree
    from py2neo import Graph, Node, Relationship
    import re
    
    print("Online: the paper (doi:", doi, ") referring STROBE-nut reporting guidelines has been converted.")
    
    graph = Graph("http://localhost:7474", auth=("neo4j", ""))
    
    #互联网导入文章的XML
    url="http://api.springernature.com/openaccess/jats/doi/{value}?api_key=f4439f0543b0e99cd4f1e00af3a6010f".format(value=doi)
    xml = etree.parse(url).getroot()

    #定位文章的题目并传入知识图谱
    title = xml.xpath('//article-meta/title-group/article-title//text()')
    title_node = Node("Article", Subject="Nutritional epidemiology", name=title)
    graph.create(title_node)


    #定位文章的摘要并传入知识图谱
    abstract = xml.xpath('//abstract//text()')
    ab_node = Node("Abstract", name="Abstract", value=abstract)
    title_ab = Relationship(title_node, "hasAbstract", ab_node)
    graph.create(title_ab)

    #定位文章的DOI并传入知识图谱，作为题目的属性,，DOI用正则表达处理为string
    doi = xml.xpath('.//article-id[@pub-id-type="doi"]//text()')
    title_node['DOI'] = re.sub('^[^\s]{2}|[^\s]{2}$','',str(doi))
    graph.push(title_node)

    #定位文章的keyword并传入知识图谱，连接题目
    #创建keywords组
    keywords_node = Node("Keywords set", name="Keywords set")
    title_keywords = Relationship(title_node, "has", keywords_node)
    graph.create(title_keywords)
    #导入keywords
    keyword_group = xml.xpath('//article-meta/kwd-group/*//text()')
    for keyword in keyword_group:
        if keyword != "Keywords":
            keyword_node = Node("Keyword", name=keyword)
            keywordsInGroup = Relationship(keywords_node, "keyword", keyword_node)
            graph.create(keywordsInGroup)

    #导入文章introduction, methods, results, discussion等, 并导入 这些的子部分

    #定位文章的部分并传入知识图谱，连接题目
    main_parts = xml.xpath('//body/sec/title/text()')
    n=0
    for main_part in main_parts:
        n = n+1
        #传入各部分文本
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

    graph = Graph("http://localhost:7474", auth=("neo4j", ""))


    #本地导入文章的XML
    xml = etree.parse(path).getroot()


    #定位文章的题目并传入知识图谱
    title = xml.xpath('//article-meta/title-group/article-title//text()')
    title_node = Node("Article", Subject="Nutritional epidemiology", name=title)
    graph.create(title_node)


    #定位文章的摘要并传入知识图谱
    abstract = xml.xpath('//abstract//text()')
    ab_node = Node("Abstract", name="Abstract", value=abstract)
    title_ab = Relationship(title_node, "hasAbstract", ab_node)
    graph.create(title_ab)

    #定位文章的DOI并传入知识图谱，作为题目的属性，DOI用正则表达处理为string
    doi = xml.xpath('.//article-id[@pub-id-type="doi"]//text()')
    title_node['DOI'] = re.sub('^[^\s]{2}|[^\s]{2}$','',str(doi))
    graph.push(title_node)
    print("Local file: the paper (doi:", re.sub('^[^\s]{2}|[^\s]{2}$','',str(doi)), ") referring STROBE-nut reporting guidelines has been converted.")

    #定位文章的keyword并传入知识图谱，连接题目
    #创建keywords组
    keywords_node = Node("Keywords set", name="Keywords set")
    title_keywords = Relationship(title_node, "has", keywords_node)
    graph.create(title_keywords)
    #导入keywords
    keyword_group = xml.xpath('//article-meta/kwd-group/*//text()')
    for keyword in keyword_group:
        if keyword != "Keywords":
            keyword_node = Node("Keyword", name=keyword)
            keywordsInGroup = Relationship(keywords_node, "keyword", keyword_node)
            graph.create(keywordsInGroup)

    #导入文章introduction, methods, results, discussion等, 并导入 这些的子部分

    #定位文章的部分并传入知识图谱，连接题目
    main_parts = xml.xpath('//body/sec/title/text()')
    n=0
    for main_part in main_parts:
        n = n+1
        #传入各部分文本
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


