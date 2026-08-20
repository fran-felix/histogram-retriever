import os
from histogram_retriever.myimage import MyImage
import numpy as np

class LikenessArray:

  def __init__(self, length, array=None):
    self.length = length
    self.array = np.array((self.length, 3)) # 3 dimensions: file name (0), class (1) and likeness (2)(distance)

class MyDataset:

  def __init__(self, like_array=None, path='/home/francisco/histogram-retriever/Vistex/', path_info='/home/francisco/histogram-retriever/info/info.txt'):
    self.path = path
    self.path_info = path_info

  def build_dataset(self):
    files = [f for f in os.listdir(self.path) if f.endswith('png')]
    n = len(files)

    self.like_array = LikenessArray(n)

    for i in range(n):
      path_img = os.path.join(self.path, files[i])
      img = MyImage(name=files[i],path=path_img)

      # Writes to info.txt all histograms and metadata to compare later
      # Some images are RGB and some are RGBA
      with open(self.path_info, "a") as f:
        write = "N " + files[i] + "\nH\n"
        f.write(write)

        channels = ["R", "G", "B"]
        if img.img.shape[2] == 4:
          channels.append("A")

        for ch_index, ch_name in enumerate(channels):
          f.write(f"{ch_name} ")
          img.histogram.hist[:,ch_index].tofile(f, " ", "%s")
          f.write("\n")

        f.write("\n")


data = MyDataset()
data.build_dataset()