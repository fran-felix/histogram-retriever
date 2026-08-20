import os
import histogram_retriever.myimage as myimage
import histogram_retriever.dataset as dataset
import numpy as np


def classify(k=5, img_path='/home/francisco/histogram-retriever/input/input.png',
             data_path='/home/francisco/histogram-retriever/Vistex/') -> int:
    data = dataset.MyDataset(input_img = myimage.MyImage(path=img_path),path=data_path)
    data.build_likeness_array()
    closest = data.closest(k)
    if closest[1].size == 0:
        raise ValueError("k must be greater than zero.")

    class_ids, counts = np.unique(closest[1], return_counts=True)
    return int(class_ids[np.argmax(counts)])

def validate(k=5, path_data='/home/francisco/histogram-retriever/Vistex/') -> float:
    files = [f for f in os.listdir(path_data) if f.endswith('png')]
    n = len(files)

    hits = 0
    data = dataset.MyDataset(path=path_data)

    for i in range(n):
        path_img = os.path.join(path_data, files[i])
        img = myimage.MyImage(name=files[i],path=path_img)

        data.input_img = img
        data.build_likeness_array()
        closest = data.closest(k)
        class_ids, counts = np.unique(closest[1], return_counts=True)
        img_class = int(class_ids[np.argmax(counts)])
        real_class = img.get_class_id()

        if img_class == real_class: hits += 1

    return (hits / n)


def main() -> None:
    
    print(validate(5))

if __name__ == "__main__":
    main()