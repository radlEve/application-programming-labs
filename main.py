import argparse

from hystUtils import show_hist
from imageUtils import *
from pandasUtils import *


def arg_parser() -> tuple[str, str, str]:
    """
    Парсинг аргументов командной строки
    :return: кортеж из пути к изображениям,
    максимальной ширины изображения и
    максимальной высоты изображения
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--image_folder', type=str, default='images',
                        help='photo folder')
    parser.add_argument('--max_width', type=int, default=1920,
                        help='maximum image width')
    parser.add_argument('--max_height', type=int, default=1080,
                        help='maximum image height')
    args = parser.parse_args()
    return args.image_folder, args.max_width, args.max_height


def main():
    try:
        image_folder, max_width, max_height = arg_parser()
        print("1. Создание аннотации и DataFrame...")
        create_annotation('annotation.csv', image_folder)
        df = create_dataframe('annotation.csv') #1-2
        print("   DataFrame создан. Первые 5 строк:")
        print(df.head())

        print("\n2. Добавление характеристик изображений...")
        add_img_specs(df)
        print("   Характеристики изображений добавлены. Первые 5 строк с размерами:")
        print(df.head())

        print("\n3. Вычисление статистической информации...")
        stats = get_stats(df)
        print("   Статистическая информация:")
        print(stats)

        print("\n4. Фильтрация по размеру...")
        df = filter_by_size(df, max_width, max_height)
        print(f"   Отфильтрованный DataFrame. Макс ширина: {max_width}, макс высота: {max_height}. Первые 5 строк:")
        print(df.head())

        print("\n5. Сортировка...")
        df = sort_by_area(df)
        print("   DataFrame отсортирован по площади. Первые 5 строк:")
        print(df.head())

        print("\n6. Построение гистограммы...")
        show_hist(df['area'])
        print("   Гистограмма построена и отображена.")

    except Exception as ex:
        print(f"Что-то пошло не так: \"{ex}\"")


if __name__ == '__main__':
    main()