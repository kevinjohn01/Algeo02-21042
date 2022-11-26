from typing import List
import cv2
import numpy as np
import os


def load_image_data(
    folder: str, recursive: bool = False, max_img_per_folder: int = -1
):
    prev_dir = os.path.abspath(".")
    data = []
    image_paths = []
    if recursive:
        for dirpath, _, files in os.walk(folder):
            print(dirpath)
            count = 0
            for file in files:
                filepath = os.path.abspath(os.path.join(dirpath, file))
                img = cv2.resize(
                    cv2.imread(filepath, 0), (100, 100), interpolation=cv2.INTER_CUBIC
                )
                image_paths.append(filepath)
                data.append(img)
                count += 1
                if count == max_img_per_folder:
                    break
    else:
        os.chdir(folder)
        for file in os.listdir():
            img = cv2.resize(
                cv2.imread(file, 0), (100, 100), interpolation=cv2.INTER_CUBIC
            )
            data.append(img)
    os.chdir(prev_dir)
    return np.array(data), image_paths
