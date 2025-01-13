import random

def check_weather(city):
    wethere_data={
        "temperature":random.randint(-10,40),
        "humadity":random.randint(0,100),
        "condition":random.choice(["Sunny", "Cloudy", "Rainy", "Windy", "Snowy"])
    }
    return wethere_data

def display_weather(city,weather):
    print(f"\nWeather Update for {city.capitalize()}:")
    print(f"Temperature: {weather['temperature']}°C")
    print(f"humadity: {weather['humadity']}%")
    print(f"Condition: {weather['condition']}")
    
def main():
    print(f"welcome to the temperature checking application ")
    while True:
        city=input("Enter the city name that you have to check the Weather:")    
        if city.lower()=="exit":
            print("thanks for using this appplication i hope you got a better information about the city..")
            break
        elif city=="":
            print("the city should not be empty pliz enter the city name")
            continue
        
        weather=check_weather(city)
        display_weather(city,weather)
        
if __name__=="__main__":
    main()                