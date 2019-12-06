import tkinter as tk
import PIL, PIL.ImageOps, PIL.ImageTk
from .utils import get_image_file
from time import sleep

def _format_data_string(key, val):
  return str(key) + ': ' + str(val)

class DisplayBase(tk.Frame):
  """Creates the gui display for the weather"""
  def __init__(self, root, *args, **kwargs):
    self.root = super(DisplayBase, self).__init__(root, *args, **kwargs)
    self.configure(background="black")
    self.images = []
    self.vertical_dicts = []
  
  def place_vertical_dict(self, data, row_func=None, col_func=None, root=None):
    """Place data in a downward stacking series of Labels
    
    Args:
        data (dict): data to be placed
    
    Returns:
        int: the index of DisplayBase.vertical_dicts that reference to the labels is stored at
    """
    root = root if root else self.root
    self.vertical_dicts.append([])
    if not row_func:
      def row_func(row):
        return (row % 2) + row + 2
    if not col_func:
      def col_func(row):
        return 1
    for row, key in enumerate(data):
      if key != 'icon':
        textvariable = tk.StringVar(value=_format_data_string(key, data[key]))
        message = tk.Label(root, textvariable=textvariable, width=50, background="black", fg="white", font=('Monospace', '25'), pady=5)
        self.vertical_dicts[-1].append( (textvariable, message, key) )
        message.grid(row=row_func(row), column=col_func(row))
    return len(self.vertical_dicts) - 1
  
  def update_vertical_dict(self, reference_index, data_func, *args, **kwargs):
    while True:
      data = data_func(*args, **kwargs)
      for textvariable, message, key in self.vertical_dicts[reference_index]:
        textvariable.set(_format_data_string(key, data[key]))
      self.update()
      sleep(900) # 15 minutes

  def place_image(self, path, row=1, column=1, root=None):
    image_tk = get_image_file(icon)
    self.images.append( (row, column, image_tk) )
    root = root if root else self.root
    self.label_img = tk.Label(root, image=image_tk, background="black", fg="white")
    self.label_img.grid(row=row, column=column)
