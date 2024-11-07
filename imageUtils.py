import csv
import os

from icrawler.builtin import GoogleImageCrawler


def image_download(keyword: str, save_folder: str, max_num: int) -> None:
    """
    Скачать изображения и сохранить их в указанную папку
    :param keyword: ключевое слово для поиска изображений
    :param save_folder: папка, в которую сохраняются изображения
    :param max_num: число изображений, которые необходимо скачать
    :return: None
    """
    google_crawler = GoogleImageCrawler(storage={'root_dir': save_folder})
    google_crawler.crawl(keyword=keyword, max_num=max_num)


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
    data = [["Image", "Absolute path", "Relative path"]]
    for file in file_list:
        file_abspath = os.path.abspath(os.path.join(files_folder, file))
        data.append([file, file_abspath, get_relative_path(file_abspath)])
    os.makedirs(os.path.abspath(os.path.dirname(annotation_path)), exist_ok=True)
    with open(annotation_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)