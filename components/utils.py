import PIL, PIL.ImageOps, PIL.ImageTk

def get_image_file(filename):
  img = None
  with open(filename, 'rb') as handle:
    img = PIL.Image.open(handle).convert('RGB')
  img = PIL.ImageOps.invert(img)
  return PIL.ImageTk.PhotoImage(img)
