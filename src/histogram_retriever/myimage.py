from PIL import Image
import numpy as np

class MyImage:
  def __init__(self, name="input.png", histogram=None, hist_alt=None, img=None, img_alt=None,
               path="/home/francisco/histogram-retriever/input/input.png") -> None:
    self.name = name
    self.path = path  # path to input folder with the target image
    self.img = np.array(Image.open(self.path))
    self.histogram = np.zeros((256, 3))
    self.hist_alt = np.zeros((256, 3), dtype= int)

  def test_print(self):
    print(self.img)

  def make_histogram(self):
    print(np.shape(self.img))
    print(np.shape(self.histogram))

    for i in range(self.img[:,:,0].size):
      self.histogram[self.img.flat[i]][0] += 1
    for i in range(self.img[:,:,1].size):
      self.histogram[self.img.flat[i]][1] += 1
    for i in range(self.img[:,:,2].size):
      self.histogram[self.img.flat[i]][2] += 1
    
    # for i in np.nditer(self.img[:,:,2]):
    #   self.histogram[i][2] += 1

  
img1 = MyImage()
img1.make_histogram()

print(img1.img[:,:,0])
print(img1.histogram[:,0])