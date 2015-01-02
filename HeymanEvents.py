import bs4
import requests

root_url = 'http://heymancenter.org/events'
index_url = root_url + '/semester/spring-2015/'

def get_event_page_urls():
	response = requests.get(index_url)
	soup = bs4.BeautifulSoup(response.text)
	resultEvents = [a.attrs.get('href') for a in soup.select('div.topic a[href*="/events"]') ]
	return resultEvents

def get_event_data(event_page_urls):
	

print get_event_page_urls()