import requests
def kelvin_to_celcius(kelvin_temperature):
    return kelvin_temperature - 273.15

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    parameters = {"q": city, "appid": api_key}
    try:
        response = requests.get(base_url, parameters)
        data = response.json()

        if response.status_code == 200:
            temperature_kelvin = data['main']['temp']
            temperature_celcius=kelvin_to_celcius(temperature_kelvin)
                                                  
            print(f"Weather in {city}:")
            print(f"Temperature:{temperature_celcius:.2f}°C")
            print(f"Description: {data['weather'][0]['description']}")
            print(f"Humidity: {data['main']['humidity']}%")
        else:
            print(f"Error: {data['message']}")
        # Assuming 'data' contains the API response
        if 'rain' in data:
            precipitation = data['rain']
            print(f"Precipitation: {precipitation} mm")
        else:
            print("No precipitation data available.")
    

    except requests.RequestException as e:
        print(f"Error connecting to the API: {e}")

    
if __name__ == "__main__":
    city = input("Enter the city name: ")
    api_key = "b3476aa6dd48576e5fb7885de5f7d364"

    get_weather(api_key, city)  
    
