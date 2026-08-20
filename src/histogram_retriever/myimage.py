from PIL import Image
import numpy as np

class MyImage:
  def __init__(self, name="input.png", histogram=None, hist_alt=None, img=None, img_alt=None,
               path="/home/francisco/histogram-retriever/input/input.png") -> None:
    self.name = name
    self.path = path  # path to input folder with the target image
    self.img = np.array(Image.open(self.path))
    self.histogram = np.zeros((256, 3), dtype=int)
    self.hist_alt = np.zeros((256, 3), dtype=int)


  def make_histogram(self):
    print(np.shape(self.img))
    print(np.shape(self.histogram))

    for i in range(3):
      self.histogram[:,i], _ = np.histogram(self.img[:,:,i],bins=256,range=(0,255))

  
img1 = MyImage('''path="/home/francisco/histogram-retriever/Vistex/c001_001.png"''')
img1.make_histogram()