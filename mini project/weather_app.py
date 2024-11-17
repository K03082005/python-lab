from tkinter import *
from tkinter import ttk
import requests


def data_get():
    city = city_name.get()
    try:
        data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=929feb772af510db07354388cd926c98"
        ).json()
        w_label1.config(text=data["weather"][0]["main"])
        wd_label1.config(text=data["weather"][0]["description"])
        t_label1.config(text=f"{data['main']['temp'] - 273.15:.2f} °C")
        p_label1.config(text=f"{data['main']['pressure']} hPa")
    except KeyError:
        w_label1.config(text="N/A")
        wd_label1.config(text="Invalid City")
        t_label1.config(text="N/A")
        p_label1.config(text="N/A")


# Initialize window
window = Tk()
window.title("Weather App")
window.config(bg="#dff9fb")  # Light sky blue background
window.geometry("500x600")

# App title
title_label = Label(window, text="🌦️ Weather App 🌤️", font=("Helvetica", 30, "bold"), bg="#22a6b3", fg="white")
title_label.place(x=25, y=20, height=60, width=450)

# City dropdown
list_name = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", 
    "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir", 
    "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", 
    "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", 
    "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", 
    "Uttar Pradesh", "Uttarakhand", "West Bengal", "Andaman and Nicobar Islands", 
    "Chandigarh", "Dadra and Nagar Haveli", "Daman and Diu", "Lakshadweep", 
    "National Capital Territory of Delhi", "Puducherry"
]
city_name = StringVar()
city_label = Label(window, text="Select City:", font=("Helvetica", 16, "bold"), bg="#dff9fb", fg="#130f40")
city_label.place(x=25, y=100, height=30, width=150)

com = ttk.Combobox(
    window,
    values=list_name,
    font=("Helvetica", 16),
    textvariable=city_name,
    state="readonly"
)
com.place(x=180, y=100, height=30, width=295)

# Data display labels
data_frame = Frame(window, bg="#badc58", relief="solid", bd=1)  # Light green background
data_frame.place(x=25, y=160, height=350, width=450)

w_label = Label(data_frame, text="🌥️ Weather:", font=("Helvetica", 14), bg="#badc58", fg="#130f40")
w_label.place(x=20, y=20)
w_label1 = Label(data_frame, text="", font=("Helvetica", 14, "bold"), bg="#badc58", fg="#4834d4")
w_label1.place(x=150, y=20)

wd_label = Label(data_frame, text="📄 Description:", font=("Helvetica", 14), bg="#badc58", fg="#130f40")
wd_label.place(x=20, y=80)
wd_label1 = Label(data_frame, text="", font=("Helvetica", 14, "bold"), bg="#badc58", fg="#4834d4")
wd_label1.place(x=150, y=80)

t_label = Label(data_frame, text="🌡️Temperature:", font=("Helvetica", 14), bg="#badc58", fg="#130f40")
t_label.place(x=20, y=140)
t_label1 = Label(data_frame, text="", font=("Helvetica", 14, "bold"), bg="#badc58", fg="#4834d4")
t_label1.place(x=150, y=140)

p_label = Label(data_frame, text="🔽 Pressure:", font=("Helvetica", 14), bg="#badc58", fg="#130f40")
p_label.place(x=20, y=200)
p_label1 = Label(data_frame, text="", font=("Helvetica", 14, "bold"), bg="#badc58", fg="#4834d4")
p_label1.place(x=150, y=200)

# Fetch weather button
fetch_button = Button(
    window,
    text="Get Weather",
    font=("Helvetica", 16, "bold"),
    bg="#eb4d4b",  # Vivid red button
    fg="white",
    relief="raised",
    command=data_get
)
fetch_button.place(x=180, y=520, height=40, width=140)

window.mainloop()
