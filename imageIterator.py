import csv
import os


class ImageIterator:
    def __init__(self, image_folder_or_annotation: str):
        self.source = image_folder_or_annotation
        self.image_paths = []
        self.index = 0

        # Если source - это файл-аннотация
        if os.path.isfile(image_folder_or_annotation):
            with open(image_folder_or_annotation, mode='r', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader)  # Пропускаем заголовок
                for row in reader:
                    self.image_paths.append(row[1])  # Предполагаем, что абсолютный путь к изображению во втором столбце
        # Если source - это папка
        elif os.path.isdir(image_folder_or_annotation):
            self.image_paths = [os.path.join(image_folder_or_annotation, file) for file in os.listdir(image_folder_or_annotation)]
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