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
    try:
        image_path, save_folder = arg_parser()
        img = cv2.imread(image_path)

        show_hist_im(img)
        print_img_size(img)
        split_image(img, save_folder)
        show_four_im(image_path, 'original image',
                     save_folder + 'imageB.png', 'blue',
                     save_folder + 'imageG.png', 'green',
                     save_folder + 'imageR.png', 'red')

    except Exception as ex:
        print(f"Что-то пошло не так: \"{ex}\"")

if __name__ == '__main__':
    main()