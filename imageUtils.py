import cv2
import numpy as np
import matplotlib.pyplot as plt


def print_img_size(img: np.ndarray) -> None:
    """
    Выводит разрешение изображения в консоль
    :param img: изображение в формате массива Numpy
    :return: None
    """
    try:
        if img is None:
            raise ValueError(f"Не удалось загрузить изображение")
        print(f'Height: {img.shape[0]}, width: {img.shape[1]}')

    except Exception as e:
        raise ValueError(f"Ошибка: {e}")


def show_hist_im(img: np.ndarray) -> None:
    """
    Строит и показывает гистограмму изображения (по 3 цветам)
    :param img: изображение в формате массива NumPy
    :return: None
    """
    try:
        if img is None:
            raise ValueError(f"Не удалось загрузить изображение")
        color = ('b', 'g', 'r')
        for i, col in enumerate(color):
            histr = cv2.calcHist([img], [i], None, [256], [0, 256])
            plt.plot(histr, color=col)
            plt.xlim([0, 256])
        plt.xlabel('pixel values')
        plt.ylabel('No. of pixels')
        plt.grid(color='gray', linestyle='--', linewidth=0.5)
        plt.show()

    except Exception as e:
        raise ValueError(f"Ошибка: {e}")


def show_four_im(image1_path: str, description1: str, image2_path: str, description2: str,
                 image3_path: str, description3: str, image4_path:str, description4: str) -> None:
    """
    Показывает в одном окне 4 изображения с соответствующими подписями
    :param image1_path: путь к первому изображению
    :param description1: подпись для 1-го изображения
    :param image2_path: путь ко второму изображению
    :param description2: подпись для 2-го изображения
    :param image3_path: путь к третьему изображению
    :param description3: подпись для 3-го изображения
    :param image4_path: путь к четвертому изображению
    :param description4: подпись для 4-го изображения
    :return: None
    """
    try:
        images = [image1_path, image2_path, image3_path, image4_path]
        image_data = []

        for img_path in images:
            img = cv2.imread(img_path)
            if img is None:
                raise ValueError(f"Не удалось загрузить изображение \"{img_path}\"")
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Преобразование в RGB
            image_data.append(img)

        fig = plt.figure(figsize=(10, 7))
        for i in range(4):
            fig.add_subplot(2, 2, i + 1)
            plt.imshow(image_data[i])
            plt.axis('off')
            plt.title([description1, description2, description3, description4][i])
        plt.show()

    except Exception as e:
        raise ValueError(f"Ошибка: {e}")


def split_image(img: np.ndarray, save_folder: str) -> None:
    """
    Разделяет изображение на 3 канала и сохраняет каждый канал
    в отдельный файл по указанному пути
    :param img: исходное изображение в формате массива Numpy
    :param save_folder: путь к папке, в которую необходимо сохранить
    изображение, разделенное по каналам
    :return: None
    """
    try:
        if img is None:
            raise ValueError(f"Не удалось загрузить изображение")

        img_b = np.zeros_like(img)
        img_g = np.zeros_like(img)
        img_r = np.zeros_like(img)
        img_b[:, :, 0] = img[:, :, 0]  # Синий канал
        img_g[:, :, 1] = img[:, :, 1]  # Зеленый канал
        img_r[:, :, 2] = img[:, :, 2]  # Красный канал

        cv2.imwrite(save_folder + 'imageB.png', img_b)
        cv2.imwrite(save_folder + 'imageG.png', img_g)
        cv2.imwrite(save_folder + 'imageR.png', img_r)

    except Exception as e:
        raise ValueError(f"Ошибка: {e}")
