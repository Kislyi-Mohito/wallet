FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /wallet_app

# Установка необходимых пакетов
RUN apt-get update && \
    apt-get install -y libpq-dev gcc curl && \
    apt-get clean

# Копируем файл зависимостей
COPY requirements.txt .

# Установка зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы проекта
COPY . .

# Загрузка wait-for-it.sh и установка прав на выполнение
RUN curl -o wait-for-it.sh https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh && \
    chmod +x wait-for-it.sh

# Команда для запуска Django с использованием wait-for-it.sh
CMD ["./wait-for-it.sh", "db:5432", "--", "python", "wallet/manage.py", "runserver", "0.0.0.0:8000"]
