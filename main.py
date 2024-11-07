import argparse

from imageIterator import ImageIterator
from imageUtils import image_download, create_annotation


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


def main():
    key_word, save_folder, annotation_path = arg_parser()
    image_download(key_word, save_folder, 50)
    create_annotation(annotation_path, save_folder)

    print("Annotation iterator:")
    paths = ImageIterator(annotation_path)
    for path in paths:
        print(path)

    print("Image folder iterator:")
    paths = ImageIterator(save_folder)
    for path in paths:
        print(path)


if __name__ == '__main__':
    main()