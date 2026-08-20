import os
import numpy as np
from PIL import Image
from histogram_retriever.myimage import MyImage


class MyDataset:

  def __init__(self, path='/home/francisco/histogram-retriever/Vistex/', path_info='/home/francisco/histogram-retriever/info/info.txt'):
    files = [f for f in os.listdir(path) if f.endswith('png')]
    n = len(files)

    for i in range(n):
      path_img = os.path.join(path, files[i])
      img = MyImage(name=files[i],path=path_img)
      img.make_histogram()

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
          img.histogram[:,ch_index].tofile(f, " ", "%s")
          f.write("\n")

        f.write("\n")


data = MyDataset()