# menu_app
# Клонируем приложение и переходим в него
git clone https://github.com/7Sunset7/menu_app.git
cd menu_app
# Запускаем контейнер с приложением и базой данных
docker-compose up --build -d
# Останавливаем его
docker-compose down
# Запускаем контейнер с приложением и тестовой базой данных
docker-compose -f docker-compose_test.yaml up --build -d
# Запускаем тестирование приложения
docker-compose -f docker-compose_test.yaml run test
# Останавливаем контейнер с приложением и тестовой базой данных
docker-compose -f docker-compose_test.yaml down