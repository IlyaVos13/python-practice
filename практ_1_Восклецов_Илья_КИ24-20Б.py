from datetime import datetime

def f():
    print("string")
    a = input()
    if a == "y":
        return True
    if a == "n":
        return False
    else:
        return f()

    

def input_passport():
    while True:
        passport = input("введите паспорт (SS SS-NNNNNN): ")

        if len(passport) == 12 and passport[2] == " " and passport[5] == "-":
            if passport[:2].isdigit() and passport[3:5].isdigit() and passport[6:].isdigit():
                return passport

        print("ошибка! неверный формат паспорта")


def input_name():
    while True:
        name = input("введите имя: ")

        if name != "":
            return name

        print("ошибка! имя не может быть пустым")


def input_date():
    while True:
        date = input("введите дату рождения (YYYY-MM-DD): ")

        try:
            datetime.strptime(date, "%Y-%m-%d")
            return date
        except ValueError:
            print("ошибка! неверная дата")


def input_phone():
    while True:
        phone = input("введите телефон (+X(XXX) XXX-XX-XX или X(XXX) XXX-XXXX): ")

        if phone.startswith("+"):
            if (
                len(phone) == 17
                and phone[2] == "("
                and phone[6] == ")"
                and phone[7] == " "
                and phone[11] == "-"
                and phone[14] == "-"
            ):
                return phone

        elif (
            len(phone) == 15
            and phone[1] == "("
            and phone[5] == ")"
            and phone[6] == " "
            and phone[10] == "-"
        ):
            return phone

        print("ошибка! неверный формат телефона")


def input_temperature():
    while True:
        try:
            temperature = float(input("введите температуру (XX.XX): "))

            if -100 <= temperature <= 100:
                return temperature

            print("ошибка! температура должна быть от -100 до 100")

        except ValueError:
            print("ошибка! введите число.")


def main():
        print("ввод данных пациента")

        passport = input_passport()
        name = input_name()
        birth_date = input_date()
        phone = input_phone()
        temperature = input_temperature()

        print("\nданные пациента")
        print("паспорт:", passport)
        print("имя:", name)
        print("дата рождения:", birth_date)
        print("телефон:", phone)
        print("температура:", temperature)


main()