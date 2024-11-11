import requests
def api_for_weather(place):
    result = requests.get(
        ' http://api.openweathermap.org/data/2.5/weather?q='+place+'&appid=348faf3ed79a29bad44e712956cce9ec')
    data = result.json()
    return data

print(api_for_weather('ANANTAPUR'))