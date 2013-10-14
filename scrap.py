from urllib2 import urlopen
from bs4 import BeautifulSoup
import lxml

url = "http://finance.yahoo.com/q?s="

def get_category_links(quote):
    html = urlopen(url+quote).read()
    soup = BeautifulSoup(html,'lxml')
    data = soup.find('div', 'rtq_table')
    return data
  
print get_category_links('AAPL')