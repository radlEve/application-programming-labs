import argparse
import re


def arg_parser() -> tuple[str, str, str]:
    """
    Парсинг аргументов командной строки
    :return: кортеж из названия читаемого файла, искомого пола и буквы
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('file_name', type=str, help='name of file')
    parser.add_argument('gender', type=str, help='the desired gender')
    parser.add_argument('letter', type=str, help='the desired letter')
    args = parser.parse_args()
    return args.file_name, args.gender, args.letter


def file_read(file_name: str) -> str:
    """
    Прочесть файл и вернуть его в виде строки
    """
    try:
        with open(file_name, 'r', encoding = 'utf-8') as file:
            return file.read()
    except FileNotFoundError:
        raise ValueError("Файл не найден: проверьте имя файла!")
    except PermissionError:
        raise PermissionError("Недостаточно прав для чтения файла!")
    except Exception as ex:
        raise Exception(ex)


def split(string: str) -> list[str]:
    """
    Разделить строку string, записанную в формате "1)1текст2)2текст3)текст..." на список из элементов
    ['1текст', '2текст', '3текст']
    """
    pattern = r'\d+\)'
    listed = re.split(pattern, string)
    return listed[1::]


def find(text: str, gender: str, letter: str) -> list[str]:
    """
    Найти в тексте имена, удовлетворяющие условию
    :param text: неразделенный текст, содержащий всё
    :param gender: искомый пол (М/Ж)
    :param letter: искомая первая буква имени
    :return: список, состоящий из всех найденных имен, удовлетворяющих условию
    """
    profiles = split(text)
    suitableness = set()
    for profile in profiles:
        gender_match = re.search(r'Пол:\s*\w', profile)
        if gender_match is not None and gender_match.group()[-1] == gender:
            letter_match = re.search(r'Имя:\s\w', profile)
            if letter_match is not None and letter_match.group()[-1] == letter:
                suitableness.add(re.search(r'Имя:\s\w*', profile).group()[5::])
    return list(suitableness)


def main():
    try:
        file_name, gender, letter = arg_parser()
        data = file_read(file_name)
        answer = find(data, gender, letter)
        print(answer)
    except Exception as ex:
        print(f"Что-то пошло не так: \"{ex}\"")


if __name__ == '__main__':
    main()