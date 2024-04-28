# geocoder-test-task
## Запуск в Docker
- Склонируйте репозиторий, загрузите зависимости и создайте `.env` файл из шаблона:

```bash
git clone https://github.com/bleschunov/geocoder_test_task.git
cd geocoder_test_task
cat .env.template >> .env
```

- В `.env` заполните переменные окружения.
  - В `DOUBLE_GIS_API_KEY` укажите API KEY из личного кабинета 2GIS 
  - В `DB_CONNECTION_STRING` укажите строку подключения к базе данных в формате: `postgresql+asyncpg://db_user:db_password@db_host:db_host/db_name`
  - В `POSTGRES_USER` и `PGUSER` можно поставить одинаковые значения.
  - В `POSTGRES_HOST` нужно поставить postgres [название сервиса в docker-compose.yml], так как далее будет запускать в контейнере.

Выполните команды

```bash
docker compose -f docker-compose.service.yml -f docker-compose.db.yml up 
```

Вам будет доступен SwaggerUI по ссылке `http://localhost:8080/docs`


## Как запустить тесты локально?

Создайте `.env.test`, установите зависимости:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

cat .env >> .env.test
```

Замените хост базы данных в `.env.test` в `DB_CONNECTION_STRING` и в `POSTGRES_HOST` на `localhost`

Запустите тестовую базу:
```bash
docker compose -f docker-compose.testdb.yml up -d
```

Чтобы запустить каждый из тестов выполните команды:

```bash
python test/test_src/test_model/test_geocoder_model.py TestGeocoderModel.test_getting_point_from_cache
python test/test_src/test_model/test_geocoder_model.py TestGeocoderModel.test_getting_point_from_api
python test/test_src/test_model/test_geocoder_model.py TestGeocoderModel.test_exception_404_if_point_is_not_found
```

## FAQ

### Как понимаешь, что адреса «большая черёмушкинская 20» и «б. черемушкинская, 20» одинаковые?
Использую [расширение PostgreSQL pgtrgm](). В init.sql устанавливается threshold, который можно регулировать для чувствительности сравнения.

### Какой геокодер используешь и почему?
Использую [2GIS геокодер](). Он показался оптимальным по соотношению простоты использования и функционалу.


