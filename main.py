import pandas as pd
from pathlib import Path


def load_employees(path):
    return pd.read_excel(
        path,
        skiprows=4,
        usecols=[
            "ФИО",
            "Должность (специальность, профессия), класс (категория) квалификация",
            "Орг.Ед. 1.1",
        ],
    )

if __name__ == "__main__":
    excel_files = list(Path("data").glob("*.xls")) + list(Path("data").glob("*.xlsx"))
    if not excel_files:
        print("В папке data нет Excel-файлов (.xls или .xlsx)!")
        exit(1)
    path = excel_files[0]
    print(f"Найден файл: {path.name}")
    df = load_employees(path)
    print(df.head())
