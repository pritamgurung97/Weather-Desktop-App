import tkinter as tk
from Weather import current_temp
import math
from PIL import Image, ImageTk

def update_temperature_label():
    current_temperature_celsius = math.ceil(current_temp())
    temperature_label.config(text=f"{current_temperature_celsius}°C")
    window.after(600000, update_temperature_label)  # Update temperature every 10 minutes

# Main GUI window
window = tk.Tk()
window.title('Weather App')
window.geometry('400x200')

# Open the JPEG image using Pillow
background_image = Image.open('static/images/bg.png')

# Convert the image to PhotoImage using ImageTk
background_photo = ImageTk.PhotoImage(background_image)

# Create a label to hold the background image
background_label = tk.Label(window, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Label for "Dublin"
dublin_label = tk.Label(window, text="Dublin", font=('Helvetica', 30), bg='white', fg='#333333')
dublin_label.pack(pady=20)

# Label for "Current Weather"
current_weather_label = tk.Label(window, text="Current Weather", font=('Helvetica', 14), bg='white', fg='#555555')
current_weather_label.pack()

# Label for the current temperature
current_temperature_celsius = math.ceil(current_temp())
temperature_label = tk.Label(window, text=f"{current_temperature_celsius}°C", font=('Helvetica', 60), bg='white', fg='#0099FF')
temperature_label.pack()

# Update temperature label every 10 minutes
update_temperature_label()

window.mainloop()
