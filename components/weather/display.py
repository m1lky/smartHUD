import tkinter as tk
import PIL, PIL.ImageOps, PIL.ImageTk
from .api import Weather as api
from ..utils import get_image_file
from time import sleep
from ..display_base import DisplayBase
def _format_data_string(key, val):
  return key + ': ' + str(val)

class DisplayWeather(DisplayBase):
  """Creates the gui display for the weather"""
  def __init__(self, root, *args, **kwargs):
    self.root = super(DisplayWeather, self).__init__(root, *args, **kwargs)
    self.configure(background="black")
    #main area display
    self.api = api(latitude=42.401458, longitude=-71.126482)
    self.data_reference = self.place_vertical_dict(self.api.get_weather_display_data())
    self.after(1000, self.update_data())

  # def place_data(self, data):
  #   self._set_icon(data.get('icon'))
  #   self.message_boxes = []          
  #   # may have to put grid back here
  #   for row, key in enumerate(data):
  #     if key != 'icon':
  #       textvariable = tk.StringVar(value=_format_data_string(key, data[key]))
  #       message = tk.Label(self.root, textvariable=textvariable, width=50, background="black", fg="white", font=('Monospace', '25'), pady=5)
  #       self.message_boxes.append( (textvariable, message, key) )
  #       message.grid(row=(row % 2) + row + 2, column=1)

  def update_data(self):
    config = {}
    config['data_func'] = self.api.get_weather_display_data
    config['reference_index'] = self.data_reference
    self.update_vertical_dict(**config)
    # while True:
    #   self.api.get_weather()
    #   data = self.api.get_display_data()
    #   print(data)
    #   for textvariable, message, key in self.message_boxes:
    #     textvariable.set(_format_data_string(key, data[key]))
    #   self.update()
    #   sleep(900) # 15 minutes

  def _set_icon(self, icon):
    self.image_tk = get_image_file(icon)
    self.label_img = tk.Label(self.root, image=self.image_tk, background="black", fg="white")
    self.label_img.grid(row=1, column=1)
