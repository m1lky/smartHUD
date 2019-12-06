import PIL, PIL.ImageOps, PIL.ImageTk, PIL.Image

def get_image_file(filename):
  img_temp = None
  with open(filename, 'rb') as handle:
    img = PIL.Image.open(handle)
    img_temp = img.resize((250, 250), PIL.Image.BILINEAR, quality=100)
    img_temp = PIL.ImageOps.invert(img_temp.convert('RGB'))
  return PIL.ImageTk.PhotoImage(img_temp)
