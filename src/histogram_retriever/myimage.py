from PIL import Image
import numpy as np


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
    self.histogram = np.zeros((256, self.img.shape[2]), dtype=np.uint8)
    self.hist_alt = np.zeros((256, self.img.shape[2]), dtype=np.uint8)

  def make_histogram(self):
    print(np.shape(self.img))
    print(np.shape(self.histogram))

    for i in range(self.img.shape[2]):
      self.histogram[:,i], _ = np.histogram(self.img[:,:,i], bins=256, range=(0,255))

    return self.histogram
