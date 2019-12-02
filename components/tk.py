from weather.display import DisplayWeather
from tkinter import Tk
root = Tk()
root.configure(bg='black')
weather = DisplayWeather(root=root)
root.mainloop()

