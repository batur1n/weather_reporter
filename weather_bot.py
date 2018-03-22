# -*- coding: utf-8 -*-

import json 
import urllib2

API_KEY = "############" # http://api.wunderground.com/weather/api
TEMP_URL = "http://api.wunderground.com/api/{}/geolookup/conditions/forecast/q/Ukraine/Kiev.json".format(API_KEY)
ASTR_URL = "http://api.wunderground.com/api/{}/astronomy/q/Ukraine/Kiev.json".format(API_KEY)


temp_response = urllib2.urlopen(TEMP_URL)
json_string = temp_response.read()
parsed_json = json.loads(json_string)
location = parsed_json['location']['city']
temp_c = parsed_json['current_observation']['temp_c']
weather = parsed_json['current_observation']['weather']
print u"Current weather conditions in %s: %s, %s°C." % (location, weather, temp_c)
temp_response.close()

astr_response = urllib2.urlopen(ASTR_URL)
json_string2 = astr_response.read()
parsed_json2 = json.loads(json_string2)
illumintaion = parsed_json2['moon_phase']['percentIlluminated']
moonage = parsed_json2['moon_phase']['ageOfMoon']
moon = "unknown"
if int(moonage) >= 14:
    moon = "Waning"
else:
    moon = "Waxing"
status = "unknown"
if int(illumintaion) >= 50:
    status = "Gibbous"
else:
    status = "Crescent"
sunrise_time = parsed_json2['moon_phase']['sunrise']['hour'] + ":" + parsed_json2['moon_phase']['sunrise']['minute']
sunset_time  = parsed_json2['moon_phase']['sunset']['hour'] + ":" + parsed_json2['moon_phase']['sunset']['minute']
astr_response.close()

print "Sunrise at: %s, sunset at: %s. Moon is %s %s (%s%% illumination)." % (sunrise_time, sunset_time, moon, status, illumintaion)


