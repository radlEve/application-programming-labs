import matplotlib.pyplot as plt
import pandas as pd


def show_hist(df: pd.DataFrame) -> None:
    """
    Построить и отобразить гистограмму распределения площадей изображений.
    :param df: DataFrame с колонкой 'area'.
    :return: None
    """
    plt.hist(df['area'], bins=20, color='skyblue', edgecolor='black')
    plt.xlabel('Площадь изображения')
    plt.ylabel('Количество изображений')
    plt.title('Распределение площадей изображений')
    plt.grid(axis='y', alpha=0.75)
    plt.show()