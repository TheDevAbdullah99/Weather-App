import requests
import json
import win32com.client as wincom

city = input("Enter the name of the city\n")

# Weather API URL (replace with your API key)
url = f"http://api.weatherapi.com/v1/current.json?key=12c408ccd3da46a9941133338250609&q={city}"

r = requests.get(url)
wdic = json.loads(r.text)

# Extract temperature
w = wdic["current"]["temp_c"]
print(w)

# Speak result
speaker = wincom.Dispatch("SAPI.SpVoice")
speaker.Speak(f"The current weather in {city} is {w} degrees Celsius")
