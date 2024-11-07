import argparse
import csv
import os
from icrawler.builtin import GoogleImageCrawler


def arg_parser() -> tuple[str, str, str]:
    """
    Парсинг аргументов командной строки
    :return: кортеж из ключевого слова для поиска,
    пути к папке для сохранения и пути к файлу аннотации
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--key_word', type=str, default='pig',
                        help='the search keyword')
    parser.add_argument('--save_folder', type=str, default='images',
                        help='the path to the folder to save(absolute/relative)')
    parser.add_argument('--annotation_path', type=str, default='annotation.csv',
                        help='the path to the annotation file(absolute/relative)')
    args = parser.parse_args()
    return args.key_word, args.save_folder, args.annotation_path


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
        file_abspath = os.path.join(files_folder, file)
        data.append([file, os.path.abspath(file_abspath), get_relative_path(file_abspath)])
    os.makedirs(os.path.abspath(os.path.dirname(annotation_path)), exist_ok=True)
    with open(annotation_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)


class ImageIterator:
    def __init__(self, source: str):
        self.source = source
        self.image_paths = []
        self.index = 0

        # Если source - это файл-аннотация
        if os.path.isfile(source):
            with open(source, mode='r', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader)  # Пропускаем заголовок
                for row in reader:
                    self.image_paths.append(row[1])  # Предполагаем, что абсолютный путь к изображению во втором столбце
        # Если source - это папка
        elif os.path.isdir(source):
            self.image_paths = [os.path.join(source, file) for file in os.listdir(source)]
        else:
            raise ValueError("Указанный источник не является файлом или папкой.")

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.image_paths):
            image_path = self.image_paths[self.index]
            self.index += 1
            return image_path
        else:
            raise StopIteration


def main():
    key_word, save_folder, annotation_path = arg_parser()
    image_download(key_word, save_folder, 50)
    create_annotation(annotation_path, save_folder)


if __name__ == '__main__':
    main()