import pyowm
from Tkinter import *

owm = pyowm.OWM('YOUR_KEY') 

def printtext():
   global e
   string = e.get()
   observation = owm.weather_at_place(string)
   l = observation.get_location()
   loc_name = l.get_name()
   w = observation.get_weather()
   time = w.get_reference_time(timeformat='iso')
   sunrise = w.get_sunrise_time('iso')
   sunset = w.get_sunset_time('iso')
   rain = w.get_rain()
   rain_check = len(rain)
   status = w.get_status()

   # Weather details
   wind = w.get_wind()                  
   humidity = w.get_humidity()             
   temp = w.get_temperature('celsius')  
   values = wind.values()
   temps = temp.values()

   #displaying output
   root = Tk()
   text = Text(root)
   text.insert(INSERT, "Location :" + str(loc_name) + "\n")
   text.insert(INSERT, "Reference Time :" + str(time) + "\n")
   text.insert(INSERT, "Current status :" + str(status) + "\n")
   text.insert(INSERT, "Sunrise Time :" + str(sunrise) + "\n")
   text.insert(INSERT, "Sunset Time :" + str(sunset) + "\n")
   if(rain_check != 0):
      text.insert(INSERT, "Rain volume :" + str(rain) + "\n")
   text.insert(INSERT,"wind speed :" + str(values[0]) + "\n")
   text.insert(INSERT,"Humidity :" + str(humidity) + "\n")
   text.insert(INSERT,"MAX Temprature :" + str(temps[0]) + "\n")
   text.insert(INSERT,"MIN Temprature :" + str(temps[2]) + "\n")
   text.pack()
   root.mainloop()

# getting value from user
root = Tk()
e = Entry(root)
L1 = Label(root, text="Enter location")
L1.pack( side = LEFT)
e.pack()
e.focus_set()

b = Button(root,text='submit',command=printtext)
b.pack(side='bottom')
root.mainloop()
