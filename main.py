import argparse

from imageUtils import *


def arg_parser() -> tuple[str, str]:
    """
    Парсинг аргументов командной строки
    :return: кортеж из пути к изображению и пути к папке для сохранения
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--image_path', type=str, default='image.png',
                        help='the path to the image')
    parser.add_argument('--save_folder', type=str, default='',
                        help='the path to the folder to save(absolute/relative)')
    args = parser.parse_args()
    return args.image_path, args.save_folder


def main():
    image_path, save_folder = arg_parser()
    show_hist_im(image_path)
    print_img_size(image_path)
    split_image(image_path, save_folder)
    show_four_im(image_path, 'original image',
                 save_folder + 'imageB.png', 'blue',
                 save_folder + 'imageG.png', 'green',
                 save_folder + 'imageR.png', 'red')


if __name__ == '__main__':
    main()