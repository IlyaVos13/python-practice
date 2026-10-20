import argparse
import re


def read_file(file_name):
    objects = []

    point_pattern = r"^Point\(\s*-?\d+(\.\d+)?\s*,\s*-?\d+(\.\d+)?\s*\)$"

    line_pattern = r"^Line\(\s*Point\(\s*-?\d+(\.\d+)?\s*,\s*-?\d+(\.\d+)?\s*\)\s*,\s*Point\(\s*-?\d+(\.\d+)?\s*,\s*-?\d+(\.\d+)?\s*\)\s*\)$"

    circle_pattern = r"^Circle\(\s*Point\(\s*-?\d+(\.\d+)?\s*,\s*-?\d+(\.\d+)?\s*\)\s*,\s*\d+(\.\d+)?\s*\)$"

    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if re.fullmatch(point_pattern, line):
                objects.append(line)

            elif re.fullmatch(line_pattern, line):
                objects.append(line)

            elif re.fullmatch(circle_pattern, line):
                objects.append(line)

            elif line != "":
                print("Некорректная строка:", line)

    return objects


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-f",
        "--file",
        required=True,
        help="Путь к файлу"
    )

    parser.add_argument(
        "-o",
        "--oper",
        required=True,
        choices=["print", "count"],
        help="Операция: print или count"
    )

    args = parser.parse_args()

    try:
        objects = read_file(args.file)
    except FileNotFoundError:
        print("Ошибка: файл не найден")
        return

    if args.oper == "print":
        for obj in objects:
            print(obj)

    elif args.oper == "count":
        print(len(objects))


if __name__ == "__main__":
    main()
