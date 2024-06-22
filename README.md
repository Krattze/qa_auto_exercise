# API & UI autotest for www.automationexercise.com
Этот проект содержит автоматические тесты на Python для веб-сайта www.automationexercise.com, используя паттерн Page Object Model (POM) для структурирования кода. Проект включает как API, так и UI тесты для проверки функциональности сайта, реализованные с использованием Playwright.
## Чтобы запустить, проект:
- Установить библиотеки из requirements.txt
- Установить allure
- Запустить тесты: pytest --alluredir allure-results
- Для генерации отчета: allure serve allure-results
## Отчеты в allure
### Обзор
![image](https://github.com/Krattze/qa_auto_exercise/assets/82762876/cbbfb85a-6c6b-4e05-8cb0-504e9a40017d)
### Пример отчета для API теста
![image](https://github.com/Krattze/qa_auto_exercise/assets/82762876/b2b34c3a-66d8-4900-96bb-f81438eab533)
### Пример отчета для UI теста
![image](https://github.com/Krattze/qa_auto_exercise/assets/82762876/70e878d4-a18f-42a9-b86a-61d75b679ffa)


