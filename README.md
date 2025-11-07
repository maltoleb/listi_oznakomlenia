# 📘 Листы ознакомления (pet-project)

CLI-утилита для автоматического формирования **листов ознакомления сотрудников**  
по данным Excel-файла и шаблону Word.

---

## 🚀 Функциональность
- 📂 Читает Excel-файлы со списком сотрудников
- 🧩 Группирует их по участкам / начальникам
- 📝 Генерирует Word-документы по шаблону
- ⚙️ Поддерживает конфигурацию через `config.json`

---

## 🧱 Структура проекта
.
├── main.py
├── requirements.txt
├── data/
│ └── Список сотрудников.xlsx
├── templates/
│ └── Бланк.docx
└── CHANGELOG.md

yaml
Копировать код

---

## 🧩 Git-flow
Основные ветки:
- `main` — стабильные версии (релизы)
- `develop` — текущая разработка
- `feature/*` — отдельные шаги/фичи

---

## 🧰 Установка и запуск
```bash
git clone git@github.com:maltoleb/listi_oznakomlenia.git
cd listi_oznakomlenia
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py