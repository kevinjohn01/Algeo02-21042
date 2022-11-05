from typing import List
import cv2
import numpy as np
import os


def load_image_data(folder: str, recursive: bool = False) -> np.ndarray:
    prev_dir = os.path.abspath('.')
    data: List[np.ndarray] = []
    if (recursive):
        for dirpath, _, files in os.walk(folder):
            for file in files:
                os.chdir(dirpath)
                img = cv2.resize(cv2.imread(file, 0), (100, 100), interpolation=cv2.INTER_AREA)
                data.append(img)
    else:
        os.chdir(folder)
        for file in os.listdir():
            img = cv2.resize(cv2.imread(file, 0), (100, 100), interpolation=cv2.INTER_AREA)
            data.append(img)
    os.chdir(prev_dir)
    return np.array(data, dtype=np.ndarray)


def matrix_mean(mat: np.ndarray) -> np.ndarray:
    return np.mean(mat, axis=0, dtype=np.float64)
