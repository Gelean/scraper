from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

# Functions taken from https://www.pybloggers.com/2018/01/practical-introduction-to-web-scraping-in-python/

def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)

def log_error(e):
    """
    It is always a good idea to log errors. 
    This function just prints them, but you can
    make it do anything.
    """
    print(e)

def http_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None
    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None

#raw_html = open('contrived.html').read()
#html = BeautifulSoup(raw_html, 'html.parser')
#for p in html.select('p'):
#    print ("Line:", p.text)
#    if p['id'] == 'walrus':
#        print(p.text)

raw_html = http_get('http://www.elderek.com/about.html')
#print(get(url_root))
html = BeautifulSoup(raw_html, 'html.parser')
#print(html)
#print(len(html))
for h1 in html.select('h1'):
    print("H1:", h1.text)
for h2 in html.select('h2'):
    print("H2:", h2.text)
for h3 in html.select('h3'):
    print("H3:", h3.text)
for p in html.select('p'):
    print("p:", p.text)
