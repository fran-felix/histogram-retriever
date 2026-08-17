import os
from PIL import Image
import numpy as np
import histogram_retriever.myimage as myimage

def tar() -> None:
    path = "/home/francisco/histogram-retriever/Vistex"
    files = [f for f in os.listdir(path) if f.endswith('png')]
    n = len(files)
    for i in range (n):
        path_img = os.path.join(path, files[i])
        img = Image.open(path_img)
        img = np.array(img)
        print(img)

def main() -> None:
    img1 = myimage.MyImage()
    img1.test_print()

if __name__ == "__main__":
    main()