import csv
import os
import cv2


def get_relative_path(absolute_path: str) -> str:
    """
    Получить путь относительно исполняемого файла из полного пути
    :param absolute_path: полный путь к файлу
    :return: путь к файлу относительно исполняемого файла
            (если на др. диске или вне директории с исполняемым файлом, возвращается полный путь)
    """
    active_dir = os.getcwd()
    if active_dir in absolute_path:
        return absolute_path.replace(active_dir + '\\', '')
    return absolute_path


def create_annotation(annotation_path: str, files_folder: str) -> None:
    """
    Создать аннотацию в виде файла по указанному пути с названием файла
    :param annotation_path: путь к создаваемому файлу аннотации
    :param files_folder: путь к папке, содержащей файлы, описываемые в аннотации
    :return: None
    """
    file_list = os.listdir(files_folder)
    data = [["Absolute path", "Relative path"]]
    for file in file_list:
        file_abspath = os.path.abspath(os.path.join(files_folder, file))
        data.append([file_abspath, get_relative_path(file_abspath)])
    os.makedirs(os.path.abspath(os.path.dirname(annotation_path)), exist_ok=True)
    with open(annotation_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def get_image_specs(image_path: str) -> tuple[int, int, int]:
    """
    Получить высоту, ширину и количество каналов изображения
    :param image_path: путь к изображению
    :return: кортеж из высоты, ширины и количества каналов изображения
    """
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f'Не удалось прочитать изображение по пути {image_path}')
    height, width, channels = img.shape
    return height, width, channels