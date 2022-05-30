#### Тестовое задание - тестирование API:  https://www.openbrewerydb.org

Протестировать API сайта https://www.openbrewerydb.org/ с использованием pytest:
- написать минимум 10 тестов
- из них минимум 2 параметризованных
- 1 тест параметризован через фикстуру
- обязательно валидация json-ответов
- минимальная тестовая документация (почему выбраны те или иные тесты, приоритезация тестов и др.)
- задание-бонус: обеспечить возможность запуска данного набора тестов в докере

---

В тестах проверяется основной функционал, описанный в https://www.openbrewerydb.org/documentation (Single Brewery, List Breweries, Random Brewery, Search Breweries). 
4 параметризованных теста (с разными query параметрами), 3 негативных теста (с некорректным id, удаление json-объекта, создание-json объекта)

Использовались библиотеки:
- requests - для работы с http-запросами
- pydantic - для валидации json-ответов
- pytest - для выполненитя тестового кода

Для запуска тестов внутри контейнера
```console
foo@bar:~PROJECT_PATH$ docker build -t pytest_container_image . 
foo@bar:~PROJECT_PATH$ docker run --rm -ti pytest_container_image /bin/sh
# pytest -v 
```
