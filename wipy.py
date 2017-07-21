'''

command line arguements :- 
	now	-	get todays weather update
	


'''

import urllib, urllib2, json
import os
import sys
from datetime import datetime

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'   # BLUE
    OKGREEN = '\033[92m'  # GREEN
    WARNING = '\033[93m'  # YELLOW
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

dir_path = os.path.expanduser('~')

def init_wipy():
	dirp = dir_path + "/.wipy"
	if not os.path.isdir(dirp):
		os.makedirs(dirp)

def query(location):
	url = "https://query.yahooapis.com/v1/public/yql?"
	query = "select * from weather.forecast where woeid in (select woeid from geo.places(1) where text='%s')" % location
	q_url = url + urllib.urlencode({'q': query}) + "&format=json"
	result = json.loads(urllib2.urlopen(q_url).read())
	return result
	

init_wipy()

args = sys.argv[1:]

date = str(datetime.now().date())
has_current_data = False
if not os.path.exists(dir_path + "/.wipy" + date):
	has_current_data = True
	
bc = bcolors()


result = query('Lucknow')
location_json = result['query']['results']['channel']['location']
wind_json = result['query']['results']['channel']['wind']
sun_json = result['query']['results']['channel']['astronomy']
atmos_json = result['query']['results']['channel']['atmosphere']


item_json = result['query']['results']['channel']['item']

condition_json = item_json['condition'];
forecast_array = item_json['forecast']


#       PRINT LOCATION		#

print "City - %s\nRegion - %s\nCountry - %s\n\n" % (location_json['city'], location_json['region'], location_json['country'])

#		PRINT WIND CONDITION		#

print "Wind Temp - %s F\nDirection - %s\nSpeed - %skmph\n\n" % (wind_json['chill'], wind_json['direction'], wind_json['speed'])

#		SUN SETTINGS			#

print "Sunrise - %s\nSunset - %s\n\n" % (sun_json['sunrise'], sun_json['sunset'])

#		ATMOSPHERE			#

print "Humidity - %s percent\nPressure - %s mb\nVisibility - %sm\n\n" % (atmos_json['humidity'], atmos_json['pressure'], atmos_json['visibility'])

#		WEATHER CONDITION		#

print "Weather Temp - %s F\nWeather - %s\n\n" % (condition_json['temp'], condition_json['text'])


#		FORECAST			#

print bc.OKBLUE + "Weather Forecast" + bc.ENDC + "\n"
for f in forecast_array:
	print "Date - %s %s\nHigh. Temp - %s\nLow. Temp - %s\nWeather - %s\n\n" % (f['date'], f['day'], f['high'], f['low'], f['text'])
