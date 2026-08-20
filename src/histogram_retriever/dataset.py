import os
from histogram_retriever.myimage import MyImage
import numpy as np

class LikenessArray:

  def __init__(self, length):
    self.length = length
    self.names = np.zeros(length,dtype=str) # 0
    self.classes = np.zeros(length,dtype=int) # 1
    self.likeness = np.zeros(length) # 2
    self.array = [self.names, self.classes, self.likeness]

  def sort_likeness(self):
    order = np.argsort(self.array[2])
    self.names, self.classes, self.likeness = [arr[order] for arr in self.array]
    self.array = [self.names, self.classes, self.likeness]

class MyDataset:

  def __init__(self, input_img=MyImage(), like_array=None, path='/home/francisco/histogram-retriever/Vistex/', path_info='/home/francisco/histogram-retriever/info/info.txt'):
    self.input_img = input_img
    self.path = path
    self.path_info = path_info

  def build_dataset(self):
    files = [f for f in os.listdir(self.path) if f.endswith('png')]
    n = len(files)

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

  def build_likeness_array(self):
    files = [f for f in os.listdir(self.path) if f.endswith('png')]
    n = len(files)
    self.like_array = LikenessArray(n)

    for i in range(n):
      path_img = os.path.join(self.path, files[i])
      img = MyImage(name=files[i],path=path_img)

      # Images must have same shape (RBG and RGB, RGBA and RGBA)
      if img.img.shape[2] != self.input_img.img.shape[2]:
        raise RuntimeError("Images must be both RGB or RGBA.")
      likeness = np.linalg.norm(img.histogram.hist - self.input_img.histogram.hist)
      self.like_array.array[0][i] = img.name
      self.like_array.array[1][i] = img.get_class_id()
      self.like_array.array[2][i] = likeness

    self.like_array.sort_likeness()

  def closest(self, k=5):
    if self.like_array is None:
      raise RuntimeError("Likeness array contains null values, build it first.")

    k = min(k, self.like_array.length)
    return [closest[:k] for closest in self.like_array.array]