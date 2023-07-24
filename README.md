# menu_app
# Клонируем приложение из репозитория переходим в него
git clone https://github.com/7Sunset7/menu_app.git
# Переходим в него  
cd menu_app
# Устанавливаем зависимости 
python -m pip install -r requirements.txt
# Меняем значения в переменных окружения на свои
В файле .env изменить данные для подключения к бд на свои
# Запускаем сервер и тесты
Запусаем сервер командой uvicorn main:app --reload и тестируем через postman 
