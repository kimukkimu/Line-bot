import requests


def weather_response():
    api_url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=130040'
    weather_date = requests.get(api_url).json()

    response = weather_date['title'] + '\n'
    for forecasts in weather_date['forecasts']:
        response += forecasts['dateLabel'] + 'の天気は、' + forecasts['telop'] + '\n'
    #return response

    return "成功！"
