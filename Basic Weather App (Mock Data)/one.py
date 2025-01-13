import random

def get_wather(city):
    weather_data={
        "temperature":random.randint(-10,40),
        "humadity":random.randint(20,100),
        "condition":random.choice(["rainy","cloudy","sunny","snow_fall","gand_fatat_le_thandi_ahe"])
    }
    return weather_data

def display_weather(city,weather):
    print(f"weather update :{city.capitalize()}")
    print(f"Temperature:{weather['temperature']}")
    print(f"Humadity:{weather['humadity']}")
    print(f"Condition:{weather['condition']}")
    
def main():
    print("Welcome to the temperature checking application") 
    while True:
        city=input("Enter the city name that you have to check the wather:") 
        if city.lower()=="exit":
            print("thanks for using this app i hope you got an better infomation about the city weather...")
            break
        elif city=="":
            print("Enter the city name properly it coudent be empty:")
            continue
        weather=get_wather(city)
        display_weather(city,weather)    
if __name__=="__main__":
    main()          