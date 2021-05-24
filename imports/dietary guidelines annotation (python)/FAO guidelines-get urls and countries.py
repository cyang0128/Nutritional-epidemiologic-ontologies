#get all the urls of all the countries
try:
    from urllib import request
except:
    from urllib2 import urlopen as request
    from urllib2 import Request
from bs4 import BeautifulSoup

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
}
url = "http://www.fao.org/nutrition/education/food-dietary-guidelines/home/en/"
m = request.urlopen(request.Request(url, headers=HEADERS)).read()
s = BeautifulSoup(m, "html.parser")
metadata = s.findAll("a", attrs={"class":"linkcountry"})
url_list =[]
country_list = []
for n_t in range(0,len(metadata)):
    url_list.append(metadata[n_t]['href'])
    country_list.append(metadata[n_t].get_text())

print("There are urls of "+ str(len(country_list))+" countries/areas.")
print("")
print("Country list:")
print(country_list)
print("")
print("url list:")
print(url_list)
