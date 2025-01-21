from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

# Initialize the Tkinter root window
root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)


# Function to fetch and display weather details
def getWeather():
    try:
        city = textfield.get().strip()
        if not city:
            raise ValueError("City name cannot be empty.")

        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        if location is None:
            raise ValueError("City not found.")

        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        if result is None:
            raise ValueError("Unable to determine timezone.")

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        # Weather API call
        api_key = "ceb2b94552741ec65d6f9c156d22436e"  # Replace with your API key
        api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        response = requests.get(api_url)
        response.raise_for_status()  # Raise HTTPError for bad responses

        json_data = response.json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp'] - 273.15)  # Convert Kelvin to Celsius
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        # Update UI with weather details
        t.config(text=f"{temp}°")
        c.config(text=f"{condition} | FEELS LIKE {temp}°")
        w.config(text=f"{wind} m/s")
        h.config(text=f"{humidity}%")
        d.config(text=description.capitalize())
        p.config(text=f"{pressure} hPa")

    except requests.exceptions.RequestException:
        messagebox.showerror("Weather App", "Error fetching data. Check your internet connection.")
    except ValueError as ve:
        messagebox.showerror("Weather App", str(ve))
    except Exception as e:
        messagebox.showerror("Weather App", f"An unexpected error occurred: {str(e)}")


# Search box
Search_image = PhotoImage(file="search.png")
myimage = Label(image=Search_image)
myimage.place(x=20, y=20)

textfield = tk.Entry(root, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white")
textfield.place(x=50, y=40)
textfield.focus()

Search_icon = PhotoImage(file="search_icon.png")
myimage_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather)
myimage_icon.place(x=400, y=34)

# Logo
Logo_image = PhotoImage(file="logo.png")
logo = Label(image=Logo_image)
logo.place(x=150, y=100)

# Bottom box
Frame_image = PhotoImage(file="box.png")
frame_myimage = Label(image=Frame_image)
frame_myimage.pack(padx=5, pady=5, side=BOTTOM)

# Time and weather details
name = Label(root, font=("arial", 15, 'bold'))
name.place(x=30, y=100)
clock = Label(root, font=("Helvetica", 20))
clock.place(x=30, y=130)

# Weather labels
label1 = Label(root, text="WIND", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label1.place(x=120, y=400)

label2 = Label(root, text="HUMIDITY", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label2.place(x=225, y=400)

label3 = Label(root, text="DESCRIPTION", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label3.place(x=430, y=400)

label4 = Label(root, text="PRESSURE", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label4.place(x=650, y=400)

# Weather data display
t = Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400, y=150)
c = Label(font=("arial", 15, 'bold'))
c.place(x=400, y=250)

w = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
w.place(x=120, y=430)

h = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
h.place(x=280, y=430)

d = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
d.place(x=450, y=430)

p = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
p.place(x=670, y=430)

# Run the application
root.mainloop()
