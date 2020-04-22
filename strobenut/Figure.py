def max(n):

    from py2neo import Graph, Node, Relationship
    import matplotlib.pyplot as plt
    import matplotlib.ticker as ticker
    from IPython import get_ipython
    
    get_ipython().run_line_magic('matplotlib', 'inline')
    
    graph = Graph("http://localhost:7474", auth=("neo4j", ""))
    
    #count the number of STROBE-nut items reported per article
    query = """
    MATCH (article)-[r:`STROBE-nut`]->()-[*]->(n:`STROBE-nut item`)
    return article.DOI as `DOI`, count(*) as `nut` ORDER BY `nut` DESC LIMIT %s
    """ %(n)

    dataset = graph.run(query).data()

    X=[]
    for data in dataset:
        X.append(data['nut']) #get the number of reported items as "X"

    Y=[]
    for data in dataset:
        Y.append(data['DOI']) #get the DOI of papers as "Y"

    plt.barh(Y, X, color='blue') # develop the bar graph (横向)
    plt.title('Highest reporting completeness') #set title
    plt.xlabel("STROBE-nut items reported(n)") #set label of axis x
    plt.ylabel("DOI") #set label of axis y

    plt.xlim(0,24) # set the length of axis x

    for x, y in zip(X, range(len(Y))):
        plt.text(x+0.7, y-0.2, x)

    plt.show()

def min(n):

    from py2neo import Graph, Node, Relationship
    import matplotlib.pyplot as plt
    import matplotlib.ticker as ticker
    from IPython import get_ipython
    get_ipython().run_line_magic('matplotlib', 'inline')
    graph = Graph("http://localhost:7474", auth=("neo4j", ""))
    
    #count the number of STROBE-nut items reported per article
    query = """
    MATCH (article)-[r:`STROBE-nut`]->()-[*]->(n:`STROBE-nut item`)
    return article.DOI as `DOI`, count(*) as `nut` ORDER BY `nut` LIMIT %s
    """ %(n)

    dataset = graph.run(query).data()

    X=[]
    for data in dataset:
        X.append(data['nut']) #get the number of reported items as "X"

    Y=[]
    for data in dataset:
        Y.append(data['DOI']) #get the DOI of papers as "Y"

    plt.barh(Y, X, color='red') # develop the bar graph (横向)
    plt.title('Lowest reporting completeness') #set title
    plt.xlabel("STROBE-nut items reported(n)") #set label of axis x
    plt.ylabel("DOI") #set label of axis y

    plt.xlim(0,24) # set the length of axis x

    for x, y in zip(X, range(len(Y))):
        plt.text(x+0.7, y-0.2, x)

    plt.show()
    
def nut_max(number):

    from py2neo import Graph, Node, Relationship
    import matplotlib.pyplot as plt
    import matplotlib.ticker as ticker
    from IPython import get_ipython

    get_ipython().run_line_magic('matplotlib', 'inline')

    graph = Graph("http://localhost:7474", auth=("neo4j", ""))

    #count the number of STROBE-nut items reported per article
    query = """
    MATCH (article)-[r:`STROBE-nut`]->()-[*]->(n:`STROBE-nut item`)
    return n.item as `item`, count(*) as `nut` ORDER BY `nut` DESC LIMIT %s
    """%(number)

    dataset = graph.run(query).data()

    X=[]
    for data in dataset:
        X.append(data['nut']) #get the number of reported items as "X"

    Y=[]
    for data in dataset:
        Y.append(data['item']) #get the DOI of papers as "Y"

    plt.barh(Y, X, color='blue', ls='--', lw=2) # develop the bar graph (横向)
    plt.title('Highly reported STROBE-nut items') #set title
    plt.xlabel("Articles(n)") #set label of axis x
    plt.ylabel("STROBE-nut items") #set label of axis y

    plt.xlim(0,16) # set the length of axis x

    for x, y in zip(X, range(len(X))):
        plt.text(x+0.2, y-0.2, x)

    plt.show()
    
def nut_min(number):
    from py2neo import Graph, Node, Relationship
    import matplotlib.pyplot as plt
    import matplotlib.ticker as ticker
    from IPython import get_ipython

    get_ipython().run_line_magic('matplotlib', 'inline')

    graph = Graph("http://localhost:7474", auth=("neo4j", ""))
    
    #check the nut items not reported in any articles
    query = """
    MATCH (article)-[r:`STROBE-nut`]->()-[*]->(n:`STROBE-nut item`)
    return n.item as `item`, count(*) as `nut` ORDER BY `nut`
    """

    dataset = graph.run(query).data()

    X=[]
    Y=[]
    NUT=['nut-12.3','nut-8.4', 'nut-17', 'nut-12.1', 'nut-16', 'nut-8.3', 'nut-8.6', 'nut-5', 'nut-7.2', 'nut-11', 'nut-8.2', 'nut-12.2', 'nut-14', 'nut-20', 'nut-7.1', 'nut-13', 'nut-9', 'nut-22.2', 'nut-6', 'nut-19', 'nut-1', 'nut-8.5', 'nut-22.1', 'nut-8.1']

    for data in dataset:
        Y.append(data['item']) 

    if Y != NUT:
        Y = [item for item in NUT if not item in Y]
        Z=len(Y)
        number = number - Z
        for n in range(0,24):
            if Z != 0:
                X.append(0)
                Z=Z-1
            else:
                break
                
    #count the number of STROBE-nut items reported per article
    query = """
    MATCH (article)-[r:`STROBE-nut`]->()-[*]->(n:`STROBE-nut item`)
    return n.item as `item`, count(*) as `nut` ORDER BY `nut` LIMIT %s
    """%(number)

    dataset = graph.run(query).data()

    for data in dataset:
        X.append(data['nut']) #get the number of reported items as "X"

    for data in dataset:
        Y.append(data['item']) #get the DOI of papers as "Y"

    plt.barh(Y, X, color='red', ls='--', lw=2) # develop the bar graph (横向)
    plt.title('Rarely reported STROBE-nut items') #set title
    plt.xlabel("Articles(n)") #set label of axis x
    plt.ylabel("STROBE-nut items") #set label of axis y

    
    plt.xlim(0,16) # set the length of axis x
    
    for x, y in zip(X, range(len(X))):
        plt.text(x+0.1, y-0.2, x)

    plt.show()

