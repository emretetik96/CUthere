import bs4
import requests

ROOT_URL = 'http://heymancenter.org/events'
INDEX_URL = ROOT_URL + '/semester/spring-2015/'
ORGANIZATION_TITLE = 'Heyman Center for the Humanities'

def get_event_page_urls():
	response = requests.get(INDEX_URL)
	soup = bs4.BeautifulSoup(response.text)
	resultEvents = [a.attrs.get('href') for a in soup.select('div.topic a[href*="/events"]') ]
	return resultEvents

def get_event_data(event_page_url):
	event_data = {}
	response = requests.get(event_page_url)
	soup = bs4.BeautifulSoup(response.text)
	event_data['title'] = soup.select('div.heading span[itemprop="name"]')[0].get_text()
	event_data['organization_title'] = ORGANIZATION_TITLE
	for key in event_data:
		return event_data

def show_event_info():
	event_page_urls = get_event_page_urls()
	for event_page_url in event_page_urls:
		print(get_event_data(event_page_url))

##for testing purposes
print('|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')			
show_event_info()