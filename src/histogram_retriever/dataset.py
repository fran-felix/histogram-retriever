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
      #img = np.array(Image.open(path_img))
      img = MyImage(name=files[i],path=path_img)

      # Writes to info.txt all histograms and metadata to compare later
      # instead of keeping it as a data structure in memory
      with open(path_info, "a") as f:
        write = "N " + files[i] + "\nH " # N meaning name and H meaning histogram
        f.write(write)
        img.histogram.tofile(f, " ", "%s")
        f.write("\n\n")

data = MyDataset()