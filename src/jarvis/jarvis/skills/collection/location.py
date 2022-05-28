import requests
import json
import logging

from jarvis.settings import IPSTACK_API
from jarvis.skills.collection.internet import InternetSkills
from jarvis.skills.skill import AssistantSkill


class LocationSkill(AssistantSkill):

    @classmethod
    def get_current_location(cls, **kwargs):
        location_results = cls.get_location()
        if location_results:
            city, latitude, longitude = location_results
            cls.response("You are in {0}".format(city))
    
    @classmethod
    def get_location(cls):
        try:
            send_url = "http://api.ipstack.com/check?access_key=" + IPSTACK_API['key']
            geo_req = requests.get(send_url)
            geo_json = json.loads(geo_req.text)
            latitude = geo_json['latitude']
            longitude = geo_json['longitude']
            city = geo_json['city']
            return city, latitude, longitude
        except Exception as e:
            if InternetSkills.internet_availability():
                # If there is an error but the internet connect is good, then the location API has problem
                cls.console(error_log=e)
                logging.debug("Unable to get current location with error message: {0}".format(e))
                return None
