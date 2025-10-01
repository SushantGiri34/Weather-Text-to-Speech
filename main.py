import win32com.client as wincom
import requests

city = input("Enter the name of the city: ")
api_key = "******************************"  # replace with your valid API key

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
r = requests.get(url)
data = r.json()

# Check if API call is successful
if r.status_code == 200 and "main" in data:
    w = data["main"]["temp"]
    speak = wincom.Dispatch("SAPI.SpVoice")
    text = f"The current weather in {city} is {w} degrees Celsius."
    print(text)
    speak.Speak(text)
else:
    # Print full response for debugging
    print(f"Error fetching weather for '{city}'. Response from API:")
    print(data)
