import argparse
import re

def arg_parser() -> tuple:
    parser = argparse.ArgumentParser()
    parser.add_argument('FileName', type=str, help='name of file')
    parser.add_argument('gender', type=str, help='the desired gender')
    parser.add_argument('letter', type=str, help='the desired letter')
    args = parser.parse_args()
    return args.FileName, args.gender, args.letter

def file_read(file_name: str) -> str:
    """
    Прочесть файл и вернуть его в виде строки
    """
    try:
        with open(file_name, 'r', encoding = 'utf-8') as file:
            return file.read()
    except Exception: raise ValueError("Файл не найден: проверьте имя файла!")


def split(string: str) -> list:
    """
    Разделить строку string, записанную в формате "1)1текст2)2текст3)текст..." на список из элементов
    ['1текст', '2текст', '3текст']
    """
    pattern = r'\d+\)'
    listed = re.split(pattern, string)
    return listed[1::]

def find(text: str, gender: str, letter: str) -> list:
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
        FileName, gender, letter = arg_parser()
        data = file_read(FileName)
        answer = find(data, gender, letter)
        print(answer)
    except ValueError as ve: print(f"Something went wrong: \"{ve}\"")
if __name__ == '__main__':
    main()