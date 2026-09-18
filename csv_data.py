import csv

fieldnames = ["date", "base", "quote", "rate"]

def write_data(data: list[dict]) -> None:
    with open(file= 'new_file.csv', mode= 'w', newline= '') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames= fieldnames)
        writer.writeheader()
        writer.writerows(data)


def read_data(filepath: str) -> list[dict]:
    with open(file= filepath, mode= 'r', newline= '') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)
    return data