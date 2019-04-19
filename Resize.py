import os
import cv2


def resize(path, new_path):
    for i, image in enumerate(os.listdir(path)):
        resized_image = cv2.resize(cv2.imread(f'{path}/{image}'), (512, 512))
        cv2.imwrite(f'{new_path}/{i}.png', resized_image)


if __name__ == '__main__':
    path = "F:/Data"
    new_path = "F:/Data"
    resize(path, new_path)

