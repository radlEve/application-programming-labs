import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel,
                             QFileDialog, QVBoxLayout, QWidget)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

from imageIterator import ImageIterator


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Просмотр датасета")

        self.image_label = QLabel(self)
        self.image_label.setFixedSize(800, 600)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_label.setText("Папка не выбрана")

        self.next_button = QPushButton("Следующее изображение", self)
        self.next_button.clicked.connect(self.show_next_image)

        self.open_button = QPushButton("Выбрать папку датасета", self)
        self.open_button.clicked.connect(self.open_dataset_folder)

        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.next_button)
        layout.addWidget(self.open_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        self.iterator = None
        self.image_count = 0


    def open_dataset_folder(self) -> None:
        folder_path = QFileDialog.getExistingDirectory(self, "Выберите папку с датасетом")
        if folder_path:
            try:
                self.iterator = ImageIterator(folder_path)
                # Проверка, есть ли изображения
                self.image_count = len(self.iterator.image_paths)
                if self.image_count == 0:
                    self.image_label.setText("Изображения отсутствуют")
                    self.iterator = None
                else:
                    self.show_next_image()
            except ValueError as e:
                self.image_label.setText(f"Ошибка: {e}")
                self.iterator = None

    def show_next_image(self) -> None:
        if not self.iterator:
            self.image_label.setText("Папка не выбрана")
            return  # Завершаем функцию если итератора нет
        try:
            image_path = next(self.iterator)
            pixmap = QPixmap(image_path)
            self.image_label.setPixmap(pixmap.scaled(self.image_label.size(),
                                                    Qt.AspectRatioMode.KeepAspectRatio))
        except StopIteration:
            self.image_label.setText("Больше изображений нет")


def main():
    try:
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec())

    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()