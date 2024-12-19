import matplotlib.pyplot as plt
import pandas as pd


def show_hist(col: pd.Series) -> None:
    """
    Построить и отобразить гистограмму распределения площадей изображений.
    :param col: колонка, по которой строится гистограмма
    :return: None
    """
    plt.hist(col, bins=20, color='skyblue', edgecolor='black')
    plt.xlabel(col.name)
    plt.ylabel('Количество изображений')
    plt.title(f'Распределение {col.name}')
    plt.grid(axis='y', alpha=0.75)
    plt.show()