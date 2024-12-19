import pandas as pd

from imageUtils import get_image_specs


def create_dataframe(csv_file: str) -> pd.DataFrame:
    """
    Создать DataFrame из CSV файла
    :param csv_file: путь к CSV файлу
    :return: DataFrame с колонками "absolute_path" и "relative_path"
    """
    try:
        df = pd.read_csv(csv_file)
        df.columns = ['absolute_path', 'relative_path']
        return df
    except FileNotFoundError as e:
        raise FileNotFoundError(f'Файл не найден: {e}')
    except Exception as e:
        raise Exception(f"Ошибка при чтении CSV: {e}")


def add_img_specs(df: pd.DataFrame) -> None:
    """
    Добавить в DataFrame колонки 'height', 'width', 'channels' и 'area' с информацией об изображениях
    :param df: DataFrame, содержащий колонку 'absolute_path'
    :return: None
    """
    try:
        df[['height', 'width', 'channels']] = df['absolute_path'].apply(lambda x: pd.Series(get_image_specs(x)))
        df['area'] = df['height'] * df['width']
    except Exception as e:
        raise Exception(f'Не удалось получить характеристики изображения: {e}')


def get_stats(df: pd.DataFrame) -> pd.DataFrame:
    """
    Вычислить статистическую информацию по колонкам 'height', 'width', 'channels'.
    :param df: DataFrame, содержащий колонки 'height', 'width', 'channels'
    :return: DataFrame со статистической информацией
    """
    stats = df[['height', 'width', 'channels']].describe()
    return stats

def filter_by_size(df: pd.DataFrame, max_width: int, max_height: int) -> pd.DataFrame:
    """
    Отфильтровать DataFrame по максимальной ширине и высоте изображения.
    :param df: DataFrame с колонками 'height' и 'width'.
    :param max_width: максимальная ширина изображения.
    :param max_height: максимальная высота изображения.
    :return: отфильтрованный DataFrame.
    """
    filtered_df = df[(df['height'] <= max_height) & (df['width'] <= max_width)]
    return filtered_df

def sort_by_area(df: pd.DataFrame) -> pd.DataFrame:
    """
    Отсортировать DataFrame по площади изображения.
    :param df: DataFrame с колонкой 'area'.
    :return: отсортированный DataFrame.
    """
    df_sorted = df.sort_values(by='area')
    return df_sorted