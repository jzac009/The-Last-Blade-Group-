import requests

# Function to fetch and display the weather
def get_weather(city):
    api_key = 'd8ddf9ff8dfc633d489d2576c7b5dd32'  #My OpenWeatherMap API key
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric' #the URL of the website


    # Send a GET request to the weather API
    response = requests.get(url)

    # Parse the JSON response
    data = response.json()

    # Check if the response contains valid data (status code 200)
    if data['cod'] == 200:
        # Extract weather and temperature data
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        print(f'Weather in {city}: {weather}, {temp}°C')
    else:
        print(f'City {city} not found.')


get_weather('Manila')  # Fetch and display the weather information for City.