def pie():

    from py2neo import Graph, Node, Relationship
    import matplotlib.pyplot as plt
    import matplotlib.ticker as ticker
    from IPython import get_ipython
    get_ipython().run_line_magic('matplotlib', 'inline')
    
    graph = Graph("http://localhost:7474", auth=("neo4j", ""))
    
    #count the number of STROBE-nut items reported per article
    query = """
    MATCH (article)-[r:`STROBE-nut`]->()-[*]->(n:`STROBE-nut item`)
    return article.DOI as `DOI`, count(*) as `nut` ORDER BY `nut`
    """

    dataset = graph.run(query).data()
    
    top=0
    high=0
    middle=0
    low=0
    for data in dataset:
        if data['nut'] >=18:
            top = top +1
        elif data['nut'] >=12:
            high = high +1
        elif data['nut'] >=6:
            middle = middle +1
        elif data['nut'] <6:
            low = low +1
    
    plt.figure(figsize=(6,9)) #figure size
    labels = [u'≥75% items reported',u'≥50% items reported',u'≥25% items reported',u'<25% items reported'] #set labels
    sizes = [top,high,middle,low] # set values
    colors = ['skyblue','lightgreen','yellow','red'] #set colors
    explode = (0,0,0,0.5) #separate one part from the rest parts 
    patches,text1,text2 = plt.pie(sizes,
                          explode=explode,
                          labels=labels,
                          colors=colors,
                          autopct = '%3.0f%%', #a fixed number of decimal places
                          shadow = False,
                          startangle =90, #Counterclockwise
                          pctdistance = 0.6) #the distance between values and the circle center
    
    plt.title('Overall reporting completeness of all papers') #set title
    plt.axis('equal')
    plt.legend()
    plt.show()

def article(DOI):
    import pygal
    from pygal.style import Style
    from py2neo import Graph, Node, Relationship
    
    graph = Graph("http://localhost:7474", auth=("neo4j", ""))
    #Overall
    query = """
    MATCH (article{DOI:'%s'})-[*]->(section:`STROBE-nut section`)-[*]->(n:`STROBE-nut item`)
    return count(n.name)
    """ %(DOI)
    dataset = graph.run(query).data()
    if dataset == []:
        Overall=0
    else:
        Overall=0.5*(dataset[0]['count(n.name)'])/24*100

    #Title/Abstract
    query = """
    MATCH (article{DOI:'%s'})-[*]->(section:`STROBE-nut section`{name:'Title/Abstract'})-[*]->(n:`STROBE-nut item`)
    return section.name, count(n.name)
    """ %(DOI)
    dataset = graph.run(query).data()
    if dataset == []:
        Title=0
    else:
        Title=0.5*(dataset[0]['count(n.name)'])*100

    #Methods
    query = """
    MATCH (article{DOI:'%s'})-[*]->(section:`STROBE-nut section`{name:'Methods'})-[*]->(n:`STROBE-nut item`)
    return section.name, count(n.name)
    """ %(DOI)
    dataset = graph.run(query).data()
    if dataset == []:
        Methods=0
    else:
        Methods=0.5*(dataset[0]['count(n.name)'])/15*100

    #Results
    query = """
    MATCH (article{DOI:'%s'})-[*]->(section:`STROBE-nut section`{name:'Results'})-[*]->(n:`STROBE-nut item`)
    return section.name, count(n.name)
    """ %(DOI)
    dataset = graph.run(query).data()
    if dataset == []:
        Results=0
    else:
        Results=0.5*(dataset[0]['count(n.name)'])/4*100

    #Discussion
    query = """
    MATCH (article{DOI:'%s'})-[*]->(section:`STROBE-nut section`{name:'Discussion'})-[*]->(n:`STROBE-nut item`)
    return section.name, count(n.name)
    """ %(DOI)
    dataset = graph.run(query).data()
    if dataset == []:
        Discussion=0
    else:
        Discussion=0.5*(dataset[0]['count(n.name)'])/2*100

    #Other information
    query = """
    MATCH (article{DOI:'%s'})-[*]->(section:`STROBE-nut section`{name:'Other information'})-[*]->(n:`STROBE-nut item`)
    return section.name, count(n.name)
    """ %(DOI)
    dataset = graph.run(query).data()
    if dataset == []:
        info=0
    else:
        info=0.5*(dataset[0]['count(n.name)'])/2*100
    
    custom_style = Style(value_label_font_size=50, label_font_size=20)
    radar_chart = pygal.Radar(style=custom_style)
    radar_chart.title = 'Reporting completeness of article (in %)'
    radar_chart.x_labels = ['Overall', 'Title/Abstract', 'Methods', 'Results', 'Discussion', 'Other information']
    radar_chart.add('STROBE-nut', [100, 100, 100, 100, 100, 100], show_dots=False)
    radar_chart.add(DOI, [Overall, Title, Methods, Results, Discussion, info], fill=True)
    #radar_chart.render_in_browser()
    radar_chart.render_to_png('/Users/chenyang/Desktop/strobenut.png')
