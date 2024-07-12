import csv


def read_addresses(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file]


def read_validators(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        return [row[1] for row in reader]


def main():
    og_val_addr = read_validators('og_validators.csv')
    your_addr = read_addresses('your_addr.csv')

    count_in_list = 0
    count_not_in_list = 0

    print("-" * 50)
    print("Проверяем количество наших адресов в списке...")
    print("-" * 50)

    for address in your_addr:
        if address in og_val_addr:
            print(f"{address}")
            print("-" * 50)
            count_in_list += 1
        else:
            count_not_in_list += 1

    print(f"Адресов в списке: {count_in_list}")
    print(f"Количество адресов что не вошли в список: {count_not_in_list}")
    print("-" * 50)

    if count_in_list:
        print("Удача сегодня на нашей стороне!")
    else:
        print("Воркаем дальше!")


if __name__ == "__main__":
    main()
