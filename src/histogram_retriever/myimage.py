from PIL import Image
import numpy as np

class MyImage:
  def __init__(self, name="input.png", histogram=None, hist_alt=None, img=None, img_alt=None,
               path="/home/francisco/histogram-retriever/input/input.png") -> None:
    self.name = name
    self.path = path  # path to input folder with the target image
    self.img = Image.open(self.path)
    self.img = np.array(self.img)

  def test_print(self):
    print(self.img)
  

  
    