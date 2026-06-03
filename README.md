# Домашняя работа 2
#### Выполнил Егор Маштаков ББИ2505

## Установка и запуск 
#### 1. Клонируйте репозиторий
```bash
git clone https://github.com/egor-mashtakov/HW2_TP
```
#### 2. Перейдите в папку
```bash
cd HW2_TP
```

#### 3 Создайте виртуальное окружение
```bash
python -m venv .venv
```

#### 4 Активируйте виртуальное окружение
```bash
# Mac/Linux
source .venv/bin/activate

# Win(CMD)
.venv\Scripts\activate.bat

# Win(PowerShell)
.venv\Scripts\Activate.ps1
```
#### 5. Установите зависимости
```bash
pip install -r requirements.txt

# Альтернативно, так как в проекте используется pyproject.toml:
pip install .
```

#### 6. Запустите тесты
```bash
pytest
```