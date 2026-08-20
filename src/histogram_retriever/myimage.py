from PIL import Image
import numpy as np


class Histogram:
  def __init__(self, img):
    self.hist = np.zeros((256, img.shape[2]))
    for i in range(img.shape[2]):
          self.hist[:,i], _ = np.histogram(img[:,:,i], bins=256, range=(0,255), density=True)

class MyImage:

  def __init__(self, name="input.png", histogram=None, hist_alt=None, img=None, img_alt=None,
               path="/home/francisco/histogram-retriever/input/input.png") -> None:
    self.name = name
    self.path = path

    loaded = np.array(Image.open(self.path))

    # Check for greyscale
    if loaded.ndim == 2:
      loaded = np.stack([loaded, loaded, loaded], axis=-1)
    if loaded.shape[-1] not in (3, 4):
      raise ValueError(f"Unsupported number of channels: {loaded.shape}")

    self.img = loaded
    self.histogram = Histogram(self.img)
    # self.hist_alt = 
