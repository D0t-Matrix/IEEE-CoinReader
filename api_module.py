import pyaztro # import for the module for the horoscope
import urllib.request # import for the HTTP GET responses
import json # import json handling

"""To utilize this class, add the following line to your imports
from api_module import API_Calls
"""

class API_Calls(object):
    """Class to hold all API calls for the project
    
    Designed and written by: Dominic Kenney
    Project: Horoscope Coin Reader
    Team: IEEE - Amanda Shultz
    Year: 2019 - 2020
    """

    def get_advice(self) -> str:
        """Returns a random piece of advice as a string"""
        advice_uri = 'https://api.adviceslip.com/advice' # url for the random advice
        return ((self.__json_grabber(advice_uri))["slip"]["advice"]) # returns the advice string from the json object

    def __json_grabber(self, uri: str) -> json:
        """Helper method to grab and return the JSON object from the given URI's HTTP call """
        data = urllib.request.urlopen(uri)  # grabs the response from the HTTP call
        return json.loads(data.read()) # turns the response into valid json data

    def __horoscope_grab(self, _sign: str) -> str:
        """Helper method to grab the horoscope data for the given star sign"""
        return pyaztro.Aztro(sign = _sign) # returns the horoscope object with the data loaded

    def get_horoscope_description(self, _sign: str) -> str:
        """Returns the description of the given star sign. Takes input string of sign in lowercase"""
        return self.__horoscope_grab(_sign).description # returns the description as string

    def get_horoscope_mood(self, _sign: str) -> str:
        """Returns the mood of the given star sign. Takes input string of sign in lowercase"""
        return self.__horoscope_grab(_sign).mood # returns the mood as string

    def get_horoscope_lucky_number(self, _sign: str) -> str:
        """Returns the lucky number of the given star sign. Takes input string of sign in lowercase"""
        return self.__horoscope_grab(_sign).lucky_number # returns the lucky number as string

    def get_horoscope_lucky_time(self, _sign: str) -> str:
        """Returns the lucky number of the given star sign. Takes input string of sign in lowercase"""
        return self.__horoscope_grab(_sign).lucky_time # returns the lucky number as string

    def get_fact(self) -> str:
        """Grabs and returns a random useless fact as a string"""
        fact_uri = 'https://uselessfacts.jsph.pl/random.json?language=en' # url for the random fact
        return ((self.__json_grabber(fact_uri))["text"]) # returns the fact string from the json object
