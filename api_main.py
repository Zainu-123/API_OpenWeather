"""Importing the necessary libraries"""
import datetime as dt
import requests

"""Assigning the API Key of the user to a variable"""


with open('api_key.txt', 'r') as f:
    api_key = f.read().strip()

"""Defining a function to retrieve weather information"""

def weather_info(api_key,location, data_weather):
    url=f'http://api.openweathermap.org/data/2.5/weather?q={location}&APPID={api_key}'

    """Catching an exception for a wrong URL"""
    
    try:
        response=requests.get(url)
    except requests.ConnectionError:
        return 1
    
    """Catching an exception for Invalid Location"""
    try:
        result=response.json()
        temperature = result['main']['temp']
        humidity=result['main']['humidity']
        weather= result['weather'][0]['description']
        data_weather.append(temperature)
        data_weather.append(humidity)
        data_weather.append(weather)
    except:
        return 2
                
"""Defining main function"""

def main():
    location= input("Enter the location as in State,Country for which the weather information is required : ")
    data_weather = []
    ret = weather_info(api_key, location, data_weather)
    if(ret == 1):
        print('URL Invalid')
    elif (ret == 2):
        print('Invalid Location')
    else:
        print(f'The temperature of {location} is :',data_weather[0])
        print(f'The humidity of {location} is: ', data_weather[1])
        print(f'{location} seems to have {data_weather[2]} at the moment')
        
        
if __name__ == "__main__":
    main()

                
                            
                    
                
                     
    
                
            

    
   
            
        
            
             

    




