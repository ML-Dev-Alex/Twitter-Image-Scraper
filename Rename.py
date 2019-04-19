import os
import re


def rename(path):
    for i, image in enumerate(os.listdir(path)):
        image_path = f'{path}/{image}'

        if os.path.exists(image_path):
            extension = re.findall(r"^.*\.(JPEG|jpeg|jpg|JPG|gif|GIF|png|PNG)$", image)
            if not extension:
                continue
            extension = str(extension[0]).lower()

            if extension == "gif":
                new_file_path = f'{path}/food{i}.gif'
            elif extension == "jpg" or extension == "jpeg":
                new_file_path = f'{path}/food{i}.jpg'
            elif extension == "png":
                new_file_path = f'{path}/food{i}.png'
            else:
                print(f'error on file : {image_path}')
            os.rename(image_path, new_file_path)


if __name__ == '__main__':
    path = "F:/Data"
    rename(path)
