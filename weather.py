import config  # you will need a config file with variable api_key to function
import requests  # library to allow http requests
import sys  # Library to terminate program


def choose_city():
    value = (input("What city do you want to check the weather in?\n"))
    value = str(value)
    return value


def get_weather_details(city_value):
    city = city_value  # city for weather
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + config.api_key + "&units=metric"

    request = requests.get(url)  # assign request result to variable
    json = request.json()  # result is a json file, assign to variable
    description = json.get("weather")[0].get("description")  # get description value from key weather at list 0
    temp = json.get("main").get("temp")  # get temp value from key main

    return {'city': city, 'temp': temp, 'description': description}  # return values needed as a dictionary


def main():
    city = choose_city()
    weather_dict = get_weather_details(city)  # create dictionary with above function
    print("The temp in", weather_dict['city'], "is", weather_dict['temp'], "Celsius", "with", weather_dict['description'])


while True:  # infinite loop
    main()
    while True:
        run_again = str(input('Run again? (y/n): '))
        run_again = run_again.lower()
        if run_again == 'y':
            break
        elif run_again == 'n':
            print("Goodbye")
            sys.exit()
        else:
            print("invalid input.")
