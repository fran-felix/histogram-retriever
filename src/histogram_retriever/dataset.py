import os
from histogram_retriever.myimage import MyImage
import numpy as np

class LikenessArray:

  def __init__(self, length, array=None):
    self.length = length
    self.array = np.array((self.length, 3)) # 3 dimensions: file name (0), class (1) and likeness (2)(distance)

class MyDataset:

  def __init__(self, input_img=MyImage(), like_array=None, path='/home/francisco/histogram-retriever/Vistex/'):
    self.path = path

  def build_dataset(self, path_info='/home/francisco/histogram-retriever/info/info.txt'):
    files = [f for f in os.listdir(self.path) if f.endswith('png')]
    n = len(files)

    self.like_array = LikenessArray(n)

    for i in range(n):
      path_img = os.path.join(self.path, files[i])
      img = MyImage(name=files[i],path=path_img)

      # Writes to info.txt all histograms and metadata to compare later
      # Some images are RGB and some are RGBA
      with open(path_info, "a") as f:
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

      # compare input_img to img
      # add result to likeness array

    # sort likeness array based on distance

    # parar de preguiça e fazer uma função de leitura pro arquivo

data = MyDataset()
data.build_dataset()