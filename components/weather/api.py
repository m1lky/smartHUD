import requests, json, datetime
WEATHER_API_KEY = '7aafe66c5304d686c762e97869c4f4fc'

#example format of call: 'https://api.forecast.io/forecast/APIKEY/LATITUDE,LONGITUDE,TIME'
#you can exclude time to get the current forecast for the next week
WEATHER_API_SITE = 'https://api.forecast.io/forecast/' + WEATHER_API_KEY + '/'


"""{'apparentTemperature': 15.98,
 'cloudCover': 0,
 'dewPoint': 7.92,
 'humidity': 0.71,
 'icon': 'clear-day',
 'ozone': 354.4,
 'precipIntensity': 0,
 'precipProbability': 0,
 'pressure': 1037.4,
 'summary': 'Clear',
 'temperature': 15.64,
 'time': 1574743236,
 'uvIndex': 1,
 'visibility': 10,
 'windBearing': 205,
 'windGust': 3.52,
 'windSpeed': 2.86}"""

def get_wind_direction(degrees):
    # The api gives directions in degrees, with 0 as nautical north
    if degrees > 338 or degrees <= 23:
        return 'North'
    elif degrees > 23 and degrees <= 68:
        return 'North East'
    elif degrees > 68 and degrees <= 113:
        return 'East'
    elif degrees > 113 and degrees <= 158:
        return 'South East'
    elif degrees > 158 and degrees <= 203:
        return 'South'
    elif degrees > 203 and degrees <= 248:
        return 'South West'
    elif degrees > 248 and degrees <= 293:
        return 'West'
    elif degrees > 293 and degrees <= 338:
        return 'North West'

DISPLAY_NAMES_MAP = {'apparentTemperature': 'Apparent Temp',
 # 'cloudCover': 'Cloud Cover',
 # 'dewPoint': 'Dew Point',
 'humidity': 'Humidity',
 'icon': 'icon', 
 # 'ozone': 'Ozone',
 # 'precipIntensity': 'Rain Intensity',
 'precipProbability': 'Rain Chance',
 # 'pressure': 'Pressure',
 'summary': 'Summary',
 # 'temperature': 'Temp',
 'time': 'Timestamp',
 # 'uvIndex': 'UV Index',
 # 'visibility': 'Visibility',
 # 'windBearing': 'Wind Direction',
 # 'windGust': 'Gusts',
 'windSpeed': 'Wind Speed'}

ICON_FILES = {
 'clear-day':'sunny',
 'clear-night':'sunny',
 'rain': 'rain',
 'snow': 'snow',
 'sleet': 'icey', 
 'wind': 'cloudy_day',
 'fog': 'cloudy_night',
 'cloudy': 'cloudy_day',
 'partly-cloudy-day': 'cloudy_day',
 'partly-cloudy-night': 'cloudy_night'
}

class Weather(object):
  """docstring for Weather"""
  def __init__(self, latitude=None, longitude=None, time=None):
    super(Weather, self).__init__()
    self.coordinates = (latitude, longitude)
    self.request_url = WEATHER_API_SITE + str(latitude) + ',' + str(longitude) 
  
  def get_weather(self):
    """Request the forecast from the weather API
    
    Returns:
        Dict|None: Response from api if successful else None
    """
    response = requests.get(self.request_url)
    if response.status_code == 200:
      self.last_response = response.json()
      return self.last_response
    return None

  def get_display_data(self, data=None):
    """Converts data or the last response from the api to a readable
       format suitable for use with tkinter
    Args:
        data (dict, optional): The weather api data to format
    
    Returns:
        dict: weather keys and values are human readable versions of data
    """
    data = data or self.last_response['currently']
    ret_val = {}
    for key, value in data.items():
      new_val = None
      if key in DISPLAY_NAMES_MAP:
        if key == 'windBearing':
          new_val = get_wind_direction(value)
        elif 'temp' in key.lower():
          new_val = str(round(value  * 5.0 / 9.0) + 32) + chr(176)
        elif key == 'time':
          new_val = datetime.datetime.fromtimestamp(value).strftime("%m/%d/%y %H:%M")
        elif key == 'icon':
          new_val = 'components/weather/assets/' + ICON_FILES[value] + '.gif'
        elif key == 'precipProbability':
          new_val = "{:,.2f}%".format(value)
        elif key in DISPLAY_NAMES_MAP.keys():
          new_val = value
        if new_val:
          ret_val[DISPLAY_NAMES_MAP[key]] = new_val
    return ret_val

  def get_weather_display_data(self):
    """Helper function to both get the data and return display version
    
    Returns:
        dict: same as get_display_data
    """
    self.get_weather()
    return self.get_display_data()