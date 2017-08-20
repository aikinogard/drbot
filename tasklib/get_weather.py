import logging
import doctest
from weather import Weather

def FtoC(f):
    """convert Fahrenheit to Celsius
    >>> FtoC(68)
    20
    """
    return int((int(f) - 32) * 5. / 9)

def format_weather(info):
    """format weather
    >>> info = {'date': 'Sun, 20 Aug 2017 11:00 AM PDT',\
                'text': 'Mostly Sunny',\
                'code': '34',\
                'temp_c': '22',\
                'temp': '73'}
    >>> format_weather(info)
    'Sun, 20 Aug 2017 11:00 AM PDT\\n22C, Mostly Sunny'
    """
    line1 = info['date']
    line2 = str(info['temp_c']) + 'C, ' + info['text']
    return '\n'.join([line1, line2])

def get_weather(location):
    weather = Weather()
    info = weather.lookup_by_location(location).condition()
    info['temp_c'] = FtoC(info['temp'])
    return format_weather(info)

if __name__ == '__main__':
    doctest.testmod()