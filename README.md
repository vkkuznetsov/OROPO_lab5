# Развертывание и запуск проекта

Этот проект использует Makefile для автоматизации основных шагов установки, тестирования и запуска. Перед тем как начать, убедитесь, что у вас настроено окружение и правильные значения в файле конфигурации.

## Шаг 1: Установка зависимостей
Перед тем как начать работу с проектом, создайте виртуальное окружение и установите зависимости.

### Для Linux/MacOS:
Перейдите в директорию проекта.

Выполните команду для создания виртуального окружения и установки зависимостей:

```bash
make install
```
### Для Windows:
Перейдите в директорию проекта.

Выполните команду для создания виртуального окружения и установки зависимостей:

```bash
make winstall
```
Это создаст виртуальное окружение и установит все необходимые зависимости из файла requirements.txt.

## Шаг 2: Настройка конфигурации
Перед тем как запускать приложение, убедитесь, что файл конфигурации config.settings.yml настроен правильно.

Откройте файл config.settings.yml.
Убедитесь, что все необходимые значения для подключения и настройки приложения указаны в файле. Это может включать, например:
API_SECRET_KEY
Настройки подключения к базе данных

Убедитесь, что вы указали свои значения для всех переменных, прежде чем запускать скрипты.

## Шаг 3: Запуск тестов
После установки зависимостей вы можете запустить тесты проекта с помощью команды:

```bash
make test
```
Это выполнит все тесты с использованием pytest, а также выведет краткий отчет о результатах выполнения.

## Шаг 4: Запуск приложения
После успешной установки зависимостей и настройки конфигурации, вы можете запустить приложение с помощью следующей команды:

ЁЁbash
Копировать код
make run
Это запустит приложение с помощью команды python -m lab и сделает его доступным для работы.