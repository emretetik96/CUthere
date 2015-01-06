import bs4
import requests
from datetime import datetime

ROOT_URL = 'http://heymancenter.org/events'
INDEX_URL = ROOT_URL + '/semester/spring-2015/'
ORGANIZATION_TITLE = 'Heyman Center for the Humanities'

#scrapes the URLs of single event pages from the INDEX_URL page
def get_event_page_urls():
	response = requests.get(INDEX_URL)
	soup = bs4.BeautifulSoup(response.text)
	resultEvents = [a.attrs.get('href') for a in soup.select('div.topic a[href*="/events"]') ]
	return resultEvents


#returns the data of the event whose page URL is passed as a parameter;
#returns the data in the form of a dictionary
def get_event_data(event_page_url):
	event_data = {}
	response = requests.get(event_page_url)
	soup = bs4.BeautifulSoup(response.text)
	event_data['event_title'] = soup.select('div.heading span[itemprop="name"]')[0].get_text()
	event_data['organization_title'] = ORGANIZATION_TITLE
	event_data['location'] = soup.select('span[itemprop="location"]')[0].get_text()
	#reading multiple paragraphs into a single dictionary value matched to the
	#'event_description' key
	event_data['event_description'] = ''
	for paragraph in soup.select('div[itemprop="description"] p'):
		event_data['event_description'] += paragraph.get_text()
	#separates date and time as two different values to be passed into the 
	#get_datetime_object function. The result of this call is datetime object,
	#which is stored in the event_data dictionary, with a key of 'date'
	dateTimeTogether = soup.select('em.date')[0].get_text()
	if (dateTimeTogether.endswith('am') or dateTimeTogether.endswith('pm')):
		timeIndex = dateTimeTogether.find(':') - 2
		date_string = dateTimeTogether[:timeIndex]
		time_string = dateTimeTogether[timeIndex:]
		event_data['date'] = get_datetime_object(date_string, time_string)
	else:
		date_string = dateTimeTogether
		event_data['date'] = get_datetime_object(date_string)
	return event_data


def get_datetime_object(date_string, time_string='none'):	
	year = int(date_string[-5:])
	if "Jan" in date_string:
		month = 1	
	if "Feb" in date_string:
		month = 2
	if "Mar" in date_string:
		month = 3	
	if "Apr" in date_string:
		month = 4
	if "May" in date_string:
		month = 5
	stringIndexAfterDay = date_string.rfind(',')		
	day = int(date_string[stringIndexAfterDay-2 : stringIndexAfterDay])
	if time_string != 'none':
		#set the hour and minute
		colon_index = time_string.find(':')
		if 'am' in time_string:
			#set the hour
			hour = int(time_string[colon_index-2 : colon_index])
		else:
			#set the hour 
			hour = int(time_string[colon_index-2 : colon_index]) + 12
			if hour == 24:
				hour = 12
		minute = int(time_string[colon_index+1 : colon_index+3])
		date = datetime(year, month, day, hour, minute)
	else:
		date = datetime(year, month, day)
	return date
	

#prints the information of each event on the INDEX_URL page; for testing purposes 
def show_event_info():
	event_page_urls = get_event_page_urls()
	for event_page_url in event_page_urls:
		print(get_event_data(event_page_url))

	
##for testing purposes
print('|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')			
show_event_info()
