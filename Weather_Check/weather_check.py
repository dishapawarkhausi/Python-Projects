import requests
import os
from dotenv import load_dotenv
import tkinter as tk
from tkinter import messagebox

load_dotenv()

def get_weather(city):
    api_key  = os.getenv("OPENWEATHER_API_KEY")
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q" : city,
        "appid" : api_key,
        "units" : "metric"   # Use 'imperial' for Fahrenheit
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        wind_speed_mps = data["wind"]["speed"]
        wind_speed_kmph = wind_speed_mps * 3.6
        weather = {
            "city" : data["name"],
            "temperature" : data["main"]["temp"],
            "description" : data["weather"][0]["description"],
            "humidity" : data["main"]["humidity"],
            "wind_speed_kmph" : round(wind_speed_kmph, 2)
        }
        return weather
    else:
        return {"error" : "City not found"}

def show_weather():
    city = city_entry.get()
    weather = get_weather(city)
    if "error" in weather:
        messagebox.showerror("Error", weather["error"])
    else:
        result_label.config(text=f"Weather in {weather['city']}:\n"
                                f"Temperature: {weather['temperature']}°C\n"
                                f"Description: {weather['description']}\n"
                                f"Humidity: {weather['humidity']}%\n"
                                f"Wind Speed: {weather['wind_speed_kmph']} km/h")

root = tk.Tk()
root.title("Weather App")

title_label = tk.Label(root, text="Welcome to the Weather App!", font=("Helvetica", 14))
title_label.pack(pady=10)

city_label = tk.Label(root, text="Enter the name of a city:", font=("Helvetica", 12))
city_label.pack(pady=5)

city_entry = tk.Entry(root, font=("Helvetica", 12), width=20)
city_entry.pack(pady=5)

search_button = tk.Button(root, text="Get Weather", font=("Helvetica", 12), command=show_weather)
search_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=10)

root.mainloop()
