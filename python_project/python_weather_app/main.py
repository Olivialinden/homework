
import requests # making HTTP requests, including API requests.

def get_weather_data(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # get temperature in Celsius
    }

#is a dictionary containing parameters to be included in the API request. 
#These parameters include the city name, your API key, 
#and the desired units for temperature (metric in this case, which gives temperature in Celsius).

    response = requests.get(base_url, params=params)#sends a GET request to the API using the provided parameters.
    data = response.json() #stores the JSON response received from the API.
    return data

def main():
    api_key = "f9a3e719c679441b57d70f5aa006e293"
    city = input("Enter city name: ")

    while True:
        print("\nMenu:")
        print("1. Show Current Weather")
        print("2. Show Temperature")
        print("3. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            weather_data = get_weather_data(api_key, city)
            weather = weather_data["weather"][0]["description"]
            print(f"Current weather in {city}: {weather}")
        elif choice == "2":
            weather_data = get_weather_data(api_key, city)
            temp = weather_data["main"]["temp"]
            print(f"Temperature in {city}: {temp}°C")
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

