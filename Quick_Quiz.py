import tkinter as tk
from tkinter import messagebox
import requests

def get_weather():
    city = city_entry.get().strip()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name!")
        return

    # 1. Geocoding API: Shehar ke name se Latitude & Longitude nikalna
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    
    try:
        geo_res = requests.get(geo_url).json()
        
        if "results" not in geo_res:
            result_label.config(text="City not found!", fg="red")
            return
            
        lat = geo_res["results"][0]["latitude"]
        lon = geo_res["results"][0]["longitude"]
        country = geo_res["results"][0].get("country", "")

        # 2. Weather API: Un coordinates se live weather lana
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        weather_res = requests.get(weather_url).json()
        
        current = weather_res["current_weather"]
        temp = current["temperature"]
        wind = current["windspeed"]

        # 3. GUI mein result update karna
        result_label.config(
            text=f"Location: {city.capitalize()}, {country}\n"
                 f"Temperature: {temp}°C\n"
                 f"Wind Speed: {wind} km/h",
            fg="green"
        )

    except Exception as e:
        messagebox.showerror("Error", "Network or API Error occurred!")

# --- GUI Window Configuration ---
root = tk.Tk()
root.title("Weather Checker")
root.geometry("350x280")
root.resizable(False, False)

# UI Elements
title_label = tk.Label(root, text="Live Weather App", font=("Arial", 14, "bold"))
title_label.pack(pady=10)

city_entry = tk.Entry(root, font=("Arial", 12), width=20)
city_entry.pack(pady=5)
city_entry.insert(0, "Faisalabad")  # Default city

search_btn = tk.Button(root, text="Get Weather", font=("Arial", 10, "bold"), bg="#4CAF50", fg="white", command=get_weather)
search_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 11), justify="center")
result_label.pack(pady=10)

# App Loop Start
root.mainloop()

