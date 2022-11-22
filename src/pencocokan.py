from imgprocess import load_image_data
from eigen import eigens
import cv2
import numpy as np


K = 37
IMG_PER_FOLDER = 5
THRESHOLD = 5000


def get_eigenfaces(dataset_folder):
    images, image_paths = load_image_data(
        dataset_folder, recursive=True, max_img_per_folder=IMG_PER_FOLDER
    )
    gamma = []
    for i in range(images.shape[0]):
        gamma.append(np.reshape(images[i], (10000, 1)))

    gamma = np.array(gamma, dtype=np.uint8)
    avg_face = gamma.mean(axis=0)
    A = []
    normalized_faces = []
    for i in range(gamma.shape[0]):
        normalized_face = gamma[i] - avg_face
        normalized_faces.append(normalized_face)
        A.append(normalized_face)

    A = np.column_stack(A)
    cov = A.T @ A
    e, v = np.linalg.eig(cov)
    eigenfaces = []
    for i in range(v.shape[0]):
        eigenfaces.append(A @ v[i])

    order = np.argsort(e)[::-1]
    return np.array(eigenfaces)[order][:K], images, normalized_faces, avg_face, image_paths


def test_image(dataset, filepath):
    print(filepath)
    test_image = cv2.imread(filepath, 0)
    test_image = cv2.resize(test_image, (100, 100), interpolation=cv2.INTER_CUBIC)
    test_image = np.reshape(test_image, (10000, 1))
    eigenfaces, images, normalized_faces, avg_face, image_paths = get_eigenfaces(dataset)
    phi = test_image - avg_face
    test_image_weights = []
    for i in range(min(K, len(images))):
        test_image_weights.append(eigenfaces[i].T @ phi)
    test_image_weights = np.row_stack(test_image_weights)
    omega = []
    print(len(images))
    for i in range(len(images)):
        weights = []
        for j in range(min(K, len(images))):
            weights.append(eigenfaces[j].T @ normalized_faces[i])
        omega.append(np.row_stack(weights))
    idxmin = -1
    euclid = 999999999999
    for i in range(len(omega)):
        euclid_i = np.linalg.norm(omega[i] - test_image_weights)
        if euclid_i < euclid and euclid_i <= THRESHOLD:
            idxmin = i
            euclid = euclid_i
    return image_paths[idxmin] #if idxmin != -1 else ''


def euclidean_distance(a, b):
    assert a.shape == b.shape, "operan harus berupa vector dengan dimensinya sama"
    sum = 0
    for i in range(a.shape[0]):
        sum += (a[i][0] - b[i][0]) ** 2
    return np.sqrt(sum)

'''
if __name__ == "__main__":
    img = test_image(
        "dataset",
        "D:\Tubes algeo\dataset\pins_Tom Hiddleston\Tom Hiddleston18_1485.jpg",
    )
    print(img)
'''
