import bs4
import requests

root_url = 'http://heymancenter.org/events'
index_url = root_url + '/semester/spring-2015/'

def get_event_page_urls():
	response = requests.get(index_url)
	soup = bs4.BeautifulSoup(response.text)
	resultEvents = [a.attrs.get('href') for a in soup.select('div.topic a[href*="/events"]') ]
	return resultEvents

def get_event_data(event_page_url):
	event_data = {}
	response = requests.get(event_page_url)
	soup = bs4.BeautifulSoup(response.text)
	event_data['title'] = soup.select('div.heading span[itemprop="name"]')[0].get_text()
	for key in event_data:
		##print isinstance(event_data[key], unicode)
		return event_data[key]
		##event_data[key].encode('utf_8', 'ignore')
		##event_data[key] = event_data[key].decode('utf_8')		
	##return event_data.values()

def show_event_info():
	event_page_urls = get_event_page_urls()
	for event_page_url in event_page_urls:
		print(get_event_data(event_page_url))

##for testing purposes
print('|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')			
print(show_event_info())