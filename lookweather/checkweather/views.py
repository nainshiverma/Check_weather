from django.shortcuts import render

import requests



# Create your views here.
def weather(request):
    city = request.GET.get('city' , "Lucknow")
    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=257a08d84c0eed8d2fb4d89917a1a57e'
    data = requests.get(url).json()
    

    TodayWeather ={
        'city': data['name'] , 
        'weather':data['weather'][0]['main'] , 
        'icon':data['weather'][0]['icon'], 
        'kelvin_temperature':data['main']['temp'] ,
        'Celcius_temperature':int(data['main']['temp']-273) ,
        'pressure':data['main']['pressure'],
        'humidity':data['main']['humidity'],
        'description': data['weather'][0]['description']
         }
    
    context={'data' : TodayWeather}
    print(context)
    
    return render(request , 'weather.html' , context)


