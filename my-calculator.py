
import tkinter as tk
from tkinter import messagebox
import requests


# --- Weather Function ---
def get_weather():
    city = city_entry.get().strip()
    api_key = "YOUR_OPENWEATHER_API_KEY" 

    if not city:
        messagebox.showwarning("Warning", "First enter the name of the city!")
        return

    # OpenWeatherMap API URL
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            temp = data["main"]["temp"]
            weather_desc = data["weather"][0]["description"].capitalize()
            weather_label.config(
                text=f"Weather in {city.capitalize()}:\n{weather_desc}, {temp}°C"
            )
        else:
            weather_label.config(text="City nahi mili! Naam check karein.")
    except Exception as e:
        weather_label.config(text="Network / API Error!")


# --- Calculator Functions ---
def click_button(item):
    global expression
    expression += str(item)
    input_text.set(expression)


def clear_button():
    global expression
    expression = ""
    input_text.set("")


def evaluate_button():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except Exception:
        input_text.set("Error")
        expression = ""


# --- Main GUI Window ---
window = tk.Tk()
window.title("Calculator with Weather API")
window.geometry("380x520")
window.configure(bg="#222831")
window.expression = ""
input_text = tk.StringVar()

# --- Weather Section ---
weather_frame = tk.Frame(window, bg="#393E46", bd=5)
weather_frame.pack(fill="x", padx=10, pady=10)

city_label = tk.Label(
    weather_frame,
    text="Enter City:",
    bg="#393E46",
    fg="white",
    font=("Arial", 10, "bold"),
)
city_label.grid(row=0, column=0, padx=5, pady=5)

city_entry = tk.Entry(weather_frame, font=("Arial", 10), width=15)
city_entry.grid(row=0, column=1, padx=5, pady=5)

weather_btn = tk.Button(
    weather_frame,
    text="Get Weather",
    command=get_weather,
    bg="#00ADB5",
    fg="white",
    font=("Arial", 9, "bold"),
)
weather_btn.grid(row=0, column=2, padx=5, pady=5)

weather_label = tk.Label(
    weather_frame,
    text="Weather details will show here!",
    bg="#393E46",
    fg="#EEEEEE",
    font=("Arial", 10),
)
weather_label.grid(row=1, column=0, columnspan=3, pady=5)

# --- Calculator Display ---
display_frame = tk.Frame(window, bg="#222831")
display_frame.pack(fill="x", padx=10, pady=5)

input_field = tk.Entry(
    display_frame,
    textvariable=input_text,
    font=("Arial", 18, "bold"),
    fg="white",
    bg="#393E46",
    bd=10,
    justify="right",
)
input_field.pack(fill="x")

# --- Calculator Buttons ---
buttons_frame = tk.Frame(window, bg="#222831")
buttons_frame.pack(pady=10)

buttons = [
    ("7", 1, 0),
    ("8", 1, 1),
    ("9", 1, 2),
    ("/", 1, 3),
    ("4", 2, 0),
    ("5", 2, 1),
    ("6", 2, 2),
    ("*", 2, 3),
    ("1", 3, 0),
    ("2", 3, 1),
    ("3", 3, 2),
    ("-", 3, 3),
    ("0", 4, 0),
    (".", 4, 1),
    ("=", 4, 2),
    ("+", 4, 3),
]

for text, row, col in buttons:
    if text == "=":
        btn = tk.Button(
            buttons_frame,
            text=text,
            width=5,
            height=2,
            bg="#0B7DBB",
            fg="white",
            font=("Arial", 12, "bold"),
            command=evaluate_button,
        )
    else:
        btn = tk.Button(
            buttons_frame,
            text=text,
            width=5,
            height=2,
            bg="#2C243A",
            fg="white",
            font=("Arial", 12),
            command=lambda t=text: click_button(t),
        )
    btn.grid(row=row, column=col, padx=5, pady=5)

clear_btn = tk.Button(
    buttons_frame,
    text="C",
    width=23,
    height=2,
    bg="#5D00FE",
    fg="white",
    font=("Arial", 12, "bold"),
    command=clear_button,
)
clear_btn.grid(row=5, column=0, columnspan=4, padx=5, pady=5)

window.mainloop()